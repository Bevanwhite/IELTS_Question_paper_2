from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, SelectMultipleField, RadioField, HiddenField
from wtforms.validators import DataRequired, ValidationError,  Length, Regexp, NumberRange
from wtforms.widgets import ListWidget, CheckboxInput
from flaskblog.models import Quiz, Quiz_answers_type, Create_quiz
from wtforms.widgets.core import HiddenInput


class QuizCreationForm(FlaskForm):
    name = StringField('Question Title', validators=[
        DataRequired(), Length(min=6, max=30)])
    toq = SelectField(u'Type of Question', choices=[
                      ('writing', 'Writing'), ('reading', 'Reading'), ('listening', 'Listening'), ('speaking', 'Speaking')])
    gandco = SelectField(u'Type of the Paper', choices=[
                         ('none', 'None'), ('grammar', 'Grammar'), ('cohesion', 'Cohesion')])
    userbased = SelectField(u'Type of User Group', choices=[
        ('preliminary', 'Preliminary'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])
    submit = SubmitField('Submit the Quiz')

    def validate_quiztitle(self, name):
        quiz = Quiz.query.filter_by(name=name.data).first()
        if quiz:
            raise ValidationError(
                'This quiz name it taken please choose a another one')


class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


lis = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10"),
       (11, "11"), (12, "12"), (13, "13"), (14, "14"), (15, "15"), (16,
                                                                    "16"), (17, "17"), (18, "18"), (19, "19"), (20, "20"),
       (21, "21"), (22, "22"), (23, "23"), (24, "24"), (25, "25"), (26,
                                                                    "26"), (27, "27"), (28, "28"), (29, "29"), (30, "30"),
       (31, "31"), (32, "32"), (33, "33"), (34, "34"), (35, "35"), (36, "36"), (37, "37"), (38, "38"), (39, "39"), (40, "40")]


class QuestionChecklistForm(FlaskForm):
    quiz_id = HiddenField()
    index_no = SelectField(u'Quiz ID', choices=lis,
                           coerce=int, validate_choice=True)
    title = StringField('Title', validators=[DataRequired(), Length(max=50)])
    question = TextAreaField('Question', validators=[
        DataRequired(), Length(max=1000)])
    answer01 = StringField('Answer 01', validators=[DataRequired()])
    answer02 = StringField('Answer 02', validators=[DataRequired()])
    answer03 = StringField('Answer 03', validators=[DataRequired()])
    answer04 = StringField('Answer 04', validators=[DataRequired()])
    correct_answer = MultiCheckboxField(
        u'Correct Answer', choices=[], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit the Question')

    def validate_title(self, title):
        quiz_check = Create_quiz.query.filter_by(title=title.data).first()
        if quiz_check:
            raise ValidationError(
                'This title is taken. Please choose a diffrent one')

    def validate_index_no(self, index_no):
        quiz = Create_quiz.query.filter_by(
            index_no=index_no.data, quiz_id=self.quiz_id.data).first()
        if quiz:
            raise ValidationError(
                'This pid is taken. Please choose a diffrent one')


class QuestionRadioForm(FlaskForm):
    quiz_id = HiddenField()
    index_no = SelectField(u'Quiz ID', choices=lis,
                           coerce=int, validate_choice=True)
    title = StringField('Title', validators=[DataRequired(), Length(max=50)])
    question = TextAreaField('Question', validators=[
        DataRequired(), Length(max=1000)])
    answer01 = StringField('Answer 01', validators=[DataRequired()])
    answer02 = StringField('Answer 02', validators=[DataRequired()])
    answer03 = StringField('Answer 03', validators=[DataRequired()])
    answer04 = StringField('Answer 04', validators=[DataRequired()])
    correct_answer = SelectField(
        u'Correct Answer', choices=[], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit the Question')

    def validate_title(self, title):
        quiz_check = Create_quiz.query.filter_by(title=title.data).first()
        if quiz_check:
            raise ValidationError(
                'This title is taken. Please choose a diffrent one')

    def validate_index_no(self, index_no):
        quiz = Create_quiz.query.filter_by(
            index_no=index_no.data, quiz_id=self.quiz_id.data).first()
        if quiz:
            raise ValidationError(
                'This pid is taken. Please choose a diffrent one')


class QuestionShortForm(FlaskForm):
    quiz_id = HiddenField()
    index_no = SelectField(u'Quiz ID', choices=lis,
                           coerce=int, validate_choice=True)
    title = StringField('Title', validators=[DataRequired(), Length(max=50)])
    question = TextAreaField('Question', validators=[
        DataRequired(), Length(max=1000)])
    correct_answer = StringField('Correct Answer', validators=[DataRequired()])
    submit = SubmitField('Submit the Question')

    def validate_title(self, title):
        quiz_check = Create_quiz.query.filter_by(title=title.data).first()
        if quiz_check:
            raise ValidationError(
                'This title is taken. Please choose a diffrent one')

    def validate_index_no(self, index_no):
        quiz = Create_quiz.query.filter_by(
            index_no=index_no.data, quiz_id=self.quiz_id.data).first()
        if quiz:
            raise ValidationError(
                'This pid is taken. Please choose a diffrent one')


class UpdateQuestionChecklistForm(FlaskForm):
    quiz_id = HiddenField()
    index_no = HiddenField()
    title = StringField('Title', validators=[DataRequired(), Length(max=50)])
    question = TextAreaField('Question', validators=[
        DataRequired(), Length(max=1000)])
    answer01 = StringField('Answer 01', validators=[DataRequired()])
    answer02 = StringField('Answer 02', validators=[DataRequired()])
    answer03 = StringField('Answer 03', validators=[DataRequired()])
    answer04 = StringField('Answer 04', validators=[DataRequired()])
    correct_answer = MultiCheckboxField(
        u'Correct Answer', choices=[], coerce=int)
    submit = SubmitField('Submit the Question')


class UpdateQuestionRadioForm(FlaskForm):
    quiz_id = HiddenField()
    index_no = HiddenField()
    title = StringField('Title', validators=[DataRequired(), Length(max=50)])
    question = TextAreaField('Question', validators=[
        DataRequired(), Length(max=1000)])
    answer01 = StringField('Answer 01', validators=[DataRequired()])
    answer02 = StringField('Answer 02', validators=[DataRequired()])
    answer03 = StringField('Answer 03', validators=[DataRequired()])
    answer04 = StringField('Answer 04', validators=[DataRequired()])
    correct_answer = SelectField(u'Correct Answer', choices=[], coerce=int)
    submit = SubmitField('Submit the Question')


class UpdateQuestionShortForm(FlaskForm):
    quiz_id = HiddenField()
    index_no = HiddenField()
    title = StringField('Title', validators=[DataRequired(), Length(max=50)])
    question = TextAreaField('Question', validators=[
        DataRequired(), Length(max=1000)])
    correct_answer = StringField('Correct Answer', validators=[DataRequired()])
    submit = SubmitField('Submit the Question')


class ChecklistForm(FlaskForm):
    correct_answer = MultiCheckboxField(
        u'Correct Answer', choices=[], coerce=int)
    submit = SubmitField('Submit the Question')


class RadioForm(FlaskForm):
    correct_answer = RadioField(
        u'Correct Answer', choices=[], coerce=int)
    submit = SubmitField('Submit the Question')


class ShortForm(FlaskForm):
    correct_answer = StringField('Correct Answer', validators=[DataRequired()])
    submit = SubmitField('Submit the Question')


class PreviewForm(FlaskForm):
    previous = SubmitField('Previous')
    next = SubmitField('Next')
