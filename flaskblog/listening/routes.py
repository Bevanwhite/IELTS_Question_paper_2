from flask import Flask, flash, Blueprint, render_template, request, url_for, redirect
from flask import render_template, Blueprint, flash, redirect, url_for, request, jsonify
from flask_login import login_required
from flaskblog import db
from flask_login import current_user
import os
import sqlite3
from datetime import datetime, timedelta
from flaskext.mysql import MySQL
import joblib
suggestion_model = joblib.load('Listening_activity_suggestion_up1.sav')

listening = Blueprint('listening', __name__)
app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ielts'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@listening.route("/listening")
@login_required
def listen():
    uid = current_user.id
    conn = mysql.connect()
    c = conn.cursor()
    uid = current_user.id
    q1 = "SELECT user_id FROM listening_user where user_id = %s"
    try:
        c.execute(q1, uid)
        uid_db = c.fetchone()[0]
        if uid_db:
            q1 = "SELECT study_plan FROM listening_user where user_id = %s"
            c.execute(q1, uid)
            study_plan = c.fetchone()[0]

            q2 = "SELECT progress FROM listening_user where user_id = %s"
            c.execute(q2, uid)
            progress = c.fetchone()[0]

            q3 = "SELECT weak_section FROM listening_user where user_id = %s"
            c.execute(q3, uid)
            weak_section = c.fetchone()[0]
            q4 = "SELECT study_plan_no FROM listening_user where user_id = %s"
            c.execute(q4, uid)
            study_plan_no = c.fetchone()[0]
            q5 = "SELECT pid FROM listening_user where user_id = %s"
            c.execute(q5, uid)
            pid = c.fetchone()[0]
            c.close()
            data = {'study_plan':  study_plan, 'progress': progress,
                    'weak_section': weak_section, 'study_plan_no': study_plan_no, 'pid': pid}
            return render_template('listening.html', data=data)
        else:
            return render_template("listening_test_paper1.html")
    except Exception as e:
        return render_template("listening_test_paper1.html")


@listening.route("/section1", methods=['POST'])
def section1():
    if request.method == "POST":
        q01 = request.form['q01']
        q02 = request.form['q02']
        q03 = request.form['q03']
        q04 = request.form['q04']
        q05 = request.form['q05']
        q06 = request.form['q06']
        q07 = request.form['q07']
        q08 = request.form['q08']
        q09 = request.form['q09']
        q10 = request.form['q10']

        conn = mysql.connect()
        c = conn.cursor()
        drop = "DROP TABLE IF EXISTS  user_answer"
        c.execute(drop)
        create_table = "CREATE TABLE user_answer (id INT(2) UNSIGNED AUTO_INCREMENT PRIMARY KEY,question VARCHAR(30) NOT NULL,answer VARCHAR(30))"
        c.execute(create_table)
        query = "INSERT INTO user_answer(question,answer) VALUES (%s,%s)"
        val = [("1", q01), ("2", q02), ("3", q03), ("4", q04), ("5", q05),
               ("6", q06), ("7", q07), ("8", q08), ("9", q09), ("10", q10)]
        c.executemany(query, val)
        conn.commit()
        c.close()
        return render_template("section2.html")


@listening.route("/section2", methods=['POST'])
def section2():
    if request.method == "POST":
        q11 = request.form['q11']
        q12 = request.form['q12']
        q13 = request.form['q13']
        q14 = request.form['q14']
        q15 = request.form['q15']
        q16 = request.form['q16']
        q17 = request.form['q17']
        q18 = request.form['q18']
        q19 = request.form['q19']
        q20 = request.form['q20']

        conn = mysql.connect()
        c = conn.cursor()
        query = "INSERT INTO user_answer(question,answer) VALUES (%s,%s)"
        val = [("11", q11), ("12", q12), ("13", q13), ("14", q14), ("15", q15),
               ("16", q16), ("17", q17), ("18", q18), ("19", q19), ("20", q20)]
        c.executemany(query, val)
        conn.commit()
        c.close()
        return render_template("section3.html")


