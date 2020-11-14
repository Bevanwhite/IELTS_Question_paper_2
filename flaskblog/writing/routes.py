# Senevirathne S.S. - IT17127042
# 3.0
# 10-05-2020

import joblib
from flask import render_template, Blueprint, flash, url_for, redirect, request, abort
from flask_login import login_user, login_required, current_user
from flaskblog import db
from flaskblog.models import Writingpaper, Writingpaperanswer, Quiz, Create_quiz
from flaskblog.writing.forms import WritingpaperForm, WritingUpdateForm, WritingpaperoneForm
from flaskblog.writing.utils import paper_picture, get_grammar_result, get_cohesion_result, check_spellings
from datetime import datetime
import numpy as np
from spellchecker import SpellChecker
from flask import Flask, request, jsonify
import nltk
# nltk.download('punkt')

""" Load the Writing_Activity_Suggestion.sav file to 
    provide the improvement plan of writing paper
    Train the dataset with the k-neighbors classifier """

activityModel = joblib.load('Writing_Activity_Suggestion.sav')

writing = Blueprint('writing', __name__)


@writing.route("/writing")
def write():
    page = request.args.get('page', 1, type=int)
    writingpapers = Writingpaper.query.paginate(page=page, per_page=6)
    return render_template('writing/writing.html', writingpapers=writingpapers)

    """ Sentnce similarity model 
        Check the similarity of the ielts academic writing task 1 papers' topic sentence """


# Load the cosine_model.sav file
similarity_model = joblib.load('cosine_model.sav')

# Model answer of topic sentence
test_answer1 = "The line graph illustrates the amount of three kinds of spreads (margarine, low fat and reduced spreads and butter) which were consumed over 26 years from 1981 to 2007."

""" text 1 = model answer
    text 2 = candidate answer
    Calculating and returning the cosine similarity using pre trained similarity model """


def cosine_sim(text1, text2):
    index = text2.find(".")
    text2 = text2[:index]
    tfidf = similarity_model.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]


""" Create the writing paper and commit to the database """


@writing.route("/writing/new", methods=['GET', 'POST'])
@login_required
def new_writingpaper():
    form = WritingpaperForm()
    if form.validate_on_submit():
        if form.task01_img.data:
            task01_file = paper_picture(form.task01_img.data)
            writingpaper = Writingpaper(title=form.title.data, task01=form.task01.data, task01_img=task01_file,
                                        wcreator=current_user)
        else:
            writingpaper = Writingpaper(title=form.title.data, task01=form.task01.data, task01_img=form.task01_img.data,
                                        wcreator=current_user)
        db.session.add(writingpaper)
        db.session.commit()
        flash('Your Writing Paper has been Created!', 'success')
        return redirect(url_for('writing.write'))
    return render_template('writing/create_writing.html', title='Writing Paper', form=form, legend='Writing Paper')


""" Get the result of grammar, cohesion and similarity of the topic sentence and commit to the database """


@writing.route("/writing/<int:writing_id>", methods=['GET', 'POST'])
@login_required
def show_writing(writing_id):
    writingpaper = Writingpaper.query.get_or_404(writing_id)
    form1 = WritingpaperoneForm()
    if form1.validate_on_submit():
        grammar_01 = get_grammar_result(form1.task01_answer.data)
        cohesion_01 = get_cohesion_result(form1.task01_answer.data)
        score = cosine_sim(test_answer1, form1.task01_answer.data)
        writing = Writingpaperanswer(pid=writing_id, task=form1.task01_answer.data,
                                     type="type1", grammar=float(grammar_01), cohesion=float(cohesion_01), similarity=str(round(score*100)), wcandidate=current_user)
        db.session.add(writing)
        db.session.commit()
        flash(
            'Your Question 01 Answer has been saved in the database successfully', 'success')
        return redirect(url_for('writing.show_writing', writing_id=writing_id))
    return render_template('writing/writing_paper.html',  writingpaper=writingpaper, form1=form1)


""" Update the writing paper and commit to the database """


@writing.route("/writing/<int:writing_id>/update", methods=['GET', 'POST'])
@login_required
def update_writing(writing_id):
    writing = Writingpaper.query.get_or_404(writing_id)
    if writing.wcreator != current_user:
        abort(403)
    form = WritingUpdateForm()
    if form.validate_on_submit():
        if form.task01_img.data:
            task01_file = paper_picture(form.task01_img.data)
            writing.task01_img = task01_file
        writing.title = form.title.data
        writing.task01 = form.task01.data
        db.session.commit()
        flash('Your Writing Question Papers has been updated', 'success')
        return redirect(url_for('writing.show_writing', writing_id=writing.id))
    elif request.method == 'GET':
        form.title.data = writing.title
        form.task01.data = writing.task01
        form.task01_img.data = writing.task01_img
    return render_template('writing/create_writing.html', title='Update', form=form, legend='Update')


""" Delete the writing paper and commit to the database """


@writing.route("/writing/<int:writing_id>/delete", methods=['POST'])
@login_required
def delete_writing(writing_id):
    writing = Writingpaper.query.get_or_404(writing_id)
    if writing.wcreator != current_user:
        abort(403)
    db.session.delete(writing)
    db.session.commit()
    flash('Your Writing Paper has been deleted!!', 'success')
    return redirect(url_for('writing.write'))

# Provide the writing paper result


@writing.route("/writing/<int:writing_id>/result", methods=['POST', 'GET'])
@login_required
def result(writing_id):

    writing_answer = Writingpaperanswer.query.get_or_404(writing_id)
    para = check_spellings(writing_answer.task)

    if writing_answer.wcandidate != current_user:
        abort(403)
    else:
        pic_file = url_for(
            'static', filename='profile_pics/' + current_user.image_file)
        return render_template('writing/writing_answer.html', title='Update', legend='Update', writing_answer=writing_answer, pic_file=pic_file, para=para)

# Provide improvement plan to the specific candidate


@writing.route('/writing/<int:writing_id>/summary', methods=['POST', 'GET'])
def summary(writing_id):
    writing = Writingpaperanswer.query.get_or_404(writing_id)
    quiz_creates = Create_quiz.query.filter(
        Create_quiz.index_no == 1).all()
    activitySuggestion(1, writing.grammar)
    activitySuggestion(2, writing.cohesion)
    for quiz_create in quiz_creates:
        if quiz_create.qcreatequiz.toq == 'writing':
            quiz_creates = Create_quiz.query.filter(
                Create_quiz.index_no == 1).all()

    return render_template('writing/writing_quiz.html', writing=writing, quiz_creates=quiz_creates)


def activitySuggestion(section, marks):
    test_data = np.array([section, marks]).reshape(1, 2)
    activity = activityModel.predict(test_data)[0]
    print(activity)
    return activity
