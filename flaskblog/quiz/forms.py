from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError,  Length, Regexp, NumberRange
from wtforms.widgets import ListWidget, CheckboxInput
from flaskblog.models import Quiz, Quiz_answers_type


class QuizCreationForm(FlaskForm):
    name = StringField('Question Title', validators=[
        DataRequired(), Length(min=6, max=30)])
    noq = IntegerField('Number of Questions', validators=[
        DataRequired(), NumberRange(min=0, max=40)])
    toq = SelectField(u'Type of Question', choices=[
                      ('writing', 'Writing'), ('reading', 'Reading'), ('listening', 'Listening'), ('speaking', 'Speaking')])
    submit = SubmitField('Submit the Quiz')

    def validate_quiztitle(self, name):
        quiz = Quiz.query.filter_by(name=name.data).first()
        if quiz:
            raise ValidationError(
                'This quiz name it taken please choose a another one')


class QuestionForm(FlaskForm):
    toq = SelectField(u'Type of Question', choices=[
                      ('radio', 'Radio'), ('checklist', 'Check List'), ('short', 'Short Answer')])
    submit = SubmitField('Submit the Quiz')


class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


class QuestionChecklistForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=50)])
    question = TextAreaField('Question', validators=[
        DataRequired(), Length(max=250)])
    answer01 = StringField('Answer 01', validators=[DataRequired()])
    answer02 = StringField('Answer 02', validators=[DataRequired()])
    answer03 = StringField('Answer 03', validators=[DataRequired()])
    answer04 = StringField('Answer 04', validators=[DataRequired()])
    correct_answer = MultiCheckboxField(
        u'Correct Answer', choices=[], coerce=int)

    submit = SubmitField('Submit the Question')


class QuestionRadioForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=50)])
    question = TextAreaField('Question', validators=[
        DataRequired(), Length(max=250)])
    answer01 = StringField('Answer 01', validators=[DataRequired()])
    answer02 = StringField('Answer 02', validators=[DataRequired()])
    answer03 = StringField('Answer 03', validators=[DataRequired()])
    answer04 = StringField('Answer 04', validators=[DataRequired()])
    correct_answer = SelectField(u'Correct Answer', choices=[], coerce=int)
    submit = SubmitField('Submit the Question')


class QuestionShortForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=50)])
    question = TextAreaField('Question', validators=[
        DataRequired(), Length(max=250)])
    correct_answer = StringField('Correct Answer', validators=[DataRequired()])
    submit = SubmitField('Submit the Question')
