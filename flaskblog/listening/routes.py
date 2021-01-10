from flask import Flask, flash, Blueprint, render_template, request, Blueprint, jsonify
from flask_login import login_required
from flask_login import current_user
from flaskext.mysql import MySQL
import joblib
import sys
import os
from werkzeug.utils import secure_filename
# Import trained model
suggestion_model = joblib.load(
    'flaskblog/listening/Listening_activity_suggestion_up1.sav')
# create blueprint to route
listening = Blueprint('listening', __name__)

# Import config to MYSQL db
app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ielts'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

UPLOAD_FOLDER = 'flaskblog/static/listening_audio'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Main page


@listening.route("/listening")
@login_required
def listen():
    uid = current_user.id
    conn = mysql.connect()
    c = conn.cursor()
    uid = current_user.id

    try:
        q = "SELECT paper_id  FROM listening_add_paper WHERE paper_id = 1"
        c.execute(q)
        paper_id = c.fetchone()[0]
        if paper_id:
            papers = available_quiz()
            papers1 = papers[0]
            papers2 = papers[1]
            papers3 = papers[2]
            papers4 = papers[3]
    except Exception:
        papers = {0,"no papers available"}
        create_table1= "CREATE TABLE IF NOT EXISTS listening_add_paper (paper_id INT(20) UNSIGNED AUTO_INCREMENT PRIMARY KEY , paper_name VARCHAR(150) , media_file VARCHAR(150) , instruct VARCHAR(150), level INT(2))"
        c.execute(create_table1)
        query = "INSERT INTO listening_add_paper(paper_name,media_file,instruct,level) VALUES (%s,%s,%s,%s)"
        val = ['sample paper' ,'no_file', 'instruct',1]
        c.execute(query, val)
        conn.commit()

        create_table2= "CREATE TABLE IF NOT EXISTS listening_add_paper_mcq(id INT(2) UNSIGNED AUTO_INCREMENT PRIMARY KEY, qid int(2), question VARCHAR(150) NOT NULL, a  VARCHAR(150), b  VARCHAR(150), c  VARCHAR(150),d  VARCHAR(150), corret_answer VARCHAR(150) , paper_id INT(20))"
        c.execute(create_table2)
        query = "INSERT INTO listening_add_paper_mcq(qid,question,a,b,c,d, corret_answer , paper_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = [1, 'ques','ans1','ans2','ans3','ans4','a',1]
        c.execute(query, val)
        conn.commit()

        create_table3 = "CREATE TABLE IF NOT EXISTS listening_add_paper_ttype(id INT(2) UNSIGNED AUTO_INCREMENT PRIMARY KEY , qid int(2) , question VARCHAR(150) NOT NULL , answer VARCHAR(150), paper_id INT(20))"
        c.execute(create_table3)
        query = "INSERT INTO listening_add_paper_ttype(qid,question,answer, paper_id) VALUES (%s,%s,%s,%s)"
        val = [2, 'ques','answer',1]
        c.execute(query, val)
        conn.commit()

        create_table4 = "CREATE TABLE IF NOT EXISTS listening_add_paper_matching (id INT(2) UNSIGNED AUTO_INCREMENT PRIMARY KEY , qid int(2) , question VARCHAR(150) NOT NULL , answer VARCHAR(150), paper_id INT(20))"
        c.execute(create_table4)
        query = "INSERT INTO listening_add_paper_matching(qid,question,answer,paper_id) VALUES (%s,%s,%s,%s)"
        val = [3, 'ques','answer',1]
        c.execute(query, val)
        conn.commit()

        create_table5= "CREATE TABLE IF NOT EXISTS listening_add_paper_multiple(id INT(2) UNSIGNED AUTO_INCREMENT PRIMARY KEY, qid int(2), question VARCHAR(150) NOT NULL, a  VARCHAR(150), b  VARCHAR(150), c  VARCHAR(150), d  VARCHAR(150), ans_a  int(2), ans_b int(2), ans_c  int(2),ans_d  int(2), paper_id INT(20))"
        c.execute(create_table5)
        query = "INSERT INTO listening_add_paper_multiple(qid,question,a,b,c,d,ans_a,ans_b,ans_c,ans_d, paper_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = [4, 'ques','ans1','ans2','ans3','ans4',0,0,0,0,1]
        c.execute(query, val)
        conn.commit()

    

    table = "CREATE TABLE IF NOT EXISTS listening_user (user_id int(5) UNSIGNED NOT NULL PRIMARY KEY, study_plan varchar(20) NOT NULL,study_plan_no float NOT NULL,progress int(5) DEFAULT NULL,pid int(5) NOT NULL,weak_section varchar(50) NOT NULL)"
    c.execute(table)
    q1 = "SELECT user_id FROM listening_user where user_id = %s"
    try:
        c.execute(q1, uid)
        uid_db = c.fetchone()[0]
        # if current user availble in database load their data to main page
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
                    'weak_section': weak_section, 'study_plan_no': study_plan_no, 'pid': pid , 'papers1': papers1 , 'papers2': papers2 , 'papers3': papers3 , 'papers4': papers4}
            return render_template('/listening/listening_home.html', data=data)
        # if current user not in database load test paper
        else:
            return render_template("/listening/test_papers/listening_test_paper1_section1.html")
    except Exception:
        return render_template("/listening/test_papers/listening_test_paper1_section1.html")