@listening.route("/section3", methods=['POST'])
def section3():
    if request.method == "POST":
        q21 = request.form['q21']
        q22 = request.form['q22']
        q23 = request.form['q23']
        q24 = request.form['q24']
        q25 = request.form['q25']
        q26 = request.form['q26']
        q27 = request.form['q27']
        q28 = request.form['q28']
        q29 = request.form['q29']
        q30 = request.form['q30']

        conn = mysql.connect()
        c = conn.cursor()
        query = "INSERT INTO user_answer(question,answer) VALUES (%s,%s)"
        val = [("21", q21), ("22", q22), ("23", q23), ("24", q24), ("25", q25),
               ("26", q26), ("27", q27), ("28", q28), ("29", q29), ("30", q30)]
        c.executemany(query, val)
        conn.commit()
        c.close()
        return render_template("section4.html")


@listening.route("/section4", methods=['POST'])
def section4():
    if request.method == "POST":
        q31 = request.form['q31']
        q32 = request.form['q32']
        q33 = request.form['q33']
        q34 = request.form['q34']
        q35 = request.form['q35']
        q36 = request.form['q36']
        q37 = request.form['q37']
        q38 = request.form['q38']
        q39 = request.form['q39']
        q40 = request.form['q40']

        conn = mysql.connect()
        c = conn.cursor()
        query = "INSERT INTO user_answer(question,answer) VALUES (%s,%s)"
        val = [("31", q31), ("32", q32), ("33", q33), ("34", q34), ("35", q35),
               ("36", q36), ("37", q37), ("38", q38), ("39", q39), ("40", q40)]
        c.executemany(query, val)
        conn.commit()
        c.close()

        conn = mysql.connect()
        c = conn.cursor()
        query = "SELECT t.question,t.answer,u.answer FROM test_paper1 t, user_answer u WHERE t.id = u.id"
        c.execute(query)
        data = c.fetchall()

        q1 = "SELECT answer FROM test_paper1"
        c.execute(q1)
        testq1 = [item[0] for item in c.fetchall()]

        q2 = "SELECT answer FROM user_answer"
        c.execute(q2)
        testq2 = [item[0] for item in c.fetchall()]

        q3 = "SELECT alter_answer FROM test_paper1"
        c.execute(q3)
        testq3 = [item[0] for item in c.fetchall()]
        c.close()

        sec1 = section1ans()
        sec2 = section2ans()
        sec3 = section3ans()
        sec4 = section4ans()
        lower_section = get_lower_section(sec1, sec2, sec3, sec4)
        suggetion = get_suggestions(sec1, sec2, sec3, sec4)
        return submitted_Answer(testq1, testq2, testq3, data, suggetion, lower_section)


def section1ans():

    conn = mysql.connect()
    c = conn.cursor()
    q1 = "SELECT t.answer FROM test_paper1 t, user_answer u WHERE t.id = u.id LIMIT 10"
    c.execute(q1)
    tq1 = [item[0] for item in c.fetchall()]
    q2 = "SELECT u.answer FROM test_paper1 t, user_answer u WHERE t.id = u.id LIMIT 10"
    c.execute(q2)
    tq2 = [item[0] for item in c.fetchall()]
    q3 = "SELECT t.alter_answer FROM test_paper1 t, user_answer u WHERE t.id = u.id LIMIT 10"
    c.execute(q3)
    tq3 = [item[0] for item in c.fetchall()]
    c.close()
    s1Marks = section_score(tq1, tq2, tq3)
    return s1Marks


