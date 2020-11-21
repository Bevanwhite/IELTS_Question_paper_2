from flask import render_template, Blueprint, flash, url_for, redirect, request, abort
from flask_login import login_user, login_required, current_user
from flaskblog import db
from flaskblog.models import Quiz, Create_quiz, Quiz_answers_type
from flaskblog.quiz.forms import QuizCreationForm, QuestionForm, QuestionChecklistForm, QuestionRadioForm
from flaskblog.quiz.forms import QuestionShortForm, ChecklistForm, RadioForm, ShortForm, PreviewForm
from flaskblog.quiz.forms import UpdateQuestionChecklistForm, UpdateQuestionShortForm, UpdateQuestionRadioForm
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
    quiz_creates = Create_quiz.query.filter(
        Create_quiz.quiz_id == quiz_id).all()
    see1 = Create_quiz.query.filter(Create_quiz.quiz_id == quiz_id).count()
    print(see1)
    return render_template('quiz/quiz.html', quiz=quiz, quiz_creates=quiz_creates)


@quiz.route("/quiz/new", methods=['GET', 'POST'])
@login_required
def new_quiz():
    form = QuizCreationForm()
    legend = "Creating Questions"
    if form.validate_on_submit():
        quiz = Quiz(name=form.name.data, toq=form.toq.data,
                    gandco=form.gandco.data, userbased=form.userbased.data, quiz=current_user)
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
        if form.toq.data == "radio":
            return redirect(url_for('quiz.quiz_radio', quiz_id=quiz.id))

        elif form.toq.data == "checklist":
            return redirect(url_for('quiz.quiz_checklist', quiz_id=quiz.id))

        elif form.toq.data == "short":
            return redirect(url_for('quiz.quiz_short', quiz_id=quiz.id))
    return render_template('quiz/create_question.html', form=form, legend=legend)


@quiz.route("/quiz/<int:quiz_id>/radio", methods=['GET', 'POST'])
def quiz_radio(quiz_id):
    form = QuestionRadioForm(quiz_id=quiz_id)
    quiz = Quiz.query.get_or_404(quiz_id)
    legend = "Creating Radio Button Question"
    form.correct_answer.choices = [(x.id, x.texts)
                                   for x in Quiz_answers_type.query.all()]
    if form.validate_on_submit():
        create_quiz = Create_quiz(title=form.title.data, question=form.question.data, toq="radio", answer01=form.answer01.data,
                                  answer02=form.answer02.data, answer03=form.answer03.data,
                                  answer04=form.answer04.data, correct_answer=form.correct_answer.data, index_no=form.index_no.data,
                                  quiz_id=form.quiz_id.data, user_id=current_user.id)
        db.session.add(create_quiz)
        db.session.commit()
        flash('Your Radio Question has been Created!', 'success')
        return redirect(url_for('quiz.show_quiz', quiz_id=quiz_id))
    return render_template('quiz/create_radio.html', quiz=quiz, form=form, legend=legend)


@quiz.route("/quiz/<int:quiz_id>/checklist", methods=['GET', 'POST'])
def quiz_checklist(quiz_id):
    form = QuestionChecklistForm(quiz_id=quiz_id)
    legend = "Creating Checklist Question"
    quiz = Quiz.query.get_or_404(quiz_id)
    form.correct_answer.choices = [(x.id, x.texts)
                                   for x in Quiz_answers_type.query.all()]
    if form.validate_on_submit():
        list = ' '.join([str(i) for i in form.correct_answer.data])
        create_quiz = Create_quiz(
            title=form.title.data, question=form.question.data, toq="checklist", answer01=form.answer01.data,
            answer02=form.answer02.data, answer03=form.answer03.data, answer04=form.answer04.data,
            correct_answer=list, index_no=form.index_no.data, quiz_id=form.quiz_id.data, user_id=current_user.id)
        db.session.add(create_quiz)
        db.session.commit()
        flash('Your Checklist Question has been Created!', 'success')
        return redirect(url_for('quiz.show_quiz', quiz_id=quiz_id))
    return render_template('quiz/create_checklist.html', quiz=quiz, form=form, legend=legend)


@quiz.route("/quiz/<int:quiz_id>/short", methods=['GET', 'POST'])
def quiz_short(quiz_id):
    form = QuestionShortForm(quiz_id=quiz_id)
    legend = "Creating Short Answer Question"
    quiz = Quiz.query.get_or_404(quiz_id)
    be = 'none'
    if form.validate_on_submit():
        create_quiz = Create_quiz(
            title=form.title.data, question=form.question.data, toq="short", answer01=be,
            answer02=be, answer03=be, answer04=be, correct_answer=form.correct_answer.data, index_no=form.index_no.data,
            quiz_id=form.quiz_id.data, user_id=current_user.id)
        db.session.add(create_quiz)
        db.session.commit()
        flash('Your Short Answer Question has been Created!', 'success')
        return redirect(url_for('quiz.show_quiz', quiz_id=quiz_id))
    return render_template('quiz/create_short.html', quiz=quiz, form=form, legend=legend)


