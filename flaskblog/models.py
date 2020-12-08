from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flaskblog import db, login_manger, app
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin


@login_manger.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=True, default=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')

    post = db.relationship('Post', backref='author', lazy=True)
    writingpaper = db.relationship(
        'Writingpaper', backref='wcreator', lazy=True)
    writinganswer = db.relationship(
        'Writingpaperanswer', backref='wcandidate', lazy=True)
    speaking = db.relationship(
        'Speaking', backref='vspeak', lazy=True)
    speakinganswer = db.relationship(
        'Speakinganswer', backref='speakanswer', lazy=True)
    speakingquestion = db.relationship(
        'Speakingquestion', backref='speakquestion', lazy=True)
    Speakinganswersav = db.relationship(
        'Speakinganswersaved', backref='speakinganswersaved', lazy=True)
    quiz = db.relationship(
        'Quiz', backref='quiz', lazy=True)
    create_quiz = db.relationship(
        'Create_quiz', backref='createquiz', lazy=True)
    quiz_answer = db.relationship(
        'Quiz_answer', backref='quizanswer', lazy=True)
    confirm_quiz_answer = db.relationship(
        'Confirm_quiz_answer', backref='quizanswersaved', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


class Writingpaper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), unique=True, nullable=False)
    task01 = db.Column(db.String(1000), nullable=False)
    task01_img = db.Column(db.String(20), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    answer = db.relationship(
        'Writingpaperanswer', backref='candidate', lazy=True)

    def __repr__(self):
        return f"Writingpaper('{self.id}','{self.title}')"


class Writingpaperanswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey(
        'writingpaper.id'), nullable=False)
    task = db.Column(db.Text(1000), nullable=False)
    type = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    grammar = db.Column(db.Integer, nullable=False)
    cohesion = db.Column(db.Integer, nullable=False)
    similarity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Writingpaperanswer('{self.id}','{self.pid}')"


class Speaking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), unique=True, nullable=False)
    question_01 = db.Column(db.String(500), nullable=False)
    question_02 = db.Column(db.String(500), nullable=False)
    question_03 = db.Column(db.String(500), nullable=False)
    question_04 = db.Column(db.String(500), nullable=False)
    question_05 = db.Column(db.String(500), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    speaking = db.relationship(
        'Speakinganswersaved', backref='speaker', lazy=True)

    def __repr__(self):
        return f"Speaking('{self.id}','{self.user_id}')"


class Speakingquestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), unique=True, nullable=False)
    question_01 = db.Column(db.String(500), nullable=False)
    question_02 = db.Column(db.String(500), nullable=False)
    question_03 = db.Column(db.String(500), nullable=False)
    question_04 = db.Column(db.String(500), nullable=False)
    question_05 = db.Column(db.String(500), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Speakingquestion('{self.id}','{self.user_id}')"


class Speakinganswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, nullable=True)
    answer01 = db.Column(db.String(500), nullable=True)
    answer02 = db.Column(db.String(500), nullable=True)
    answer03 = db.Column(db.String(500), nullable=True)
    answer04 = db.Column(db.String(500), nullable=True)
    answer05 = db.Column(db.String(500), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Speakinganswer('{self.id}','{self.user_id}','{self.date_posted}')"


class Speakinganswersaved(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey('speaking.id'), nullable=True)
    answer01 = db.Column(db.String(500), nullable=False)
    cohesion_01 = db.Column(db.Integer, nullable=True)
    grammar_01 = db.Column(db.Integer, nullable=True)
    answer02 = db.Column(db.String(500), nullable=False)
    cohesion_02 = db.Column(db.Integer, nullable=True)
    grammar_02 = db.Column(db.Integer, nullable=True)
    answer03 = db.Column(db.String(500), nullable=False)
    cohesion_03 = db.Column(db.Integer, nullable=True)
    grammar_03 = db.Column(db.Integer, nullable=True)
    answer04 = db.Column(db.String(500), nullable=False)
    cohesion_04 = db.Column(db.Integer, nullable=True)
    grammar_04 = db.Column(db.Integer, nullable=True)
    answer05 = db.Column(db.String(500), nullable=False)
    cohesion_05 = db.Column(db.Integer, nullable=True)
    grammar_05 = db.Column(db.Integer, nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Speakinganswersaved('{self.id}','{self.user_id}','{self.date_posted}')"


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    toq = db.Column(db.String(50), nullable=False)
    gandco = db.Column(db.String(50), nullable=False)
    userbased = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())

    create_quiz = db.relationship(
        'Create_quiz', backref='qcreatequiz', lazy=True)
    quiz_answer = db.relationship(
        'Quiz_answer', backref='qanswer', lazy=True)
    confirm_quiz_answer = db.relationship(
        'Confirm_quiz_answer', backref='qanswersaved', lazy=True)

    def __repr__(self):
        return f"Quiz('{self.id}','{self.name}','{self.toq}')"


class Create_quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), unique=True, nullable=False)
    question = db.Column(db.String(1000), nullable=False)
    toq = db.Column(db.String(50), nullable=False)
    answer01 = db.Column(db.String(100), nullable=False)
    answer02 = db.Column(db.String(100), nullable=False)
    answer03 = db.Column(db.String(100), nullable=False)
    answer04 = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)
    index_no = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Quiz_check('{self.id}','{self.title}','{self.quiz_id}')"


