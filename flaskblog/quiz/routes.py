from flask import render_template, Blueprint, flash, url_for, redirect, request, abort
from flask_login import login_user, login_required, current_user
from flaskblog import db
from flaskblog.models import Quiz, Quiz_check, Quiz_radio, Quiz_short, Quiz_answers_type
from flaskblog.quiz.forms import QuizCreationForm, QuestionForm, QuestionChecklistForm, QuestionRadioForm, QuestionShortForm
from datetime import datetime

quiz = Blueprint('quiz', __name__)


@quiz.route("/quiz/write")
def quiz_write():
    # quiz = Quiz.query.all()
    quizs = Quiz.query.filter(Quiz.toq == 'writing').all()
    return render_template('quiz/write.html', quizs=quizs)


@quiz.route("/quiz/read")
def quiz_read():
    quizs = Quiz.query.filter(Quiz.toq == 'reading').all()
    return render_template('quiz/read.html', quizs=quizs)


@quiz.route("/quiz/listen")
def quiz_listen():
    quizs = Quiz.query.filter(Quiz.toq == 'listening').all()
    return render_template('quiz/listen.html', quizs=quizs)


@quiz.route("/quiz/speak")
def quiz_speak():
    quizs = Quiz.query.filter(Quiz.toq == 'speaking').all()
    return render_template('quiz/speak.html', quizs=quizs)


@quiz.route("/quiz/<int:quiz_id>")
def show_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    quiz_checks = Quiz_check.query.filter(Quiz_check.quiz_id == quiz_id).all()
    quiz_radios = Quiz_radio.query.filter(Quiz_radio.quiz_id == quiz_id).all()
    quiz_shorts = Quiz_short.query.filter(Quiz_short.quiz_id == quiz_id).all()

    return render_template('quiz/quiz.html', quiz=quiz)


@quiz.route("/quiz/new", methods=['GET', 'POST'])
@login_required
def new_quiz():
    form = QuizCreationForm()
    legend = "Creating Questions"
    if form.validate_on_submit():
        quiz = Quiz(name=form.name.data, noq=form.noq.data, toq=form.toq.data,
                    quiz=current_user)
        db.session.add(quiz)
        db.session.commit()
        flash('Your paper has created successfully !!!', 'success')
        return redirect(url_for('quiz.quiz_write'))
    return render_template('quiz/create_quiz.html', legend=legend, form=form)


@quiz.route("/quiz/<int:quiz_id>/create_quiz", methods=['GET', 'POST'])
def quiz_question(quiz_id):
    form = QuestionForm()
    quiz = Quiz.query.get_or_404(quiz_id)
    legend = "Create Quiz Category"
    if form.validate_on_submit():
        if form.toq.data == 'radio':
            return redirect(url_for('quiz.quiz_radio', quiz_id=quiz.id))

        elif form.toq.data == 'checklist':
            return redirect(url_for('quiz.quiz_checklist', quiz_id=quiz.id))

        elif form.toq.data == 'short':
            return redirect(url_for('quiz.quiz_short', quiz_id=quiz.id))

    return render_template('quiz/create_question.html', form=form, legend=legend)


@quiz.route("/quiz/<int:quiz_id>/radio", methods=['GET', 'POST'])
def quiz_radio(quiz_id):
    form = QuestionRadioForm()
    quiz = Quiz.query.get_or_404(quiz_id)
    legend = "Creating Radio Button Question"
    form.correct_answer.choices = [(x.id, x.texts)
                                   for x in Quiz_answers_type.query.all()]
    if form.validate_on_submit():
        quiz_radio = Quiz_radio(title=form.title.data, question=form.question.data, answer01=form.answer01.data,
                                answer02=form.answer02.data, answer03=form.answer03.data,
                                answer04=form.answer04.data, correct_answer=form.correct_answer.data,
                                quiz_id=quiz_id, user_id=current_user.id)
        db.session.add(quiz_radio)
        db.session.commit()
        flash('Your Radio Question has been Created!', 'success')
        return redirect(url_for('quiz.show_quiz', quiz_id=quiz_id))
    return render_template('quiz/radio.html', quiz=quiz, form=form, legend=legend)


@quiz.route("/quiz/<int:quiz_id>/checklist", methods=['GET', 'POST'])
def quiz_checklist(quiz_id):
    form = QuestionChecklistForm()
    legend = "Creating Checklist Question"
    quiz = Quiz.query.get_or_404(quiz_id)
    form.correct_answer.choices = [(x.id, x.texts)
                                   for x in Quiz_answers_type.query.all()]
    if form.validate_on_submit():
        list = '|'.join([str(i) for i in form.correct_answer.data])
        quiz_check = Quiz_check(title=form.title.data, question=form.question.data, answer01=form.answer01.data,
                                answer02=form.answer02.data, answer03=form.answer03.data,
                                answer04=form.answer04.data, correct_answer=list,
                                quiz_id=quiz_id, user_id=current_user.id)
        db.session.add(quiz_check)
        db.session.commit()
        flash('Your Checklist Question has been Created!', 'success')
        return redirect(url_for('quiz.show_quiz', quiz_id=quiz_id))
    return render_template('quiz/checklist.html', quiz=quiz, form=form, legend=legend)


@quiz.route("/quiz/<int:quiz_id>/short", methods=['GET', 'POST'])
def quiz_short(quiz_id):
    form = QuestionShortForm()
    legend = "Creating Short Answer Question"
    quiz = Quiz.query.get_or_404(quiz_id)
    if form.validate_on_submit():
        quiz_short = Quiz_short(
            title=form.title.data, question=form.question.data, correct_answer=form.correct_answer.data,
            quiz_id=quiz_id, user_id=current_user.id)
        db.session.add(quiz_short)
        db.session.commit()
        flash('Your Checklist Question has been Created!', 'success')
        return redirect(url_for('quiz.show_quiz', quiz_id=quiz_id))
    return render_template('quiz/short.html', quiz=quiz, form=form, legend=legend)
