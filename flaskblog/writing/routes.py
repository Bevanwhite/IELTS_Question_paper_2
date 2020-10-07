from flask import render_template, Blueprint, flash, url_for, redirect, request, abort
from flask_login import login_user, login_required, current_user
from flaskblog import db
from flaskblog.models import Writingpaper, Writingpaperanswer, Writingimprovementplan
from flaskblog.writing.forms import WritingpaperForm, WritingUpdateForm, WritingpaperoneForm
from flaskblog.writing.utils import paper_picture, get_grammar_result, get_cohesion_result
from datetime import datetime


writing = Blueprint('writing', __name__)


@writing.route("/writing")
def write():
    page = request.args.get('page', 1, type=int)
    writingpapers = Writingpaper.query.paginate(page=page, per_page=6)
    return render_template('writing.html', writingpapers=writingpapers)


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
    return render_template('create_writing.html', title='Writing Paper', form=form, legend='Writing Paper')


@writing.route("/writing/<int:writing_id>", methods=['GET', 'POST'])
@login_required
def show_writing(writing_id):
    writingpaper = Writingpaper.query.get_or_404(writing_id)
    form1 = WritingpaperoneForm()
    if form1.validate_on_submit():
        grammar_01 = get_grammar_result(form1.task01_answer.data)
        cohesion_01 = get_cohesion_result(form1.task01_answer.data)
        writing = Writingpaperanswer(pid=writing_id, task=form1.task01_answer.data,
                                     type="type1", grammar=grammar_01, cohesion=cohesion_01, wcandidate=current_user)
        db.session.add(writing)
        db.session.commit()
        flash(
            'Your Question 01 Answer has been saved in the database successfully', 'success')
        return redirect(url_for('writing.show_writing', writing_id=writing_id))
    return render_template('writing_paper.html',  writingpaper=writingpaper, form1=form1)


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
    return render_template('create_writing.html', title='Update', form=form, legend='Update')


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


@writing.route("/writing/<int:writing_result_id>/result", methods=['POST', 'GET'])
@login_required
def result(writing_result_id):
    writing_answer = Writingpaperanswer.query.get_or_404(writing_result_id)
    if writing_answer.wcandidate != current_user:
        abort(403)
    else:
        pic_file = url_for(
            'static', filename='profile_pics/' + current_user.image_file)
        return render_template('writing_answer.html', title='Update', legend='Update', writing_answer=writing_answer, pic_file=pic_file)


@writing.route('/writing/<int:writing_result_id>/summary', methods=['POST', 'GET'])
def summary(writing_result_id):
    writing = Writingpaperanswer.query.get_or_404(writing_result_id)

    grammar1 = writing.grammar
    cohesion1 = writing.cohesion
    sp = 'stage 0'
    pln_no = 0
    feedback = 'feedback 1'

    if -1 < grammar1 < 11 or -1 < cohesion1 < 11:
        pln_no = 1
        feedback = 'feedback 2'
        sp = 'stage 1'
    elif 0 < grammar1 < 11 or 10 < cohesion1 < 21:
        pln_no = 2
        feedback = 'no feedback 3'
        sp = 'stage 2'
    elif 0 < grammar1 < 11 or 20 < cohesion1 < 26:
        pln_no = 3
        feedback = 'Observed difficulty in grammar. Work hard for improvement. Keep up the good work with the improvement plan.'
        sp = 'stage 3'
    elif 10 < grammar1 < 21 or 0 < cohesion1 < 11:
        pln_no = 4
        feedback = 'no feedback 5'
        sp = 'stage 4'
    elif 10 < grammar1 < 21 or 10 < cohesion1 < 21:
        pln_no = 5
        feedback = 'no feedback 6'
        sp = 'stage 5'
    elif 10 < grammar1 < 21 or 20 < cohesion1 < 26:
        pln_no = 6
        feedback = 'no feedback 7'
        sp = 'stage 6'
    elif 20 < grammar1 < 26 or 0 < cohesion1 < 11:
        pln_no = 7
        feedback = 'no feedback 8'
        sp = 'stage 7'
    elif 20 < grammar1 < 26 or 10 < cohesion1 < 21:
        pln_no = 8
        feedback = 'no feedback 9'
        sp = 'stage 8'
    elif 20 < grammar1 < 26 or 20 < cohesion1 < 26:
        pln_no = 9
        feedback = 'no feedback 10'
        sp = 'stage 9'

    writing = Writingimprovementplan(study_plan=sp, study_plan_no=pln_no,
                                     feedback=feedback, date_posted=datetime.now(), user_id=current_user.id)
    db.session.add(writing)
    db.session.commit()
    return render_template('writing_home.html', writing=writing)


@writing.route("/writing/plan_g11")
def plan_g11():
    return render_template('writing_g1.6.html')


@writing.route("/writing/plan_g12")
def plan_g12():
    return render_template('writing_g1.2.html')


@writing.route("/writing/plan1_5")
def plan1_5():
    return render_template('plan1.5.html')


@writing.route("/writing/plan2_1")
def plan2_1():
    return render_template('plan2.1.html')


@writing.route("/writing/plan2_2")
def plan2_2():
    return render_template('plan2.2.html')


@writing.route("/writing/plan2_3")
def plan2_3():
    return render_template('plan2.3.html')