@quiz.route("/quiz/<int:quiz_id>/radio/<int:id>", methods=['GET', 'POST'])
def quiz_radio_answer(quiz_id, id):
    quiz = Create_quiz.query.filter(
        Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == id).first()
    quizes = Create_quiz.query.filter(Create_quiz.quiz_id == quiz_id).all()

    if quiz.index_no > 0:
        pquiz = Create_quiz.query.filter(
            Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == quiz.index_no - 1).first()
        print(pquiz)
    if quiz.index_no < 40:
        nquiz = Create_quiz.query.filter(
            Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == quiz.index_no + 1).first()
        print(nquiz)

    form1 = PreviewForm()
    form = RadioForm()
    legend = "Answer the Radio Question"

    list = []
    list.append((1, quiz.answer01))
    list.append((2, quiz.answer02))
    list.append((3, quiz.answer03))
    list.append((4, quiz.answer04))
    print(type(list))
    form.correct_answer.choices = [
        (int(list[x][0]), str(list[x][1]))for x in range(4)]
    return render_template('quiz/radio.html', quiz=quiz, quizes=quizes, form=form, legend=legend, form1=form1, pquiz=pquiz, nquiz=nquiz)


@quiz.route("/quiz/<int:quiz_id>/checklist/<int:id>", methods=['GET', 'POST'])
def quiz_checklist_answer(quiz_id, id):
    quizes = Create_quiz.query.filter(Create_quiz.quiz_id == quiz_id).all()
    quiz = Create_quiz.query.filter(
        Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == id).first()

    if quiz.index_no > 0:
        pquiz = Create_quiz.query.filter(
            Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == quiz.index_no - 1).first()
        print(pquiz)
    if quiz.index_no < 40:
        nquiz = Create_quiz.query.filter(
            Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == quiz.index_no + 1).first()
        print(nquiz)
    form1 = PreviewForm()
    form = ChecklistForm()
    legend = "Answer Checklist Question"

    list = []
    list.append((1, quiz.answer01))
    list.append((2, quiz.answer02))
    list.append((3, quiz.answer03))
    list.append((4, quiz.answer04))
    print(type(list))
    form.correct_answer.choices = [
        (int(list[x][0]), str(list[x][1]))for x in range(4)]
    return render_template('quiz/checklist.html', quiz=quiz, quizes=quizes, legend=legend, form=form, form1=form1, pquiz=pquiz, nquiz=nquiz)


@quiz.route("/quiz/<int:quiz_id>/short/<int:id>", methods=['GET', 'POST'])
def quiz_short_answer(quiz_id, id):
    quiz = Create_quiz.query.filter(
        Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == id).first()
    quizes = Create_quiz.query.filter(Create_quiz.quiz_id == quiz_id).all()
    if quiz.index_no > 0:
        pquiz = Create_quiz.query.filter(
            Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == quiz.index_no - 1).first()
        print(pquiz)
    if quiz.index_no < 40:
        nquiz = Create_quiz.query.filter(
            Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == quiz.index_no + 1).first()
        print(nquiz)

    form1 = PreviewForm()
    form = ShortForm()
    legend = "Answer Short Question"

    return render_template('quiz/short.html', quiz=quiz, quizes=quizes, legend=legend, form=form, form1=form1, pquiz=pquiz, nquiz=nquiz)


@quiz.route("/quiz/<int:quiz_id>/radio/<int:id>/update", methods=['GET', 'POST'])
def update_radio(quiz_id, id):
    form = UpdateQuestionRadioForm(quiz_id=quiz_id, index_no=id)
    quiz = Quiz.query.get_or_404(quiz_id)
    legend = "Updating Radio Button Question"
    form.correct_answer.choices = [(x.id, x.texts)
                                   for x in Quiz_answers_type.query.all()]
    create_quiz = Create_quiz.query.filter(
        Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == id).first()
    if create_quiz.createquiz != current_user:
        abort(403)

    if form.validate_on_submit():
        create_quiz.title = form.title.data
        create_quiz.question = form.question.data
        create_quiz.answer01 = form.answer01.data
        create_quiz.answer02 = form.answer02.data
        create_quiz.answer03 = form.answer03.data
        create_quiz.answer04 = form.answer04.data
        create_quiz.correct_answer = form.correct_answer.data
        db.session.commit()
        flash('Your Radio Question has been Updated!', 'success')
        return redirect(url_for('quiz.show_quiz', quiz_id=quiz_id))
    elif request.method == 'GET':
        form.title.data = create_quiz.title
        form.question.data = create_quiz.question
        form.answer01.data = create_quiz.answer01
        form.answer02.data = create_quiz.answer02
        form.answer03.data = create_quiz.answer03
        form.answer04.data = create_quiz.answer04
        form.correct_answer.data = create_quiz.correct_answer
    return render_template('quiz/update_radio.html', quiz=quiz, form=form, legend=legend)


