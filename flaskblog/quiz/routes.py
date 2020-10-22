from flask import render_template, Blueprint, flash, url_for, redirect, request, abort
from flask_login import login_user, login_required, current_user
from flaskblog import db
from flaskblog.models import Quiz, Quiz_check, Quiz_radio, Quiz_short
from flaskblog.quiz.forms import QuizCreationForm
from datetime import datetime

quiz = Blueprint('quiz', __name__)


@quiz.route("/quiz/writing")
def quiz_write():
    #quiz = Quiz.query.all()
    quizs = Quiz.query.filter(Quiz.toq == 'writing').all()
    return render_template('quiz/quiz.html', quizs=quizs)


@quiz.route("/quiz/reading")
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


@quiz.route("/quiz/<int:writing_id>/writing")
def quiz_writing(writing_id):
    quiz = Quiz.query.get_or_404(writing_id)
    return render_template('quiz/quiz_writing.html', quiz=quiz)


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