class Quiz_answers_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texts = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Quiz_answers_type('{self.id}','{self.texts}')"


class Quiz_answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer1 = db.Column(db.String(1000), nullable=True)
    answer2 = db.Column(db.String(1000), nullable=True)
    answer3 = db.Column(db.String(1000), nullable=True)
    answer4 = db.Column(db.String(1000), nullable=True)
    answer5 = db.Column(db.String(1000), nullable=True)
    answer6 = db.Column(db.String(1000), nullable=True)
    answer7 = db.Column(db.String(1000), nullable=True)
    answer8 = db.Column(db.String(1000), nullable=True)
    answer9 = db.Column(db.String(1000), nullable=True)
    answer10 = db.Column(db.String(1000), nullable=True)
    answer11 = db.Column(db.String(1000), nullable=True)
    answer12 = db.Column(db.String(1000), nullable=True)
    answer13 = db.Column(db.String(1000), nullable=True)
    answer14 = db.Column(db.String(1000), nullable=True)
    answer15 = db.Column(db.String(1000), nullable=True)
    answer16 = db.Column(db.String(1000), nullable=True)
    answer17 = db.Column(db.String(1000), nullable=True)
    answer18 = db.Column(db.String(1000), nullable=True)
    answer19 = db.Column(db.String(1000), nullable=True)
    answer20 = db.Column(db.String(1000), nullable=True)
    answer21 = db.Column(db.String(1000), nullable=True)
    answer22 = db.Column(db.String(1000), nullable=True)
    answer23 = db.Column(db.String(1000), nullable=True)
    answer24 = db.Column(db.String(1000), nullable=True)
    answer25 = db.Column(db.String(1000), nullable=True)
    answer26 = db.Column(db.String(1000), nullable=True)
    answer27 = db.Column(db.String(1000), nullable=True)
    answer28 = db.Column(db.String(1000), nullable=True)
    answer29 = db.Column(db.String(1000), nullable=True)
    answer30 = db.Column(db.String(1000), nullable=True)
    answer31 = db.Column(db.String(1000), nullable=True)
    answer32 = db.Column(db.String(1000), nullable=True)
    answer33 = db.Column(db.String(1000), nullable=True)
    answer34 = db.Column(db.String(1000), nullable=True)
    answer35 = db.Column(db.String(1000), nullable=True)
    answer36 = db.Column(db.String(1000), nullable=True)
    answer37 = db.Column(db.String(1000), nullable=True)
    answer38 = db.Column(db.String(1000), nullable=True)
    answer39 = db.Column(db.String(1000), nullable=True)
    answer40 = db.Column(db.String(1000), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Quiz_answer('{self.id}','{self.quiz_id}','{self.user_id}')"


class Confirm_quiz_answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer1 = db.Column(db.String(1000), nullable=False)
    answer2 = db.Column(db.String(1000), nullable=False)
    answer3 = db.Column(db.String(1000), nullable=False)
    answer4 = db.Column(db.String(1000), nullable=False)
    answer5 = db.Column(db.String(1000), nullable=False)
    answer6 = db.Column(db.String(1000), nullable=False)
    answer7 = db.Column(db.String(1000), nullable=False)
    answer8 = db.Column(db.String(1000), nullable=False)
    answer9 = db.Column(db.String(1000), nullable=False)
    answer10 = db.Column(db.String(1000), nullable=False)
    answer11 = db.Column(db.String(1000), nullable=False)
    answer12 = db.Column(db.String(1000), nullable=False)
    answer13 = db.Column(db.String(1000), nullable=False)
    answer14 = db.Column(db.String(1000), nullable=False)
    answer15 = db.Column(db.String(1000), nullable=False)
    answer16 = db.Column(db.String(1000), nullable=False)
    answer17 = db.Column(db.String(1000), nullable=False)
    answer18 = db.Column(db.String(1000), nullable=False)
    answer19 = db.Column(db.String(1000), nullable=False)
    answer20 = db.Column(db.String(1000), nullable=False)
    answer21 = db.Column(db.String(1000), nullable=False)
    answer22 = db.Column(db.String(1000), nullable=False)
    answer23 = db.Column(db.String(1000), nullable=False)
    answer24 = db.Column(db.String(1000), nullable=False)
    answer25 = db.Column(db.String(1000), nullable=False)
    answer26 = db.Column(db.String(1000), nullable=False)
    answer27 = db.Column(db.String(1000), nullable=False)
    answer28 = db.Column(db.String(1000), nullable=False)
    answer29 = db.Column(db.String(1000), nullable=False)
    answer30 = db.Column(db.String(1000), nullable=False)
    answer31 = db.Column(db.String(1000), nullable=False)
    answer32 = db.Column(db.String(1000), nullable=False)
    answer33 = db.Column(db.String(1000), nullable=False)
    answer34 = db.Column(db.String(1000), nullable=False)
    answer35 = db.Column(db.String(1000), nullable=False)
    answer36 = db.Column(db.String(1000), nullable=False)
    answer37 = db.Column(db.String(1000), nullable=False)
    answer38 = db.Column(db.String(1000), nullable=False)
    answer39 = db.Column(db.String(1000), nullable=False)
    answer40 = db.Column(db.String(1000), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"confirm_quiz_answer('{self.id}','{self.quiz_id}','{self.user_id}')"