@quiz.route("/quiz/<int:quiz_id>/checklist/<int:id>/update", methods=['GET', 'POST'])
def update_checklist(quiz_id, id):
    form = UpdateQuestionChecklistForm(quiz_id=quiz_id, index_no=id)
    legend = "Updating Checklist Question"
    quiz = Quiz.query.get_or_404(quiz_id)
    create_quiz = Create_quiz.query.filter(
        Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == id).first()
    form.correct_answer.choices = [(x.id, x.texts)
                                   for x in Quiz_answers_type.query.all()]
    if create_quiz.createquiz != current_user:
        abort(403)

    if form.validate_on_submit():
        list = ' '.join([str(i) for i in form.correct_answer.data])
        create_quiz.title = form.title.data
        create_quiz.question = form.question.data
        create_quiz.answer01 = form.answer01.data
        create_quiz.answer02 = form.answer02.data
        create_quiz.answer03 = form.answer03.data
        create_quiz.answer04 = form.answer04.data
        create_quiz.correct_answer = list
        db.session.commit()
        flash('Your Checklist Question has been Updated!', 'success')
        return redirect(url_for('quiz.show_quiz', quiz_id=quiz_id))
    elif request.method == 'GET':
        car = create_quiz.correct_answer.split()
        test = [int(i) for i in car]
        form.title.data = create_quiz.title
        form.question.data = create_quiz.question
        form.answer01.data = create_quiz.answer01
        form.answer02.data = create_quiz.answer02
        form.answer03.data = create_quiz.answer03
        form.answer04.data = create_quiz.answer04
        form.correct_answer.data = test
    return render_template('quiz/update_checklist.html', quiz=quiz, form=form, legend=legend)


@quiz.route("/quiz/<int:quiz_id>/short/<int:id>/update", methods=['GET', 'POST'])
def update_short(quiz_id, id):
    form = UpdateQuestionShortForm(quiz_id=quiz_id, index_no=id)
    legend = "Updating Short Answer Question"
    quiz = Quiz.query.get_or_404(quiz_id)
    create_quiz = Create_quiz.query.filter(
        Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == id).first()
    if create_quiz.createquiz != current_user:
        abort(403)
    if create_quiz.toq != "short":
        abort(403)
    if form.validate_on_submit():
        create_quiz.title = form.title.data
        create_quiz.question = form.question.data
        create_quiz.correct_answer = form.correct_answer.data
        db.session.commit()
        flash('Your Short Answer Question has been Updated!', 'success')
        return redirect(url_for('quiz.show_quiz', quiz_id=quiz_id))
    elif request.method == 'GET':
        form.title.data = create_quiz.title
        form.question.data = create_quiz.question
        form.correct_answer.data = create_quiz.correct_answer
    return render_template('quiz/update_short.html', quiz=quiz, form=form, legend=legend)


@quiz.route("/quiz/<int:quiz_id>/radio/<int:id>/delete", methods=['GET', 'POST'])
def delete_radio(quiz_id, id):
    quiz = Create_quiz.query.filter(
        Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == id).first()
    if quiz.createquiz != current_user:
        abort(403)
    db.session.delete(quiz)
    db.session.commit()
    flash('Your Quiz Radio has been deleted!!', 'success')
    return redirect(url_for('quiz.show_quiz', quiz_id=quiz_id))


@quiz.route("/quiz/<int:quiz_id>/checklist/<int:id>/delete", methods=['GET', 'POST'])
def delete_checklist(quiz_id, id):
    quiz = Create_quiz.query.filter(
        Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == id).first()
    if quiz.createquiz != current_user:
        abort(403)
    db.session.delete(quiz)
    db.session.commit()
    flash('Your Quiz Checklist has been deleted!!', 'success')
    return redirect(url_for('quiz.show_quiz', quiz_id=quiz_id))


@quiz.route("/quiz/<int:quiz_id>/short/<int:id>/delete", methods=['GET', 'POST'])
def delete_short(quiz_id, id):
    quiz = Create_quiz.query.filter(
        Create_quiz.quiz_id == quiz_id, Create_quiz.index_no == id).first()
    if quiz.createquiz != current_user:
        abort(403)
    db.session.delete(quiz)
    db.session.commit()
    flash('Your Quiz Short has been deleted!!', 'success')
    return redirect(url_for('quiz.show_quiz', quiz_id=quiz_id))
