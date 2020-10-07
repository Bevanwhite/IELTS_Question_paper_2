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
suggestion_model = joblib.load('Reading_activity_suggestion_up1.sav')

reading = Blueprint('reading', __name__)


app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ielts'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

path = ""


@reading.route("/reading")
@login_required
def read():
    uid = current_user.id
    conn = mysql.connect()
    c = conn.cursor()
    uid = current_user.id
    q1 = "SELECT user_id FROM reading_user where user_id = %s"
    try:
        c.execute(q1, uid)
        uid_db = c.fetchone()[0]
        if uid_db:
            q1 = "SELECT study_plan FROM reading_user where user_id = %s"
            c.execute(q1, uid)
            study_plan = c.fetchone()[0]
            q3 = "SELECT weak_section FROM reading_user where user_id = %s"
            c.execute(q3, uid)
            weak_section = c.fetchone()[0]
            q4 = "SELECT study_plan_no FROM reading_user where user_id = %s"
            c.execute(q4, uid)
            study_plan_no = c.fetchone()[0]
            c.close()
            data = {'study_plan':  study_plan,
                    'weak_section': weak_section, 'study_plan_no': study_plan_no}
            return render_template('reading.html', data=data)
        else:
            return render_template("reading_section1.html")
    except Exception as e:
        return render_template("reading_section1.html")


@reading.route("/reading_section1", methods=['POST'])
def section1():
    if request.method == "POST":
        q01 = request.form['q1']
        q02 = request.form['q2']
        q03 = request.form['q3']
        q04 = request.form['q4']
        q05 = request.form['q5']
        q06 = request.form['q6']
        q07 = request.form['q7']
        q08 = request.form['q8']
        q09 = request.form['q9']
        q10 = request.form['q10']
        q11 = request.form['q11']
        q12 = request.form['q12']
        q13 = request.form['q13']

        conn = mysql.connect()
        c = conn.cursor()
        drop = "DROP TABLE IF EXISTS user_answer_reading"
        c.execute(drop)
        create_table = "CREATE TABLE user_answer_reading (id INT(2) UNSIGNED AUTO_INCREMENT PRIMARY KEY,question VARCHAR(30) NOT NULL,answer VARCHAR(30) NOT NULL)"
        c.execute(create_table)
        query = "INSERT INTO user_answer_reading(question,answer) VALUES (%s,%s)"
        val = [("1", q01), ("2", q02), ("3", q03), ("4", q04), ("5", q05), ("6", q06), ("7",
                                                                                        q07), ("8", q08), ("9", q09), ("10", q10), ("11", q11), ("12", q12), ("13", q13)]
        c.executemany(query, val)
        conn.commit()
        c.close()
        return render_template("reading_section2.html")


@reading.route("/reading_section2", methods=['POST'])
def section2():
    if request.method == "POST":
        q14 = request.form['q14']
        q15 = request.form['q15']
        q16 = request.form['q16']
        q17 = request.form['q17']
        q18 = request.form['q18']
        q19 = request.form['q19']
        q20 = request.form['q20']
        q21 = request.form['q21']
        q22 = request.form['q22']
        q23 = request.form['q23']
        q24 = request.form['q24']
        q25 = request.form['q25']
        q26 = request.form['q26']
        q27 = request.form['q27']

        conn = mysql.connect()
        c = conn.cursor()
        query = "INSERT INTO user_answer_reading(question,answer) VALUES (%s,%s)"
        val = [("14", q14), ("15", q15), ("16", q16), ("17", q17), ("18", q18), ("19", q19),
               ("20", q20), ("21", q21), ("22", q22), ("23", q23), ("24", q24), ("25", q25), ("26", q26), ("27", q27)]
        c.executemany(query, val)
        conn.commit()
        c.close()
        return render_template("reading_section3.html")


