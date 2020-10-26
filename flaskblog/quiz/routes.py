from flask import render_template, Blueprint, flash, url_for, redirect, request, abort
from flask_login import login_user, login_required, current_user
from flaskblog import db
from flaskblog.models import Quiz, Quiz_check, Quiz_radio, Quiz_short, Quiz_answers_type
from flaskblog.quiz.forms import QuizCreationForm, QuestionForm, QuestionChecklistForm
from datetime import datetime

quiz = Blueprint('quiz', __name__)


@quiz.route("/quiz/write")
def quiz_write():
    #quiz = Quiz.query.all()
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


@quiz.route("/quiz/<int:quiz_id>/radio")
def quiz_radio(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template('quiz/radio.html', quiz=quiz)


@quiz.route("/quiz/<int:quiz_id>/checklist")
def quiz_checklist(quiz_id):
    form = QuestionChecklistForm()
    legend = "Creating Checklist Question"
    quiz = Quiz.query.get_or_404(quiz_id)
    form.correct_answer.choices = [(x.id, x.texts)
                                   for x in Quiz_answers_type.query.all()]

    if form.validate_on_submit():
        pass

    return render_template('quiz/checklist.html', quiz=quiz, form=form, legend=legend)


@quiz.route("/quiz/<int:quiz_id>/short")
def quiz_short(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template('quiz/short.html', quiz=quiz)
