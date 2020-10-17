from flask import render_template, Blueprint, flash, redirect, url_for, request, jsonify, abort
from flask_login import login_required
from flaskblog.speaking.forms import SpeakForm, RecodingForm
from flaskblog.speaking.utils import Someaudio, record
from flaskblog.writing.utils import get_grammar_result, get_cohesion_result
from flaskblog import db
from flaskblog.models import Speaking, Speakinganswer, Speakinganswersaved, Speakingquestion
from flask_login import current_user
import speech_recognition as sr
import os
import sqlite3
from datetime import datetime, timedelta
import mysql.connector


speaking = Blueprint('speaking', __name__)


@speaking.route("/speaking")
def speak():
    speakings = Speaking.query.all()
    return render_template('speaking.html', speakings=speakings)


@speaking.route("/speaking/new", methods=['GET', 'POST'])
@login_required
def new_speaking():
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
    return render_template('create_speak.html', title='Speaking Paper', form=form, legend='Speaking Paper')


@speaking.route("/speaking/<int:speaking_id>", methods=['GET', 'POST'])
@login_required
def show_speaking(speaking_id):
    speaking = Speaking.query.get_or_404(speaking_id)
    form = RecodingForm()
    speakanswer = Speakinganswer.query.order_by(
        Speakinganswer.date_posted.desc()).first()
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
            conn = mysql.connector.connect(
                host="localhost", user="username", password="password", database="jeffery")
            c = conn.cursor()
            if form.record1.data:
                file_name1 = record(5)
                print(file_name1)
                if (file_name1 != 'none'):
                    sql = """UPDATE speakinganswer SET answer01 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name1, 1, speaking_id,
                           current_user.id, datetime.now())
                    c.execute(sql, val)
                    conn.commit()
            elif form.record2.data:
                file_name2 = record(5)
                if (file_name2 != 'none'):
                    sql = """UPDATE speakinganswer SET answer02 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name2, datetime.now(), 1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record3.data:
                file_name3 = record(5)
                if (file_name3 != 'none'):
                    sql = """UPDATE speakinganswer SET answer03 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name3, datetime.now(), 1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record4.data:
                file_name4 = record(5)
                if (file_name4 != 'none'):
                    sql = """UPDATE speakinganswer SET answer04 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name4, datetime.now(), 1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record5.data:
                file_name5 = record(5)
                if (file_name5 != 'none'):
                    sql = """UPDATE speakinganswer SET answer05 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name5, datetime.now(), 1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            conn.close()
        elif(speaks[-1].user_id != current_user.id):
            print("2")
            speak = Speakinganswer(
                id=speaks[-1].id+1, pid=speaking_id, date_posted=datetime.now(), speakanswer=current_user)
            print(speak)
            db.session.add(speak)
            db.session.commit()
            conn = mysql.connector.connect(
                host="localhost", user="username", password="password", database="jeffery")
            c = conn.cursor()
            if form.record1.data:
                file_name1 = record(5)
                print(file_name1)
                if (file_name1 != 'none'):
                    print(speaks[-1].id+1)
                    sql = """UPDATE speakinganswer SET answer01 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name1, datetime.now(), speaks[-1].id+1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record2.data:
                file_name2 = record(5)
                if (file_name2 != 'none'):
                    sql = """UPDATE speakinganswer SET answer02 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name2, datetime.now(), speaks[-1].id+1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record3.data:
                file_name3 = record(5)
                if (file_name3 != 'none'):
                    sql = """UPDATE speakinganswer SET answer03 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name3, datetime.now(), speaks[-1].id+1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record4.data:
                file_name4 = record(5)
                if (file_name4 != 'none'):
                    sql = """UPDATE speakinganswer SET answer04 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name4, datetime.now(), speaks[-1].id+1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record5.data:
                file_name5 = record(5)
                if (file_name5 != 'none'):
                    sql = """UPDATE speakinganswer SET answer05 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name5, datetime.now(), speaks[-1].id+1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            conn.close()
        elif (datetime.now() - speaks[-1].date_posted > timedelta(seconds=900)) and (speaks[-1].user_id == current_user.id):
            print("3")
            print(speaks[-1].id)
            speak = Speakinganswer(
                id=speaks[-1].id+1, pid=speaking_id, date_posted=datetime.now(), speakanswer=current_user)
            db.session.add(speak)
            db.session.commit()
            conn = mysql.connector.connect(
                host="localhost", user="username", password="password", database="jeffery")
            c = conn.cursor()
            if form.record1.data:
                file_name1 = record(5)
                print(file_name1)
                if (file_name1 != 'none'):
                    sql = """UPDATE speakinganswer SET answer01 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name1, datetime.now(), speaks[-1].id+1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record2.data:
                file_name2 = record(5)
                if (file_name2 != 'none'):
                    sql = """UPDATE speakinganswer SET answer02 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name2, datetime.now(), speaks[-1].id+1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record3.data:
                file_name3 = record(5)
                if (file_name3 != 'none'):
                    sql = """UPDATE speakinganswer SET answer03 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name3, datetime.now(), speaks[-1].id+1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record4.data:
                file_name4 = record(5)
                if (file_name4 != 'none'):
                    sql = """UPDATE speakinganswer SET answer04 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name4, datetime.now(), speaks[-1].id+1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record5.data:
                file_name5 = record(5)
                if (file_name5 != 'none'):
                    sql = """UPDATE speakinganswer SET answer05 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name5, datetime.now(), speaks[-1].id+1,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            conn.close()
        elif (datetime.now() - speaks[-1].date_posted <= timedelta(seconds=900)) and (speaks[-1].user_id == current_user.id):
            print("4")
            conn = mysql.connector.connect(
                host="localhost", user="username", password="password", database="jeffery")
            c = conn.cursor()
            if form.record1.data:
                file_name1 = record(5)
                print(file_name1)
                if (file_name1 != 'none'):
                    sql = """UPDATE speakinganswer SET answer01 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name1, datetime.now(), speaks[-1].id,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record2.data:
                file_name2 = record(5)
                if (file_name2 != 'none'):
                    sql = """UPDATE speakinganswer SET answer02 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name2, datetime.now(), speaks[-1].id,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record3.data:
                file_name3 = record(5)
                if (file_name3 != 'none'):
                    sql = """UPDATE speakinganswer SET answer03 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name3, datetime.now(), speaks[-1].id,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record4.data:
                file_name4 = record(5)
                if (file_name4 != 'none'):
                    sql = """UPDATE speakinganswer SET answer04 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name4, datetime.now(), speaks[-1].id,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            elif form.record5.data:
                file_name5 = record(50)
                if (file_name5 != 'none'):
                    sql = """UPDATE speakinganswer SET answer05 = %s, date_posted = %s 
                    WHERE id = %s AND pid = %s AND user_id = %s"""
                    val = (file_name5, datetime.now(), speaks[-1].id,
                           speaking_id, current_user.id)
                    c.execute(sql, val)
                    conn.commit()
            conn.close()
        speaks = Speakinganswer.query.all()
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
                    answer01=speaks[-1].answer01, cohesion_01=cohesion_01, grammar_01=grammar_01,
                    answer02=speaks[-1].answer02, cohesion_02=cohesion_02, grammar_02=grammar_02,
                    answer03=speaks[-1].answer03, cohesion_03=cohesion_03, grammar_03=grammar_03,
                    answer04=speaks[-1].answer04, cohesion_04=cohesion_04, grammar_04=grammar_04,
                    answer05=speaks[-1].answer05, cohesion_05=cohesion_05, grammar_05=grammar_05,
                    date_posted=datetime.now(), speakinganswersaved=current_user)
                db.session.add(speaksaved)
                db.session.commit()
                return redirect(url_for('speaking.speak'))
            else:
                flash(
                    'please submit all five answers and try to save the paper', 'danger')
        return render_template('speaking_paper.html',  speaking=speaking, form=form, speaks=speaks)
    return render_template('speaking_paper.html',  speaking=speaking, form=form)


@speaking.route("/speaking/<int:speaking_id>/result", methods=['POST', 'GET'])
@login_required
def result(speaking_id):
    speaking_answer = Speakingquestion.query.get_or_404(speaking_id)
    speaking_ans = Speakinganswersaved.query.get_or_404(speaking_id)
    print(speaking_answer)
    if speaking_answer.speakquestion != current_user:
        abort(403)
    else:
        spic_file = url_for(
            'static', filename='profile_pics/' + current_user.image_file)
        return render_template('speaking_anwser.html', title='Update',
                               legend='Update', speaking_answer=speaking_answer, spic_file=spic_file, speaking_ans=speaking_ans)