def section2ans():

    conn = mysql.connect()
    c = conn.cursor()
    q1 = "SELECT t.answer FROM test_paper1 t, user_answer u WHERE t.id = u.id LIMIT 10 OFFSET 10"
    c.execute(q1)
    tq1 = [item[0] for item in c.fetchall()]
    c = conn.cursor()
    q2 = "SELECT u.answer FROM test_paper1 t, user_answer u WHERE t.id = u.id LIMIT 10 OFFSET 10"
    c.execute(q2)
    tq2 = [item[0] for item in c.fetchall()]
    q3 = "SELECT t.alter_answer FROM test_paper1 t, user_answer u WHERE t.id = u.id LIMIT 10 OFFSET 10"
    c.execute(q3)
    tq3 = [item[0] for item in c.fetchall()]
    c.close()
    s2Marks = section_score(tq1, tq2, tq3)
    return s2Marks


def section3ans():

    conn = mysql.connect()
    c = conn.cursor()
    q1 = "SELECT t.answer FROM test_paper1 t, user_answer u WHERE t.id = u.id LIMIT 10 OFFSET 20"
    c.execute(q1)
    tq1 = [item[0] for item in c.fetchall()]
    q2 = "SELECT u.answer FROM test_paper1 t, user_answer u WHERE t.id = u.id LIMIT 10 OFFSET 20"
    c.execute(q2)
    tq2 = [item[0] for item in c.fetchall()]
    q3 = "SELECT t.alter_answer FROM test_paper1 t, user_answer u WHERE t.id = u.id LIMIT 10 OFFSET 20"
    c.execute(q3)
    tq3 = [item[0] for item in c.fetchall()]
    c.close()
    s3Marks = section_score(tq1, tq2, tq3)
    return s3Marks


def section4ans():

    conn = mysql.connect()
    c = conn.cursor()
    q1 = "SELECT t.answer FROM test_paper1 t, user_answer u WHERE t.id = u.id LIMIT 10 OFFSET 30"
    c.execute(q1)
    tq1 = [item[0] for item in c.fetchall()]

    q2 = "SELECT u.answer FROM test_paper1 t, user_answer u WHERE t.id = u.id LIMIT 10 OFFSET 30"
    c.execute(q2)
    tq2 = [item[0] for item in c.fetchall()]

    q3 = "SELECT t.alter_answer FROM test_paper1 t, user_answer u WHERE t.id = u.id LIMIT 10 OFFSET 30"
    c.execute(q3)
    tq3 = [item[0] for item in c.fetchall()]
    c.close()
    s4Marks = section_score(tq1, tq2, tq3)
    return s4Marks


@listening.route('/get_lower_section')
def get_lower_section(sec1, sec2, sec3, sec4):
    sections = {sec1: "section 1", sec2: "section 2",
                sec3: "section 3", sec4: "section 4"}
    if sec1 < 5 and sec2 < 5 and sec3 < 5 and sec4 < 5:
        if sec1 == sec2 and sec1 == sec3 and sec1 == sec4:
            return "Weak all sections"
        else:
            score = [sec1, sec2, sec3, sec4]
            minimum = score[0]
            for number in score:
                if minimum > number:
                    minimum = number
        return str(sections[minimum])
    else:
        return " Avarage scores for all sections"


def submitted_Answer(answer1, answer2, altanswer, data, suggetion, lower_section):
    ca = 0
    wrong = 0
    count = 0
    while count < len(answer1):
        if answer2[count] == answer1[count]:
            ca = ca + 1
            count = count + 1
        elif answer2[count] == altanswer[count]:
            ca = ca + 1
            count = count + 1
        else:
            wrong = wrong + 1
            count = count + 1
    return render_template('correct.html', output_data=data, score=ca, wrong_answers=wrong, suggestion=suggetion, lowest=lower_section)


@listening.route('/section_score')
def section_score(answer1, answer2, altanswer):
    ca = 0
    wrong = 0
    count = 0
    while count < len(answer1):
        if answer1[count] == answer2[count]:
            ca = ca + 1
            count = count + 1
        elif answer1[count] == altanswer[count]:
            ca = ca + 1
            count = count + 1
        else:
            wrong = wrong + 1
            count = count + 1
    return ca


