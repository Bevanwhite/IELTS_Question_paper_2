from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError,  Length, Regexp, NumberRange
from flaskblog.models import Quiz


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
