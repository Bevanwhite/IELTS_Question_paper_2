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
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
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
    quiz_radio_user = db.relationship(
        'Quiz_radio', backref='qradio', lazy=True)
    quiz_check_user = db.relationship(
        'Quiz_check', backref='qcheck', lazy=True)
    quiz_short_user = db.relationship(
        'Quiz_short', backref='qshort', lazy=True)

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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Writingpaperanswer('{self.id}','{self.pid}')"


class Writingimprovementplan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    study_plan = db.Column(db.String(100), nullable=False)
    study_plan_no = db.Column(db.String(30), nullable=False)
    feedback = db.Column(db.String(10000), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Writingimprovementplan('{self.id}','{self.study_plan}')"


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
    noq = db.Column(db.Integer, nullable=False)
    toq = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())

    quiz_radio = db.relationship('Quiz_radio', backref='radio', lazy=True)
    quiz_check = db.relationship('Quiz_check', backref='check', lazy=True)
    quiz_short = db.relationship('Quiz_short', backref='short', lazy=True)

    def __repr__(self):
        return f"Quiz('{self.id}','{self.name}','{self.typeofquestion}')"


class Quiz_radio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), unique=True, nullable=False)
    question = db.Column(db.String(1000), nullable=False)
    answer01 = db.Column(db.String(100), nullable=False)
    answer02 = db.Column(db.String(100), nullable=False)
    answer03 = db.Column(db.String(100), nullable=False)
    answer04 = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Quiz_radio('{self.id}','{self.quiz_id}','{self.user_id}')"


class Quiz_check(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), unique=True, nullable=False)
    question = db.Column(db.String(1000), nullable=False)
    answer01 = db.Column(db.String(100), nullable=False)
    answer02 = db.Column(db.String(100), nullable=False)
    answer03 = db.Column(db.String(100), nullable=False)
    answer04 = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    quiz_check = db.relationship('Quiz_answers', backref='answers', lazy=True)

    def __repr__(self):
        return f"Quiz_check('{self.id}','{self.title}','{self.quiz_id}')"


class Quiz_short(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), unique=True, nullable=False)
    question = db.Column(db.String(1000), nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now())
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Quiz_short('{self.id}','{self.title}','{self.quiz_id}')"


class Quiz_answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey(
        'quiz_check.id'), nullable=False)

    def __repr__(self):
        return f"Quiz_answers('{self.id}','{self.text}','{self.quiz_id}')"


class Quiz_answers_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texts = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Quiz_answers_type('{self.id}','{self.texts}')"