# teset paper section1 tempory answers save to database


@listening.route("/listening/section1", methods=['POST'])
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

        conn = mysql.connect()
        c = conn.cursor()
        # delete previous user's temporary data
        drop = "DROP TABLE IF EXISTS  user_answer"
        c.execute(drop)
        drop1 = "DROP TABLE IF EXISTS  test_paper1"
        c.execute(drop1)
        create_table = "CREATE TABLE IF NOT EXISTS user_answer (id INT(2) UNSIGNED AUTO_INCREMENT PRIMARY KEY,question VARCHAR(150) NOT NULL,answer VARCHAR(150))"
        create_ans_table = "CREATE TABLE IF NOT EXISTS test_paper1 (id int(2) UNSIGNED NOT NULL AUTO_INCREMENT,question VARCHAR(150) NOT NULL,answer VARCHAR(150) NOT NULL,alter_answer varchar(50) NOT NULL,PRIMARY KEY (id))"
        c.execute(create_table)
        c.execute(create_ans_table)
        query = "INSERT INTO test_paper1(id,question,answer,alter_answer) VALUES (%s,%s,%s,%s)"
        val = [(1, 1, "choose", "-1"), (2, 2, "private", "-1"), (3, 3, "20%", "20 percent"), (4, 4, "healthy", "-1"), (5, 5, "bones", "-1"), (6, 6, "lecture", "-1"), (7, 7, "Arretsa", "-1"), (8, 8, "vegetarian", "-1"),
               (9, 9, "market", "-1"), (10, 10, "knife", "-1"), (11, 11, "b", "B"), (12, 12, "c", "C"), (13, 13, "b",
                                                                                                         "B"), (14, 14, "e", "E"), (15, 15, "d", "D"), (16, 16, "b", "B"), (17, 17, "g", "G"), (18, 18, "c", "C"),
               (19, 19, "h", "H"), (20, 20, "i", "I"), (21, 21, "a", "A"), (22, 22, "c", "C"), (23, 23, "b", "B"), (24, 24,
                                                                                                                    "c", "C"), (25, 25, "c", "C"), (26, 26, "g", "G"), (27, 27, "c", "C"), (28, 28, "h", "H"), (29, 29, "a", "A"),
               (30, 30, "e", "E"), (31, 31, "crow", "-1"), (32, 32, "cliffs", "-1"), (33, 33, "speed", "-1"), (34, 34, "brain",
                                                                                                               "-1"), (35, 35, "food", "-1"), (36, 36, "behavior", "-1"), (37, 37, "frighten", "-1"), (38, 38, "blood", "-1"),
               (39, 39, "tails", "-1"), (40, 40, "permanent", "-1")]
        c.executemany(query, val)

        query1 = "INSERT INTO user_answer(question,answer) VALUES (%s,%s)"
        val1 = [("1", q01), ("2", q02), ("3", q03), ("4", q04), ("5", q05),
                ("6", q06), ("7", q07), ("8", q08), ("9", q09), ("10", q10)]
        c.executemany(query1, val1)
        conn.commit()
        c.close()
        return render_template("/listening/test_papers/listening_test_paper1_section2.html")