@reading.route("/reading_section3", methods=['POST'])
def section3():
    if request.method == "POST":
        q28 = request.form['q28']
        q29 = request.form['q29']
        q30 = request.form['q30']
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
        query = "INSERT INTO user_answer_reading(question,answer) VALUES (%s,%s)"
        val = [("28", q28), ("29", q29), ("30", q30), ("31", q31), ("32", q32), ("33", q33),
               ("34", q34), ("35", q35), ("36", q36), ("37", q37), ("38", q38), ("39", q39), ("40", q40)]
        c.executemany(query, val)
        conn.commit()
        c.close()

        conn = mysql.connect()
        c = conn.cursor()
        query = "SELECT t.question,t.answer,u.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id"
        c.execute(query)
        data = c.fetchall()

        q1 = "SELECT t.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id"
        c.execute(q1)
        testq1 = [item[0] for item in c.fetchall()]

        q2 = "SELECT u.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id"
        c.execute(q2)
        testq2 = [item[0] for item in c.fetchall()]
        c.close()

        sec1 = section1ans()
        sec2 = section2ans()
        sec3 = section3ans()
        lower_section = get_lower_section(sec1, sec2, sec3)
        suggetion = get_suggestions(sec1, sec2, sec3)
        return submitted_Answer(testq1, testq2, data, suggetion, lower_section)


def section1ans():

    conn = mysql.connect()
    c = conn.cursor()
    q1 = "SELECT t.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id LIMIT 6"
    c.execute(q1)
    tq1 = [item[0] for item in c.fetchall()]
    q2 = "SELECT u.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id LIMIT 6"
    c.execute(q2)
    tq2 = [item[0] for item in c.fetchall()]
    c.close()
    s1Marks = section_score(tq1, tq2)
    return s1Marks


@app.route("/st2")
def section2ans():

    conn = mysql.connect()
    c = conn.cursor()
    q1_1 = "SELECT t.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id LIMIT 12 OFFSET 6"
    c.execute(q1_1)
    tq1_1 = [item[0] for item in c.fetchall()]
    q1_2 = "SELECT t.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id LIMIT 6 OFFSET 33"
    c.execute(q1_2)
    tq1_2 = [item[0] for item in c.fetchall()]
    tq1 = tq1_1 + tq1_2

    q2_1 = "SELECT u.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id LIMIT 12 OFFSET 6"
    c.execute(q2_1)
    tq2_1 = [item[0] for item in c.fetchall()]
    q2_2 = "SELECT u.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id LIMIT 6 OFFSET 33"
    c.execute(q2_2)
    tq2_2 = [item[0] for item in c.fetchall()]
    tq2 = tq2_1 + tq2_2
    c.close()
    s2Marks = section_score(tq1, tq2)
    return s2Marks


def section3ans():

    conn = mysql.connect()
    c = conn.cursor()
    q1_1 = "SELECT t.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id LIMIT 15 OFFSET 18"
    c.execute(q1_1)
    tq1_1 = [item[0] for item in c.fetchall()]
    q1_2 = "SELECT t.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id LIMIT 1 OFFSET 39"
    c.execute(q1_2)
    tq1_2 = [item[0] for item in c.fetchall()]
    tq1 = tq1_1 + tq1_2

    q2_1 = "SELECT u.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id LIMIT 15 OFFSET 18"
    c.execute(q2_1)
    tq2_1 = [item[0] for item in c.fetchall()]
    q2_2 = "SELECT u.answer FROM reading_test_paper1 t, user_answer_reading u WHERE t.id = u.id LIMIT 1 OFFSET 39"
    c.execute(q2_2)
    tq2_2 = [item[0] for item in c.fetchall()]
    tq2 = tq2_1 + tq2_2
    c.close()
    s3Marks = section_score(tq1, tq2)
    return s3Marks


@reading.route('/section_score')
def section_score(answer1, answer2):
    ca = 0
    wrong = 0
    count = 0
    while count < len(answer1):
        if answer1[count] == answer2[count]:
            ca = ca + 1
            count = count + 1
        else:
            wrong = wrong + 1
            count = count + 1
    return int((ca/len(answer1))*100)


@reading.route('/get_lower_section')
def get_lower_section(sec1, sec2, sec3):
    sections = {sec1: "section 1", sec2: "section 2",
                sec3: "section 3"}
    if sec1 == sec2 and sec1 == sec3:
        return "weak all sections"
    else:
        score = [sec1, sec2, sec3]
        minimum = score[0]
        for number in score:
            if minimum > number:
                minimum = number
    return str(sections[minimum])


