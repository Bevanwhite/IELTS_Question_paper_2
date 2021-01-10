from flask import render_template, Blueprint, flash, redirect, url_for, request, jsonify, abort
from flask_login import login_required
from flaskblog.speaking.forms import SpeakForm, RecodingForm
from flaskblog.speaking.utils import Someaudio, record
from flaskblog.writing.utils import get_grammar_result, get_cohesion_result
from flaskblog import db
from flaskblog.models import Speaking, Speakinganswer, Speakinganswersaved, Speakingquestion, Create_quiz
from flask_login import current_user
import os
import sqlite3
from datetime import datetime, timedelta
import joblib

speaking = Blueprint('speaking', __name__)


@speaking.route("/speaking")
def speak():
    speakings = Speaking.query.all()
    return render_template('speaking/speaking.html', speakings=speakings)


@speaking.route("/speaking/new", methods=['GET', 'POST'])
@login_required
def new_speaking():
    if current_user.is_authenticated and current_user.is_admin == 0:
        abort(403)
    form = SpeakForm()
    if form.validate_on_submit():
        que_01 = Someaudio(form.question_01.data)
        que_02 = Someaudio(form.question_02.data)
        que_03 = Someaudio(form.question_03.data)
        que_04 = Someaudio(form.question_04.data)
        que_05 = Someaudio(form.question_05.data)
        speak = Speaking(title=form.title.data, question_01=que_01, question_02=que_02,
                         question_03=que_03, question_04=que_04, question_05=que_05, vspeak=current_user)
        speak01 = Speakingquestion(title=form.title.data, question_01=form.question_01.data, question_02=form.question_02.data,
                                   question_03=form.question_03.data, question_04=form.question_04.data, question_05=form.question_05.data, speakquestion=current_user)
        db.session.add(speak01)
        db.session.add(speak)
        db.session.commit()
        flash('Your Speaking Paper has been Created!', 'success')
        return redirect(url_for('speaking.speak'))
    return render_template('speaking/create_speak.html', title='Speaking Paper', form=form, legend='Speaking Paper')