@listening.route('/get_suggestions')
def get_suggestions(sec1, sec2, sec3, sec4):

    suggestions = {1: "You are at stage 1 : Great! You got a higher score. You have to focus on key ideas. We will guide you to improve your listening skill",
                      2: "You are at stage 2 : Great! You got a good score. You have to focus on key ideas and speaker's opinions and attitudes. We will guide you to improve your listening skill",
                      3: "You are at stage 3 : Great! You got a good score. You have to focus on given facts, key ideas and speaker's opinions and attitudes. We will guide you to get a higher band score and improve your listening skill.",
                      4: "You are at stage 4 : Hmm! You got a average score. You have to focus on given facts, key ideas and speaker's opinions and attitudes. We will guide you to get a higher band score. Start work with our study plan it will help you to learn faster.",
                      5: "You are at stage 5 : Hmm! You got a lower score. You have to focus on given facts, key ideas and speaker's opinions and attitudes. We will guide you to get a higher band score. Start work with our study plan it will help you to learn faster."
                   }
    section1 = sec1
    section2 = sec2
    section3 = sec3
    section4 = sec4
    test_data = [section1, section2, section3, section4]
    suggestion = suggestion_model.predict([test_data])[0]
    return str(suggestions[suggestion])


@listening.route('/listening/summary')
def summary():
    stud = {1: "stage 1",
            2: "stage 2",
            3: "stage 3",
            4: "stage 4",
            5: "stage 5"
            }
    sec1 = section1ans()
    sec2 = section2ans()
    sec3 = section3ans()
    sec4 = section4ans()
    test_data = [sec1, sec2, sec3, sec4]
    suggestion = suggestion_model.predict([test_data])[0]
    study = str(stud[suggestion])
    lower_section = get_lower_section(sec1, sec2, sec3, sec4)
    sp = study
    pln_no = int(suggestion)
    ws = str(lower_section)

    uid = int(current_user.id)
    conn = mysql.connect()
    c = conn.cursor()
    query = "INSERT INTO listening_user(user_id,study_plan,study_plan_no,progress,pid,weak_section) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (uid, sp, pln_no, 0, 0, ws)
    c.execute(query, val)
    conn.commit()
    data = {'study_plan':  sp, 'progress': 0,
            'weak_section': ws, 'study_plan_no': pln_no, 'pid': 0}
    return render_template('listening.html', data=data)


@listening.route("/listening/evaluate")
def evaluate():
    conn = mysql.connect()
    c = conn.cursor()
    uid = current_user.id
    q1 = "DELETE FROM listening_user where user_id = %s"
    c.execute(q1, uid)
    conn.commit()
    return listen()


@listening.route("/listening/progress1/<int:pid>", methods=['GET', 'POST'])
def update_plans(pid):
    conn = mysql.connect()
    c = conn.cursor()
    uid = current_user.id
    q1 = "SELECT progress FROM listening_user where user_id = %s"
    c.execute(q1, uid)
    progress = c.fetchone()[0]
    if progress == 100:
        flash('You were successfully completed this stage! please press  : evaluate study plan to check your skills')
        return listen()
    elif pid == 1 and progress == 0:
        progress4 = int(progress) + 20
    elif pid == 2 and progress == 20:
        progress4 = int(progress) + 20
    elif pid == 3 and progress == 40:
        progress4 = int(progress) + 20
    elif pid == 4 and progress == 60:
        progress4 = int(progress) + 20
    elif pid == 5 and progress == 80:
        progress4 = int(progress) + 20
    else:
        flash('You Must complete previous step before this to update progress!')
        return listen()
    q2 = "UPDATE listening_user SET progress = %s , pid = %s  WHERE user_id = %s ;"
    val = (progress4, pid, uid)
    c.execute(q2, val)
    conn.commit()
    c.close()
    return listen()