@reading.route("/submit")
def submitted_Answer(answer1, answer2, data, suggestion, weak_section):
    ca = 0
    wrong = 0
    count = 0
    while count < len(answer1):
        if answer1[count] == answer2[count]:
            ca = ca + 1
            count = count + 1
        else:
            wrong = wrong + 1
            count = count + 1
    return render_template('reading_summary.html', output_data=data, score=ca, wrong_answers=wrong, suggestion=suggestion, weak_section=weak_section)


@reading.route('/get_suggestions')
def get_suggestions(sec1, sec2, sec3):
    global path
    suggestions = {1: "You are lack with reading skills. You have to focus more and give a big effort. You have to improve reading and comprehension skills. While reading, focus on main idea of the paragraph. Then focus on details provided. Furthermore improve your skills on comprehension by understanding writer’s opinion for that you can use why? What? When? Kind of questions to analyse the details inside your mind. Try to improve your vocabulary as well as grammar skills. Keep on reading books, newspapers. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   2: "Your reading skills need to be improved. You are currently at a low stage but you can improve your skills. Focus on main idea of the provided paragraph then focus on details. Meanwhile focus on comprehension skills too, like writers opinion for that manage your reading skills with why? What? When? Inside your head. Improve your vocabulary as well as grammar skills. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more. ",
                   3: "your reading skills are at an average stage. Focus on reading for the main idea as well as details and comprehension. More over develop your vocabulary. Trying on more questions will help you to increase your score. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more. ",
                   4: "you are good at your reading skills. Improve your vocabulary and keep trying on questions will help you to improve your score. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   5: "You are good at your reading skills. No need of special improvement or guidance. Keep on practicing with more questions as well as improve your vocabulary. Provided exercises will help you to improve your skills. Keep trying on such kind of questions.",
                   6: "You are lacking with reading skills. You have to focus more and give a big effort. You have to improve on reading and comprehension skills. While reading, focus on main idea as well as for details. Improve your comprehension skills on writer’s opinion/logical argument and attitude purpose. For that improving vocabulary, reading Skills, efficiency and speed will be helpful. By reading books, journals, newspapers and whatever the things you have, can caused a major impact on improving your reading skills. Specially focus on good quality reading materials. While reading, improve the self-argument on why? What? When? Kind logical thinking regarding the paragraphs. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more and more.",
                   7: "You are lacking with reading skills but average on reading for detail. Focus on main idea too. For that improve your logical thinking. Try to focus on writer’s opinion. Always try to get the whole idea which writer tries to give. Furthermore need to improve comprehension skills. You are lack on comprehension skills as well. Improve your vocabulary reading skills, efficiency and speed for that read more books, journals newspapers, good quality reading materials with the logical thinking. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more and more. ",
                   8: "You are lacking with reading skills but your skills on understanding details is on the above average. But reading for main idea and comprehension skills are very poor. Need to improve those skills as well in order to achieve your target. Improve logical thinking, understanding writer’s opinion by reading more quality reading materials will help you to score at those areas. Need to improve vocabulary, reading efficiency and reading speed as well. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more and more.",
                   9: "You are lacking with reading skills but your skills on understanding details is great. But reading for main idea and comprehension skills are very poor. Need to improve those skills as well in order to achieve your target. Improve logical thinking, understanding writer’s opinion by reading more quality reading materials will help you to score at those areas. Need to improve vocabulary, reading efficiency and reading speed as well. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more and more.",
                   10: "You are lack with reading skills. Even though you have score marks at reading for main idea skills, they are at a lower rate. Reading for detail and comprehension skills are very poor. Need to improve reading skills, need to understand the logical argument and the content details. For that focus on reading quality reading materials, books journals and try to figure the content as well as the overall idea in writer’s point of view. Try to comprehend alone by reading several times and focus on key points while reading. Need to improve comprehension skills, vocabulary, reading efficiency and speed. More practice will help you to improve your reading skills. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more and more.",
                   11: "Your have scored in main idea understanding and reading for detail but at a lower rate. Comprehension skills are very poor. Overall your reading skills are poor. Try to figure what is the overall idea and what is the content while reading. Need to improve understanding logical argument and the content details more. Keep practicing by reading more and more on quality reading materials and try to comprehend alone by reading several times and focus on key points while reading. Need to improve vocabulary, reading efficiency and reading speed. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more. ",
                   12: "You have scored reading for main idea skills are at a lower rate and reading for detail skills are at an average rate.  But comprehension skills are very poor. Need to focus on writer’s opinion and keep improving in logical thinking and attitude purpose. While reading focus on main idea in a way of why? What?. More practice on reading for detail will improve your reading for detail skills. Need to improve vocabulary, reading efficiency and speed. Keep reading more quality reading materials and try to comprehend alone by reading several times and focus on key points while reading. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   13: "You have scored reading for main idea skills are at a lower rate and reading for detail skills are at above the average rate.  But reading for main idea should be improve more. Comprehension skills are very poor. Keep reading more quality reading materials and try to comprehend alone by reading several times and focus on key points while reading. While reading focus on main idea in a way of why? What? In order to improve your main idea understanding skills. Keep practicing on reading considering above points. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   14: "You have scored reading for main idea skills are at a lower rate and reading for detail skills are at a maximum rate. Keep practicing on understanding the overall idea, writer’s opinion and logical argument while reading. Your score means that you have the capability and you need more skills on comprehension, and your comprehension skills are very poor.  ",
                   15: "Your skills on reading for main idea is at an average stage. But skills on details understanding and comprehension is very poor. Focus on content while understanding the main idea as well. Need to improve vocabulary, reading efficiency and speed. Keep practicing on reading quality materials. Try to comprehend alone by reading several times and focus on key points while reading. Keep practicing on reading considering above points. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   16: "Your reading for main idea skills are at an average stage. But reading for detail skills are lower than the average. Comprehension skills are very poor. You need to focus on the content while you are reading. Focus on the key points. Try to extract the meaning and the theme behind. For that you need to read more and more quality reading materials. Try to grab the details and the real meaning. Keep practicing with questions. Learn to read with a logical thinking considering when? Why? What? Your reading for main idea skills will be improved above the average while practicing with more questions and papers. Improve your vocabulary and spellings as well. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   17: "Your Skills on reading for main idea and reading for detail are at an average stage. But comprehension skills are very poor. Focus on the story behind when reading. Learn to read with a logical thinking considering when? Why? What?  Read more and more good reading materials and while trying to get the story behind. Try to comprehend alone by reading several times and focus on key points while reading. By continuing the practice with questions you can improve your reading for main idea and detail skills above the average. Focus more on comprehend whatever the things you read. Keep practicing on reading considering above points. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   18: "Your skills on reading for main idea is on average stage and reading for detail skills are above the average. But your comprehension skills are very poor. Focus the overall idea and writer’s opinion while reading it will improve your reading for main idea skills above the average. Keep practicing with more related questions will improve your reading for detail skills more. Keep trying to understand the story behind to improve your comprehension skills. Learn to read with a logical thinking considering when? Why? What? Keep reading quality reading materials considering these points. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   19: "Your reading for main idea skills are at an average stage. Your reading for detail skills are excellent. But your comprehension skills are very poor. You need to balance your skills to improve yourself. Read quality materials with better understanding. Learn to read with logical thinking on why? What? When? Try to get the writer’s opinion and the story behind. Keep practicing will increase your skills. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   20: "Your reading for main idea skills are excellent while reading for detail and comprehension skills are very poor. You need to improve those skills too. While reading focus on details and content. Learn to read with the logical thinking in order to score at comprehension sections. Read more and more quality reading materials and try to understand the story behind. Improve vocabulary and spellings as well. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   21: "Your reading for main idea skills are excellent. But reading for detail skills are at a lower stage and comprehension skills are very poor. While reading focus on main points and details and try to grab the content. Considering those things and practice with more quality reading materials and questions will improve your reading for detail skills. To get a better comprehension skill learn and train yourself on logical thinking. Try to understand the background story. Improve your vocabulary and spellings as well. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   22: "Your reading for main idea skills are excellent and your reading for detail skills are at an average stage. But your comprehension skills are very poor. You need to improve your comprehension skills. For that read more and more quality reading materials. Try to understand the story behind and the writer’s opinion. Improve your vocabulary and spellings as well. To get a better comprehension skill learn and train yourself on logical thinking. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more..",
                   23: "Your reading for main idea skills are excellent. Your’ reading for detail skills also above the average. But your comprehension skills are very poor. Learn to read with logical thinking in order to improve comprehension skills. Try to understand the story behind. Keep practicing with more reading materials. By practicing more with questions you can improve your reading for detail skills more. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   24: "your reading for main idea and detail skills are excellent. But your comprehension skills are very poor. You need to score in that area too. So learn to read with logical thinking. Try to understand the story behind. Practicing in a right way you can improve your skills easily as you show excellent performances at the other two. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   25: "Your reading for main idea and details skills are very poor. And comprehension skills also at a lower place. You need to focus on reading more and more. Improve your vocabulary and spellings as well. Focus on writer’s opinion as well as the story behind. Focus on key words and try to grab the idea. Keep thinking on why? what? when? While reading. Try to grab the content and details keep practicing with more and more questions and read quality reading materials as well. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   26: "Your’ reading for main idea and reading for details skills are very poor and comprehension skills are at a. You need to improve your reading skills. Try to read with logical thinking, try to understand writer’s opinion while reading. Improve your vocabulary and spellings as well. Since you have the average comprehension skills reading while grabbing the overall idea and key words you can improve your skills. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   27: "Your reading for main idea skills and reading for detail skills are very poor even though you have comprehension skills above the average. Try to balance and improve your reading for main idea and detail skills as well in order to gain marks. Focus on overall idea and story behind and grab key words to collect details. Since you have comprehension skills above the average practicing with relevant questions will improve your skills. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   28: "Your reading for main idea skills and reading for detail skills are very poor even though you have comprehension skills at an excellent level. Seems you have a problem with these kind of reading for main idea and detail questions. Good practice with those kind of questions will improve your skills. Try to read while understanding the overall idea and grab key words to collect details. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   29: "Your reading for main idea and reading for detail skills are at a lower rate while your comprehension skills are very poor. Read more and more quality reading materials and try to understand the story behind. Read while understanding the logical argument. Grab the key words to collect details. Read while thinking why? what? When? Kind of understanding. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   30: "Your’ reading for main idea, reading for detail and comprehension skills are at a lower rate. Improve your vocabulary as well as spellings. Try to read with logical thinking and try to understand the story behind while reading. Grab the key points to collect details. Take a look at the questions and provided answers before reading the paragraphs. Practice with more questions and reading more and more quality reading materials will improve your skills. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   31: "your reading for main idea skills and reading for detail skills are at a very lower rate while comprehension skills are average. Read more and more quality reading materials with logical thinking. Grab the key points in order to collect details. Understand writer’s opinion and story behind. Improve your vocabulary and spellings as well. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more. ",
                   32: "your reading for main idea skills and reading for detail skills are at a very lower rate while comprehension skills are at an excellent rate. Try to balance the skills. Read while understanding the logical argument, read while grabbing the key words to collect data. Try to figure the story behind. Since you are having good comprehension skills practice with the reading for main idea and detail questions will improve your skills on them. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   33: "Your’ reading for main idea and reading for detail skills are at an average level.  But your comprehension skills are very poor. Read more and more quality reading materials with logical thinking. Read while thinking why? what? When? Kind of understanding. Try to figure the story behind and what writer is willing to tell. Practice with more questions will improve your skills. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   34: "Your’ reading for main idea and reading for detail skills are at an average level. While your comprehension skills are at a lower rate. Read more and more quality reading materials with logical thinking and understanding the story behind. Practicing more questions will improve your skills. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   35: "Your’ reading for main idea skills, reading for details and comprehension skills are all at an average rate. Practicing more and more questions will improve your skills. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   36: "your’ reading for main idea and reading for detail skills are at an average rate while having above the average comprehension skills. Improve logical thinking and grab key words while reading .As you are having good comprehension skills and average skills on other two, practicing with more and more questions will improve your skills. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more",
                   37: "your’ reading for main idea and reading for detail skills are at an average rate while having excellent comprehension skills. As you are having good comprehension skills and average skills on other two, practicing with more and more questions will improve your skills. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   38: "You have excellent reading for main idea and reading for detail skills. But unfortunately your comprehension skills are very poor. You may have difficulty of answering comprehension questions. While reading focus on the writer’s opinion and the story behind. Read while having the logical argument what? Why? when? To understand the story. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   39: "You have excellent reading for main idea and reading for detail skills. But your comprehension skills are at a lower rate. Improve answering skills of comprehension questions. While reading focus on the writer’s opinion and the story behind. Improve your’ vocabulary and spellings as well. Read while having the logical argument what? Why? when? To understand the story. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more",
                   40: "Your’ reading for main idea and reading for detail skills are excellent but comprehension skills are average. Focus on story behind while reading. Read more and more quality reading materials and try to comprehend. Improve vocabulary as well. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more",
                   41: "You have excellent reading for main idea and reading for detail skills and your’ comprehension skills also above the average. Therefore practicing more questions on comprehension while having logical thinking and improving vocabulary will help you to improve your comprehension skills. No any special guidance needed. Provided exercises will help you to improve your skills. Keep trying on such kind of questions more.",
                   42: "You have score well in reading for main idea, reading for detail and comprehension. You are at a good level. Well done and keep it up. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions",
                   43: "you have to improve your’ reading skills. Your reading skills are at a lower rate. Your reading for detail skills are very poor. Read more and more quality reading materials. Read with logical thinking. Try to understand the writer’s opinion. Grab key words to collect the details. Read the questions and answers provided, before reading the paragraphs. Improve your’ vocabulary and spellings as well. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.",
                   44: "You have average skills in reading for main idea and comprehension skills. But your’ reading for detail skills are very poor. Keep reading on more and more quality reading materials and try to grab the key words to collect details. Read questions and answers before reading the passage while answering. Improve your’ vocabulary and spellings as well. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.",
                   45: "Your’ reading for main idea and comprehension skills are above the average. But the reading for detail skills are very poor. Try to grab the details while reading. Read questions and answers before reading the passage while answering. Improve your’ vocabulary and spellings as well. As your other skills are at a good level seems more practice will improve your skills. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.",
                   46: "Your’ reading for main idea and comprehension skills are excellent. But unfortunately the reading for detail skills are very poor. Try to grab the details while reading. Read questions and answers before reading the passage while answering. Improve your’ vocabulary and spellings as well. As your other skills are at a very good level seems more practice will improve your skills. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.",
                   47: "Your skills on reading for main idea and comprehension are at a lower rate. Your’ reading for detail skills are at an average rate. Read more and more quality reading materials with logical thinking. Try to understand the writer’s opinion. Grab key words to identify the story behind. Improve your’ vocabulary and spellings as well. Keep practicing with more and more questions. Read questions and answers before reading the passage while answering. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.  ",
                   48: "Your skills on reading for main idea and comprehension are at a lower rate. Your’ reading for detail skills are above the average. Read more and more quality reading materials with logical thinking. Try to understand the writer’s opinion. Grab key words to identify the story behind. Improve your’ vocabulary and spellings as well. Keep practicing with more and more questions. Read questions and answers before reading the passage while answering. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.",
                   49: "Your reading for main idea and comprehension skills are at a lower rate. But your’ reading for detail skills are excellent try to read with logical thinking and try to understand the story behind. Improve your vocabulary as well as spellings. Try to understand the writer’s opinion while reading. Grab key words to identify the story behind. As your’ reading for detail skills are excellent, you can improve your comprehension with practice. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.",
                   50: "Your reading for main idea and comprehension skills are at an average level. And your’ reading for detail skills are above the average. Seems you can improve your skills by reading more and more quality reading materials with logical thinking and practicing with related questions. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.",
                   51: "Your’ reading for main idea and comprehension skills are at an average rate and your’ reading for detail skills are above the average. Overall your reading skills can be improve easily with your dedication. Practice more questions and read more quality reading materials while try to understand the logical argument. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.",
                   52: "Your’ reading for main idea and comprehension skills are above the average level and your’ reading for detail skills are excellent. Overall your reading skills can be improve easily. No any special guidance needed. Practice more questions and read more quality reading materials while try to understand the logical argument. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.",
                   53: "your’ reading for main idea and reading for detail skills are above the average. But unfortunately your’ comprehension skills are very poor. Seems you have problem of answering comprehension questions. Keep practice with comprehension questions. Read more quality reading materials with logical thinking. Try to understand the story behind. As your reading for detail skills are good, you can improve your comprehension skills by focusing on that. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.",
                   54: "You have above the average skills on reading for main idea and reading for detail. But comprehension skills are at a lower rate. Keep practice with comprehension questions. Read more quality reading materials with logical thinking. Try to understand the story behind. As your reading for detail skills are good, you can improve your comprehension skills by focusing on that. Keep practicing with questions. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions",
                   55: "Your’ reading for main idea and reading for detail skills are above the average. And your’ comprehension skills are at average level. Therefor your reading skills seems to be fine. With more practice and improving logical thinking you can improve the rest. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions",
                   56: "Your’ reading for main idea, reading for detail and comprehension skills are above the average level. Your’ reading skills are at a good level. Keep practicing will improve the rest. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.",
                   57: "Your’ reading skills are good. Reading for main idea and detail skills are above the average and comprehension skills are in an excellent level. Keep practicing will improve the rest. Provided exercises will help you to improve your skills. Keep practicing with such kind of questions.",
                   }

    section1 = sec1
    section2 = sec2
    section3 = sec3

    test_data = [section1, section2, section3]
    suggestion = suggestion_model.predict([test_data])[0]

    path = "/public/Comprehension/"+str(suggestion)+".html"

    return suggestions[suggestion]


