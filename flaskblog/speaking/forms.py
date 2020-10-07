from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError
from flaskblog.models import Speaking


class SpeakForm(FlaskForm):
    title = StringField('Question Paper Name', validators=[DataRequired()])
    question_01 = TextAreaField('Question 01', validators=[DataRequired()])
    question_02 = TextAreaField('Question 02', validators=[DataRequired()])
    question_03 = TextAreaField('Question 03', validators=[DataRequired()])
    question_04 = TextAreaField('Question 04', validators=[DataRequired()])
    question_05 = TextAreaField('Question 05', validators=[DataRequired()])
    submit = SubmitField('Save the Speaking Paper')

    def validate_title(self, title):
        speak = Speaking.query.filter_by(title=title.data).first()
        if speak:
            raise ValidationError(
                'This title is taken. Please choose a diffrent one')


class RecodingForm(FlaskForm):
    record1 = SubmitField('record your answer')
    record2 = SubmitField('record your answer')
    record3 = SubmitField('record your answer')
    record4 = SubmitField('record your answer')
    record5 = SubmitField('record your answer')
    submit = SubmitField('Save the all the anwsers')
