# Senevirathne S.S. - IT17127042
# 1.0
# 20-04-2020

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length, Regexp
from flaskblog.models import Writingpaper

""" Create  and Update functions of ielts academic writing task 1 paper """


class WritingpaperForm(FlaskForm):
    # Create the ielts academic writing task 1 paper with the required fields
    title = StringField('Question Paper Title', validators=[DataRequired()])
    task01 = TextAreaField('Question 01', validators=[DataRequired()])
    task01_img = FileField('Question 01 img', validators=[
                           FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Save the Writing Paper')

    def validate_title(self, title):
        # Validate title field of ielts academic writing task 1 paper
        writingpaper = Writingpaper.query.filter_by(title=title.data).first()
        if writingpaper:
            raise ValidationError(
                'This title is taken. Please choose a diffrent one')


class WritingUpdateForm(FlaskForm):
    # Update the ielts academic writing task 1 paper fields if necessary
    title = StringField('Question Paper Title',
                        validators=[DataRequired()])
    task01 = TextAreaField('Question 01', validators=[DataRequired()])
    task01_img = FileField('Question 01 img', validators=[
                           FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Save the Writing Paper')


class WritingpaperoneForm(FlaskForm):
    # After the candidate giving the answers, the answer will be saved with 150 minimum word
    task01_answer = TextAreaField(
        'Answer', validators=[DataRequired(), Length(min=150)])
    submit = SubmitField('Save Your answer')