@reading.route('/reading/summary')
def summary():
    sec1 = section1ans()
    sec2 = section2ans()
    sec3 = section3ans()
    test_data = [sec1, sec2, sec3]
    suggestion = suggestion_model.predict([test_data])[0]
    lower_section = get_lower_section(sec1, sec2, sec3)
    pln_no = int(suggestion)
    ws = str(lower_section)
    sp = "stage " + str(pln_no)

    uid = int(current_user.id)
    conn = mysql.connect()
    c = conn.cursor()
    query = "INSERT INTO reading_user(user_id,study_plan,study_plan_no,weak_section) VALUES (%s,%s,%s,%s)"
    val = (uid, sp, pln_no, ws)
    c.execute(query, val)
    conn.commit()
    data = {'study_plan':  sp, 'weak_section': ws, 'study_plan_no': pln_no}
    return render_template('reading.html', data=data)


@reading.route("/reading/evaluate")
def evaluate():
    conn = mysql.connect()
    c = conn.cursor()
    uid = current_user.id
    q1 = "DELETE FROM reading_user where user_id = %s"
    c.execute(q1, uid)
    conn.commit()
    return read()


@app.route('/see_suggestions', methods=["GET", "POST"])
def see_suggestions():
    global path
    return render_template(path)


@reading.route("/reading/go_home")
def load_home():
    return read()