# teset paper section2 tempory answers save to database


@listening.route("/listening/section2", methods=['POST'])
def section2():
    if request.method == "POST":
        q11 = request.form['q011']
        q12 = request.form['q012']
        q13 = request.form['q013']
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
        return render_template("/listening/test_papers/listening_test_paper1_section3.html")

# teset paper section3 tempory answers save to database


@listening.route("/listening/section3", methods=['POST'])
def section3():
    if request.method == "POST":
        q21 = request.form['q021']
        q22 = request.form['q022']
        q23 = request.form['q023']
        q24 = request.form['q024']
        q25 = request.form['q025']
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
        return render_template("/listening/test_papers/listening_test_paper1_section4.html")

# teset paper section4 tempory answers save to database


@listening.route("/listening/section4", methods=['POST'])
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
        # get separate sections scores
        sec1 = section1ans()
        sec2 = section2ans()
        sec3 = section3ans()
        sec4 = section4ans()

        # get lowest section score
        lower_section = get_lower_section(sec1, sec2, sec3, sec4)
        # get suggested studyplan
        suggetion = get_suggestions(sec1, sec2, sec3, sec4)
        # return above data to submitted_answer function
        return submitted_Answer(testq1, testq2, testq3, data, suggetion, lower_section)

# teset paper section1 tempory answers get from data base and send to paper cheching


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
    # send to check function
    s1Marks = section_score(tq1, tq2, tq3)
    return s1Marks

# teset paper section2 tempory answers get from data base and send to paper checking


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

# teset paper section3 tempory answers get from data base and send to paper cheching


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

# teset paper section4 tempory answers get from data base and send to paper cheching


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

# find lowest section score


@listening.route('/listening/get_lower_section')
def get_lower_section(sec1, sec2, sec3, sec4):

    sections = {sec1: "section 1", sec2: "section 2",
                sec3: "section 3", sec4: "section 4"}

    score = [sec1, sec2, sec3, sec4]
    minimum = score[0]
    for number in score:
        if minimum > number:
            minimum = number

    if minimum == sec1 and minimum == sec2 and minimum == sec3 and minimum == sec4:
        if sec1 < 6 and sec2 < 6 and sec3 < 6 and sec4 < 6:
            return "Weak all sections"
        if sec1 > 6 and sec2 > 6 and sec3 > 6 and sec4 > 6:
            return " Avarage scores"
    elif minimum == sec1 and minimum == sec2 and minimum == sec3:
        return "section 1 , 2 and 3"
    elif minimum == sec1 and minimum == sec2 and minimum == sec4:
        return "section 1 , 2 and 4"
    elif minimum == sec1 and minimum == sec3 and minimum == sec4:
        return "section 1 , 3 and 4"
    elif minimum == sec1 and minimum == sec3 and minimum == sec4:
        return "section 2 , 3 and 4"
    elif minimum == sec1 and minimum == sec2:
        return "section 1 and 2"
    elif minimum == sec1 and minimum == sec3:
        return "section 1 and 3"
    elif minimum == sec1 and minimum == sec4:
        return "section 1 and 4"
    elif minimum == sec2 and minimum == sec3:
        return "section 2 and 3"
    elif minimum == sec2 and minimum == sec4:
        return "section 2 and 4"
    elif minimum == sec3 and minimum == sec4:
        return "section 3 and 4"
    else:
        return str(sections[minimum])