@listening.route("/listening/go_home")
def load_home():
    return listen()


@listening.route("/listening/lesson1")
def lesson1():
    return render_template('lesson1.html')


@listening.route("/listening/lesson2")
def lesson2():
    return render_template('lesson2.html')


@listening.route("/listening/lesson3")
def lesson3():
    return render_template('lesson3.html')


@listening.route("/listening/plan1_1")
def plan1_1():
    return render_template('plan1.1.html')


@listening.route("/listening/plan1_2")
def plan1_2():
    return render_template('plan1.2.html')


@listening.route("/listening/plan1_3")
def plan1_3():
    return render_template('plan1.3.html')


@listening.route("/listening/plan1_4")
def plan1_4():
    return render_template('plan1.4.html')


@listening.route("/listening/plan1_5")
def plan1_5():
    return render_template('plan1.5.html')


@listening.route("/listening/plan2_1")
def plan2_1():
    return render_template('plan2.1.html')


@listening.route("/listening/plan2_2")
def plan2_2():
    return render_template('plan2.2.html')


@listening.route("/listening/plan2_3")
def plan2_3():
    return render_template('plan2.3.html')


@listening.route("/listening/plan2_4")
def plan2_4():
    return render_template('plan2.4.html')


@listening.route("/listening/plan2_5")
def plan2_5():
    return render_template('plan2.5.html')


@listening.route("/listening/plan3_1")
def plan3_1():
    return render_template('plan3.1.html')


@listening.route("/listening/plan3_2")
def plan3_2():
    return render_template('plan3.2.html')


@listening.route("/listening/plan3_3")
def plan3_3():
    return render_template('plan3.3.html')


@listening.route("/listening/plan3_4")
def plan3_4():
    return render_template('plan3.4.html')


@listening.route("/listening/plan3_5")
def plan3_5():
    return render_template('plan3.5.html')


@listening.route("/listening/plan4_1")
def plan4_1():
    return render_template('plan4.1.html')


@listening.route("/listening/plan4_2")
def plan4_2():
    return render_template('plan4.2.html')


@listening.route("/listening/plan4_3")
def plan4_3():
    return render_template('plan4.3.html')


@listening.route("/listening/plan4_4")
def plan4_4():
    return render_template('plan4.4.html')


@listening.route("/listening/plan4_5")
def plan4_5():
    return render_template('plan4.5.html')


@listening.route("/listening/plan5_1")
def plan5_1():
    return render_template('plan5.1.html')


@listening.route("/listening/plan5_2")
def plan5_2():
    return render_template('plan5.2.html')


@listening.route("/listening/plan5_3")
def plan5_3():
    return render_template('plan5.3.html')


@listening.route("/listening/section1_1")
def section1_1():
    return render_template('section1.1.html')


@listening.route("/listening/section1_2")
def section1_2():
    return render_template('section1.2.html')


@listening.route("/listening/section1_3")
def section1_3():
    return render_template('section1.3.html')


@listening.route("/listening/section2_1")
def section2_1():
    return render_template('section2.1.html')


@listening.route("/listening/section2_2")
def section2_2():
    return render_template('section2.2.html')


@listening.route("/listening/section2_3")
def section2_3():
    return render_template('section2.3.html')


@listening.route("/listening/section3_1")
def section3_1():
    return render_template('section3.1.html')


@listening.route("/listening/section3_2")
def section3_2():
    return render_template('section3.2.html')


@listening.route("/listening/section3_3")
def section3_3():
    return render_template('section4.3.html')


@listening.route("/listening/section4_1")
def section4_1():
    return render_template('section4.1.html')


@listening.route("/listening/section4_2")
def section4_2():
    return render_template('section4.2.html')


@listening.route("/listening/section4_3")
def section4_3():
    return render_template('section4.3.html')