@speaking.route("/speaking/<int:speaking_id>", methods=['GET', 'POST'])
@login_required
def show_speaking(speaking_id):
    speaking = Speaking.query.get_or_404(speaking_id)
    form = RecodingForm()
    answer_speak = Speakinganswer.query.all()
    if form.is_submitted():
        speaks = Speakinganswer.query.all()
        speaking = Speaking.query.get_or_404(speaking_id)
        print(speaks)
        if len(speaks) == 0:
            print("1")
            print('list is empty')
            speak = Speakinganswer(
                id=1, pid=speaking_id, date_posted=datetime.now(), speakanswer=current_user)
            db.session.add(speak)
            db.session.commit()
            if form.record1.data:
                file_name1 = record(20)
                print(file_name1)
                if (file_name1 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == 1, Speakinganswer.user_id ==
                                                            current_user.id, Speakinganswer.pid == speaking_id).update({Speakinganswer.answer01: file_name1, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')

            elif form.record2.data:
                file_name2 = record(20)
                if (file_name2 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == 1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer02: file_name2, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record3.data:
                file_name3 = record(20)
                if (file_name3 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == 1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer03: file_name3, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record4.data:
                file_name4 = record(20)
                if (file_name4 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == 1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer04: file_name4, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record5.data:
                file_name5 = record(20)
                if (file_name5 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == 1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer05: file_name5, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
        elif(speaks[-1].user_id != current_user.id):
            print("2")
            speak = Speakinganswer(
                id=speaks[-1].id+1, pid=speaking_id, date_posted=datetime.now(), speakanswer=current_user)
            print(speak)
            db.session.add(speak)
            db.session.commit()
            if form.record1.data:
                file_name1 = record(20)
                print(file_name1)
                if (file_name1 != 'none'):
                    print(speaks[-1].id+1)
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id+1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer01: file_name1, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record2.data:
                file_name2 = record(20)
                if (file_name2 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id+1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer02: file_name2, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record3.data:
                file_name3 = record(20)
                if (file_name3 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id+1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer03: file_name3, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record4.data:
                file_name4 = record(20)
                if (file_name4 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id+1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer04: file_name4, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record5.data:
                file_name5 = record(20)
                if (file_name5 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id+1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer05: file_name5, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
        elif (datetime.now() - speaks[-1].date_posted > timedelta(seconds=900)) and (speaks[-1].user_id == current_user.id):
            print("3")
            print(speaks[-1].id)
            speak = Speakinganswer(
                id=speaks[-1].id+1, pid=speaking_id, date_posted=datetime.now(), speakanswer=current_user)
            db.session.add(speak)
            db.session.commit()
            if form.record1.data:
                file_name1 = record(20)
                print(file_name1)
                if (file_name1 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id+1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer01: file_name1, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record2.data:
                file_name2 = record(20)
                if (file_name2 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id+1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer02: file_name2, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record3.data:
                file_name3 = record(20)
                if (file_name3 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id+1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer03: file_name3, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record4.data:
                file_name4 = record(20)
                if (file_name4 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id+1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer04: file_name4, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record5.data:
                file_name5 = record(20)
                if (file_name5 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id+1, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer05: file_name5, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
        elif (datetime.now() - speaks[-1].date_posted <= timedelta(seconds=900)) and (speaks[-1].user_id == current_user.id):
            print("4")
            if form.record1.data:
                file_name1 = record(20)
                print(file_name1)
                if (file_name1 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer01: file_name1, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record2.data:
                file_name2 = record(20)
                if (file_name2 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer02: file_name2, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record3.data:
                file_name3 = record(20)
                if (file_name3 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer03: file_name3, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record4.data:
                file_name4 = record(20)
                if (file_name4 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer04: file_name4, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
            elif form.record5.data:
                file_name5 = record(20)
                if (file_name5 != 'none'):
                    db.session.query(Speakinganswer).filter(Speakinganswer.id == speaks[-1].id, Speakinganswer.user_id == current_user.id, Speakinganswer.pid == speaking_id
                                                            ).update({Speakinganswer.answer05: file_name5, Speakinganswer.date_posted: datetime.now()}, synchronize_session=False)
                    db.session.commit()
                    flash(
                        'Your Speaking answer has been Subbmited to the Database!', 'success')
        speaks = Speakinganswer.query.all()
        answer_speak = Speakinganswer.query.all()
        if form.submit.data:
            if speaks[-1].answer01 != None and speaks[-1].answer02 != None and speaks[-1].answer03 != None and speaks[-1].answer04 != None and speaks[-1].answer05 != None:
                print(speaks[-1].answer01)
                grammar_01 = get_grammar_result(speaks[-1].answer01)
                cohesion_01 = get_cohesion_result(speaks[-1].answer01)
                grammar_02 = get_grammar_result(speaks[-1].answer02)
                cohesion_02 = get_cohesion_result(speaks[-1].answer02)
                grammar_03 = get_grammar_result(speaks[-1].answer03)
                cohesion_03 = get_cohesion_result(speaks[-1].answer03)
                grammar_04 = get_grammar_result(speaks[-1].answer04)
                cohesion_04 = get_cohesion_result(speaks[-1].answer04)
                grammar_05 = get_grammar_result(speaks[-1].answer05)
                cohesion_05 = get_cohesion_result(speaks[-1].answer05)
                speaksaved = Speakinganswersaved(
                    pid=speaking_id,
                    answer01=speaks[-1].answer01, cohesion_01=float(cohesion_01), grammar_01=float(grammar_01),
                    answer02=speaks[-1].answer02, cohesion_02=float(cohesion_02), grammar_02=float(grammar_02),
                    answer03=speaks[-1].answer03, cohesion_03=float(cohesion_03), grammar_03=float(grammar_03),
                    answer04=speaks[-1].answer04, cohesion_04=float(cohesion_04), grammar_04=float(grammar_04),
                    answer05=speaks[-1].answer05, cohesion_05=float(cohesion_05), grammar_05=float(grammar_05),
                    date_posted=datetime.now(), speakinganswersaved=current_user)
                db.session.add(speaksaved)
                db.session.commit()
                flash(
                    'Your Speaking Paper has been Subbmited to the Database!', 'success')
                return redirect(url_for('speaking.speak'))
            else:
                flash(
                    'please submit all five answers and try to save the paper', 'danger')
        return render_template('speaking/speaking_paper.html',  speaking=speaking, form=form, speaks=speaks, answer_speak=answer_speak)
    return render_template('speaking/speaking_paper.html',  speaking=speaking, form=form, answer_speak=answer_speak)


@speaking.route("/speaking/<int:speaking_qid>/result/<int:speaking_aid>", methods=['POST', 'GET'])
@login_required
def result(speaking_qid, speaking_aid):
    speaking_q = Speakingquestion.query.get_or_404(speaking_qid)
    speaking_a = Speakinganswersaved.query.get_or_404(speaking_aid)
    grammar = (speaking_a.grammar_01 + speaking_a.grammar_02 +
               speaking_a.grammar_03 + speaking_a.grammar_04 + speaking_a.grammar_05)/5
    cohesion = (speaking_a.cohesion_01 + speaking_a.cohesion_02 +
                speaking_a.cohesion_03 + speaking_a.cohesion_04 + speaking_a.cohesion_05)/5
    print(grammar)
    print(cohesion)
    print(speaking_a)
    if speaking_a.speakinganswersaved != current_user:
        abort(403)
    else:
        spic_file = url_for(
            'static', filename='profile_pics/' + current_user.image_file)
        return render_template('speaking/speaking_anwser.html', speaking_q=speaking_q, speaking_a=speaking_a, spic_file=spic_file,  grammar=grammar, cohesion=cohesion)


@speaking.route("/speaking/<int:speaking_qid>/summary/<int:speaking_aid>", methods=['POST', 'GET'])
def summary(speaking_qid, speaking_aid):
    speaking_q = Speakingquestion.query.get_or_404(speaking_qid)
    speaking_a = Speakinganswersaved.query.get_or_404(speaking_aid)
    quiz_creates = Create_quiz.query.filter(Create_quiz.index_no == 1).all()
    grammar = (speaking_a.grammar_01 + speaking_a.grammar_02 +
               speaking_a.grammar_03 + speaking_a.grammar_04 + speaking_a.grammar_05)/5
    cohesion = (speaking_a.cohesion_01 + speaking_a.cohesion_02 +
                speaking_a.cohesion_03 + speaking_a.cohesion_04 + speaking_a.cohesion_05)/5
    print(grammar)
    print(cohesion)
    for quiz_create in quiz_creates:
        if quiz_create.qcreatequiz.toq == 'speaking':
            quiz_creates = Create_quiz.query.filter(
                Create_quiz.index_no == 1).all()

    return render_template('speaking/speaking_quiz.html', speaking_q=speaking_q,
                           speaking_a=speaking_a, quiz_creates=quiz_creates, grammar=grammar, cohesion=cohesion)


def result_machinelearning(task):

    grammerAvg = 24
    coheshionAvg = 30

    test_data = [[grammerAvg, coheshionAvg]]
    model = joblib.load('improvePlan.sav')
    category = model.predict(test_data)

    print(category)

    return render_template('speaking/result_machinelearning.html', category=category)