# checking answers with real answers


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
    # feedback and summarized report
    return render_template('/listening/listening_summary.html', output_data=data, score=ca, wrong_answers=wrong, suggestion=suggetion, lowest=lower_section)

# checking separate section  answers with real answers


@listening.route('/listening/section_score')
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

# generate studyplan


@listening.route('/listening/get_suggestions')
def get_suggestions(sec1, sec2, sec3, sec4):
    # feedbacks
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
# after test paper mainpage will load with this data


@listening.route('/listening/summary')
def summary():
    stud = {1: "Stage 1",
            2: "Stage 2",
            3: "Stage 3",
            4: "Stage 4",
            5: "Stage 5"
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
    # insert data to listening user table
    query = "INSERT INTO listening_user(user_id,study_plan,study_plan_no,progress,pid,weak_section) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (uid, sp, pln_no, 0, 0, ws)
    c.execute(query, val)
    conn.commit()
    return listen()

# after complete plan user can reset his current study plan and get new one


@listening.route("/listening/evaluate")
def evaluate():
    conn = mysql.connect()
    c = conn.cursor()
    uid = current_user.id
    q1 = "DELETE FROM listening_user where user_id = %s"
    c.execute(q1, uid)
    conn.commit()
    return listen()
# study plan progress updater and validation


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

@listening.route("/listening/add_paper", methods=['POST'])
def add_paper():
    if request.method == "POST":
        paper_name = request.form['paper_name']
        media_file = request.files['media_file']
        instruct = request.form['instruct']
        level = request.form['l_val']

        filename = secure_filename(media_file.filename)
        media_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        #adding sample data to quiz database tables
        conn = mysql.connect()
        c = conn.cursor()
        query = "INSERT INTO listening_add_paper(paper_name,media_file,instruct,level) VALUES (%s,%s,%s,%s)"
        val = [paper_name ,filename,instruct,level]
        c.execute(query, val)
        conn.commit()
        c.close()

        return addpaper_2()
            
@listening.route("/listening/add_paper_mcq", methods=['POST'])
def add_paper_mcq():

    if request.method == "POST":
        qid = request.form['mqid']
        ques = request.form['mques']
        ans1 = request.form['mans1']
        ans2 = request.form['mans2']
        ans3 = request.form['mans3']
        ans4 = request.form['mans4']
        correct_answer = request.form['mcorrect_answer']

        conn = mysql.connect()
        c = conn.cursor()
        q = "SELECT MAX(paper_id)  FROM listening_add_paper"
        c.execute(q)
        paper_id = c.fetchone()[0]

        query1 = "SELECT qid FROM listening_add_paper_mcq WHERE paper_id = %s"
        c.execute(query1,paper_id)
        chk1 = c.fetchall()

        query2 = "SELECT qid FROM listening_add_paper_ttype WHERE paper_id = %s"
        c.execute(query2,paper_id)
        chk2 = c.fetchall()

        query3 = "SELECT qid FROM listening_add_paper_matching WHERE paper_id = %s"
        c.execute(query3,paper_id)
        chk3 = c.fetchall()

        maxid = [chk1,chk2,chk3]
        if str(qid) in str(maxid):
            warn = "This Question number: "+ str(qid) +" already taken! change Question number"
            previd = max(max(maxid))[0]
            return s_quiz(previd , warn)
            
        else:
            query = "INSERT INTO listening_add_paper_mcq(qid,question,a,b,c,d, corret_answer) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val = [qid, ques,ans1,ans2,ans3,ans4,correct_answer]
            c.execute(query, val)
            conn.commit()
        
            q1 = "ALTER TABLE listening_add_paper_mcq  ADD CONSTRAINT FK_paper_mcq FOREIGN KEY (paper_id) REFERENCES listening_add_paper(paper_id)"
            c.execute(q1)

            q2 = "SELECT MAX(id) from listening_add_paper_mcq"
            c.execute(q2)
            mcqqid = c.fetchone()[0]

            q3 = "UPDATE listening_add_paper_mcq SET paper_id = %s WHERE id = " + str(mcqqid) +";"
            c.execute(q3,paper_id)

            conn.commit()
            c.close()
            warn = ""
            return s_quiz(qid , warn)

@listening.route("/listening/add_paper_multiple", methods=['POST' , 'GET'])
def add_paper_multiple():

    if request.method == "POST":
        qid = request.form['qid']
        ques = request.form['ques']
        ans1 = request.form['ans1']
        ans2 = request.form['ans2']
        ans3 = request.form['ans3']
        ans4 = request.form['ans4']
        ans11 = request.form.get('ans11')
        ans22 = request.form.get('ans22')
        ans33 = request.form.get('ans33')
        ans44 = request.form.get('ans44')

        conn = mysql.connect()
        c = conn.cursor()
        q = "SELECT MAX(paper_id)  FROM listening_add_paper"
        c.execute(q)
        paper_id = c.fetchone()[0]

        
        query1 = "SELECT qid FROM listening_add_paper_mcq WHERE paper_id = %s"
        c.execute(query1,paper_id)
        chk1 = c.fetchall()

        query2 = "SELECT qid FROM listening_add_paper_ttype WHERE paper_id = %s"
        c.execute(query2,paper_id)
        chk2 = c.fetchall()

        query3 = "SELECT qid FROM listening_add_paper_matching WHERE paper_id = %s"
        c.execute(query3,paper_id)
        chk3 = c.fetchall()

        query4 = "SELECT qid FROM listening_add_paper_multiple WHERE paper_id = %s"
        c.execute(query4,paper_id)
        chk4 = c.fetchall()
        

        maxid = [chk1,chk2,chk3,chk4]
        if str(qid) in str(maxid):
            warn = "This Question number: "+ str(qid) +" already taken! change Question number"
            previd = max(max(maxid))[0]
            return s_quiz(previd , warn)
            
        else:
            query = "INSERT INTO listening_add_paper_multiple(qid,question,a,b,c,d,ans_a,ans_b,ans_c,ans_d) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = [qid, ques,ans1,ans2,ans3,ans4,ans11,ans22,ans33,ans44]
            c.execute(query, val)
            conn.commit()
        
            q1 = "ALTER TABLE listening_add_paper_multiple  ADD CONSTRAINT FK_paper_multiple FOREIGN KEY (paper_id) REFERENCES listening_add_paper(paper_id)"
            c.execute(q1)

            q2 = "SELECT MAX(id) from listening_add_paper_multiple"
            c.execute(q2)
            multipleqid = c.fetchone()[0]

            q3 = "UPDATE listening_add_paper_multiple SET paper_id = %s WHERE id = " + str(multipleqid) +";"
            c.execute(q3,paper_id)

            conn.commit()
            c.close()
            warn = ""
            return s_quiz(qid , warn)

@listening.route("/listening/add_paper_t_type", methods=['POST'])
def add_paper_t_type():
    if request.method == "POST": 
        qid = request.form['qid']
        ques = request.form['ques']
        answer = request.form['answer']

        conn = mysql.connect()
        c = conn.cursor()

        q = "SELECT MAX(paper_id)  FROM listening_add_paper"
        c.execute(q)
        paper_id = c.fetchone()[0]

        query1 = "SELECT qid FROM listening_add_paper_mcq WHERE paper_id = %s"
        c.execute(query1,paper_id)
        chk1 = c.fetchall()

        query2 = "SELECT qid FROM listening_add_paper_ttype WHERE paper_id = %s"
        c.execute(query2,paper_id)
        chk2 = c.fetchall()

        query3 = "SELECT qid FROM listening_add_paper_matching WHERE paper_id = %s"
        c.execute(query3,paper_id)
        chk3 = c.fetchall()

        maxid = [chk1,chk2,chk3]
        if str(qid) in str(maxid):
            warn = "This Question number: "+ str(qid) +" already taken! change Question number"
            previd = max(max(maxid))[0]
            return s_quiz(previd , warn)
        else:
            query = "INSERT INTO listening_add_paper_ttype(qid,question,answer) VALUES (%s,%s,%s)"
            val = [qid, ques,answer]
            c.execute(query, val)
            conn.commit()

            q = "ALTER TABLE listening_add_paper_ttype  ADD CONSTRAINT FK_paper_ttype FOREIGN KEY (paper_id) REFERENCES listening_add_paper(paper_id)"
            c.execute(q)
        
            q1 = "SELECT MAX(paper_id)  FROM listening_add_paper"
            c.execute(q1)
            paper_id = c.fetchone()[0]

            q2 = "SELECT MAX(id) from listening_add_paper_ttype"
            c.execute(q2)
            ttypeqid = c.fetchone()[0]

            q3 = "UPDATE listening_add_paper_ttype SET paper_id = %s WHERE id = " + str(ttypeqid) +";"
            c.execute(q3,paper_id)
            conn.commit()
            c.close()
            warn = ""
            return s_quiz(qid , warn)

@listening.route("/listening/add_paper_matching", methods=['POST'])
def add_paper_matching():
    if request.method == "POST":
        qid = request.form['qid']
        ques = request.form['ques']
        answer = request.form['answer']

        conn = mysql.connect()
        c = conn.cursor()
        query = "INSERT INTO listening_add_paper_matching(qid,question,answer) VALUES (%s,%s,%s)"
        val = [qid, ques,answer]
        c.execute(query, val)
        conn.commit()
        
        q = "SELECT MAX(paper_id)  FROM listening_add_paper"
        c.execute(q)
        paper_id = c.fetchone()[0]

        query1 = "SELECT qid FROM listening_add_paper_mcq WHERE paper_id = %s"
        c.execute(query1,paper_id)
        chk1 = c.fetchall()

        query2 = "SELECT qid FROM listening_add_paper_ttype WHERE paper_id = %s"
        c.execute(query2,paper_id)
        chk2 = c.fetchall()

        query3 = "SELECT qid FROM listening_add_paper_matching WHERE paper_id = %s"
        c.execute(query3,paper_id)
        chk3 = c.fetchall()

        maxid = [chk1,chk2,chk3]
        if str(qid) in str(maxid):
            warn = "This Question number: "+ str(qid) +" already taken! change Question number"
            previd = max(max(maxid))[0]
            return s_quiz(previd , warn)
        else:
            q = "ALTER TABLE listening_add_paper_matching ADD CONSTRAINT FK_paper_matching FOREIGN KEY (paper_id) REFERENCES listening_add_paper(paper_id)"
            c.execute(q)
        
            q1 = "SELECT MAX(paper_id)  FROM listening_add_paper"
            c.execute(q1)
            paper_id = c.fetchone()[0]

            q2 = "SELECT MAX(id) from listening_add_paper_matching"
            c.execute(q2)
            matchqid = c.fetchone()[0]

            q3 = "UPDATE listening_add_paper_matching SET paper_id = %s WHERE id = " + str(matchqid) +";"
            c.execute(q3,paper_id)
            conn.commit()
            c.close()
            warn = ""
            return s_quiz(qid , warn)


@listening.route("/listening/display_quiz/<int:paper_id>", methods=['GET', 'POST'])
def display_quiz(paper_id):
    sid = str(paper_id)
    conn = mysql.connect()
    c = conn.cursor()
    query1 = "SELECT * FROM listening_add_paper_mcq  WHERE paper_id = %s"
    c.execute(query1,sid)
    mcq = c.fetchall()
    mcq_ans = len(mcq)

    query2 = "SELECT * FROM listening_add_paper_ttype  WHERE paper_id = %s"
    c.execute(query2,sid)
    ttype = c.fetchall()
    ttype_ans = len(ttype)

    query3 = "SELECT * FROM listening_add_paper_matching WHERE paper_id = %s"
    c.execute(query3,sid)
    matching = c.fetchall()
    match_ans = len(matching)

    query4 = "SELECT * FROM listening_add_paper_multiple  WHERE paper_id = %s"
    c.execute(query4,sid)
    multiple = c.fetchall()
    multiple_ans = len(multiple)

    query5 = "SELECT * FROM listening_add_paper WHERE paper_id = %s"
    c.execute(query5,sid)
    res = c.fetchall()
    return render_template('/listening/quiz/display_quiz.html',multiple = multiple, multiple_ans = multiple_ans ,ttype_ans = ttype_ans ,match_ans=match_ans,mcq_ans = mcq_ans ,mcq = mcq ,matching = matching , ttype = ttype , res = res)

@listening.route("/listening/available_quiz")
def available_quiz():
    conn = mysql.connect()
    c = conn.cursor()
    query1 = "SELECT * FROM listening_add_paper WHERE level = 1"
    c.execute(query1)
    papers1 =  c.fetchall()
    query2 = "SELECT * FROM listening_add_paper WHERE level = 2"
    c.execute(query2)
    papers2 =  c.fetchall()
    query3 = "SELECT * FROM listening_add_paper WHERE level = 3"
    c.execute(query3)
    papers3 =  c.fetchall()
    query4 = "SELECT * FROM listening_add_paper WHERE level = 4"
    c.execute(query4)
    papers4 =  c.fetchall()
    papers = [papers1,papers2,papers3,papers4]
    return papers

#@listening.route("/listening/show_users")
#def show_users():

@listening.route("/listening/save_paper")
def save_paper():
    flash('successfully added')
    return addpaper_1()

# home link    
@listening.route("/listening/go_home")
def load_home():
    return listen()


# Practise papers,test papers,lessons routes

@listening.route("/listening/addpaper_2_1/<int:qid>/<string:warn>")
def s_quiz(qid,warn):
    return render_template('/listening/quiz/addpaper_2_1.html' , qid = qid , warn = warn)

@listening.route("/listening/addpaper_1")
def addpaper_1():
    return render_template('/listening/quiz/addpaper_1.html')

def addpaper_2():
    return render_template('/listening/quiz/addpaper_2.html')

@listening.route("/listening/lesson1")
def lesson1():
    return render_template('/listening/improvment_plan_papers/lesson1.html')


@listening.route("/listening/lesson2")
def lesson2():
    return render_template('/listening/improvment_plan_papers/lesson2.html')


@listening.route("/listening/lesson3")
def lesson3():
    return render_template('/listening/improvment_plan_papers/lesson3.html')


@listening.route("/listening/plan1_1")
def plan1_1():
    return render_template('/listening/improvment_plan_papers/plan1.1.html')


@listening.route("/listening/plan1_2")
def plan1_2():
    return render_template('/listening/improvment_plan_papers/plan1.2.html')


@listening.route("/listening/plan1_3")
def plan1_3():
    return render_template('/listening/improvment_plan_papers/plan1.3.html')


@listening.route("/listening/plan1_4")
def plan1_4():
    return render_template('/listening/improvment_plan_papers/plan1.4.html')


@listening.route("/listening/plan1_5")
def plan1_5():
    return render_template('/listening/improvment_plan_papers/plan1.5.html')


@listening.route("/listening/plan2_1")
def plan2_1():
    return render_template('/listening/improvment_plan_papers/plan2.1.html')


@listening.route("/listening/plan2_2")
def plan2_2():
    return render_template('/listening/improvment_plan_papers/plan2.2.html')


@listening.route("/listening/plan2_3")
def plan2_3():
    return render_template('/listening/improvment_plan_papers/plan2.3.html')


@listening.route("/listening/plan2_4")
def plan2_4():
    return render_template('/listening/improvment_plan_papers/plan2.4.html')


@listening.route("/listening/plan2_5")
def plan2_5():
    return render_template('/listening/improvment_plan_papers/plan2.5.html')


@listening.route("/listening/plan3_1")
def plan3_1():
    return render_template('/listening/improvment_plan_papers/plan3.1.html')


@listening.route("/listening/plan3_2")
def plan3_2():
    return render_template('/listening/improvment_plan_papers/plan3.2.html')


@listening.route("/listening/plan3_3")
def plan3_3():
    return render_template('/listening/improvment_plan_papers/plan3.3.html')


@listening.route("/listening/plan3_4")
def plan3_4():
    return render_template('/listening/improvment_plan_papers/plan3.4.html')


@listening.route("/listening/plan3_5")
def plan3_5():
    return render_template('/listening/improvment_plan_papers/plan3.5.html')


@listening.route("/listening/plan4_1")
def plan4_1():
    return render_template('/listening/improvment_plan_papers/plan4.1.html')


@listening.route("/listening/plan4_2")
def plan4_2():
    return render_template('/listening/improvment_plan_papers/plan4.2.html')


@listening.route("/listening/plan4_3")
def plan4_3():
    return render_template('/listening/improvment_plan_papers/plan4.3.html')


@listening.route("/listening/plan4_4")
def plan4_4():
    return render_template('/listening/improvment_plan_papers/plan4.4.html')


@listening.route("/listening/plan4_5")
def plan4_5():
    return render_template('/listening/improvment_plan_papers/plan4.5.html')


@listening.route("/listening/plan5_1")
def plan5_1():
    return render_template('/listening/improvment_plan_papers/plan5.1.html')


@listening.route("/listening/plan5_2")
def plan5_2():
    return render_template('/listening/improvment_plan_papers/plan5.2.html')


@listening.route("/listening/plan5_3")
def plan5_3():
    return render_template('/listening/improvment_plan_papers/plan5.3.html')


@listening.route("/listening/section1_1")
def section1_1():
    return render_template('/listening/improvment_plan_papers/section1.1.html')


@listening.route("/listening/section1_2")
def section1_2():
    return render_template('/listening/improvment_plan_papers/section1.2.html')


@listening.route("/listening/section1_3")
def section1_3():
    return render_template('/listening/improvment_plan_papers/section1.3.html')


@listening.route("/listening/section2_1")
def section2_1():
    return render_template('/listening/improvment_plan_papers/section2.1.html')


@listening.route("/listening/section2_2")
def section2_2():
    return render_template('/listening/improvment_plan_papers/section2.2.html')


@listening.route("/listening/section2_3")
def section2_3():
    return render_template('/listening/improvment_plan_papers/section2.3.html')


@listening.route("/listening/section3_1")
def section3_1():
    return render_template('/listening/improvment_plan_papers/section3.1.html')


@listening.route("/listening/section3_2")
def section3_2():
    return render_template('/listening/improvment_plan_papers/section3.2.html')


@listening.route("/listening/section3_3")
def section3_3():
    return render_template('/listening/improvment_plan_papers/section4.3.html')


@listening.route("/listening/section4_1")
def section4_1():
    return render_template('/listening/improvment_plan_papers/section4.1.html')


@listening.route("/listening/section4_2")
def section4_2():
    return render_template('/listening/improvment_plan_papers/section4.2.html')


@listening.route("/listening/section4_3")
def section4_3():
    return render_template('/listening/improvment_plan_papers/section4.3.html')

@listening.route("/listening/gg")
def gg():
    conn = mysql.connect()
    c = conn.cursor()
    query3 = "SELECT * FROM listening_add_paper"
    c.execute(query3)
    papers =  c.fetchall()
    return str(papers)