@reading.route("/reading/plan0")
def plan0():
    return render_template('0.html')


@reading.route("/reading/plan25")
def plan25():
    return render_template('25.html')


@reading.route("/reading/plan50")
def lesson3():
    return render_template('50.html')


@reading.route("/reading/plan75")
def plan50():
    return render_template('75.html')


@reading.route("/reading/plan100")
def plan100():
    return render_template('100.html')


@reading.route("/reading/plan_detail0")
def plan_detail0():
    return render_template('detail0.html')


@reading.route("/reading/plan_detail25")
def plan_detail25():
    return render_template('detail25.html')


@reading.route("/reading/plan_detail50")
def plan_detail50():
    return render_template('detail50.html')


@reading.route("/reading/plan_detail75")
def plan_detail75():
    return render_template('detail75.html')


@reading.route("/reading/plan_detail100")
def plan_detail100():
    return render_template('detail100.html')


@reading.route("/reading/plan_main0")
def plan_main0():
    return render_template('main0.html')


@reading.route("/reading/plan_main25")
def plan_main25():
    return render_template('main25.html')


@reading.route("/reading/plan_main50")
def plan_main50():
    return render_template('main50.html')


@reading.route("/reading/plan_main75")
def plan_main75():
    return render_template('main75.html')


@reading.route("/reading/plan_main100")
def plan_main100():
    return render_template('main100.html')
