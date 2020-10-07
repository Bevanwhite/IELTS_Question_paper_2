from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length, Regexp
from flaskblog.models import Writingpaper


class WritingpaperForm(FlaskForm):
    title = StringField('Question Paper Title',
                        validators=[DataRequired()])
    task01 = TextAreaField('Question 01', validators=[DataRequired()])
    task01_img = FileField('Question 01 img', validators=[
                           FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Save the Writing Paper')

    def validate_title(self, title):
        writingpaper = Writingpaper.query.filter_by(title=title.data).first()
        if writingpaper:
            raise ValidationError(
                'This title is taken. Please choose a diffrent one')


class WritingUpdateForm(FlaskForm):
    title = StringField('Question Paper Title',
                        validators=[DataRequired()])
    task01 = TextAreaField('Question 01', validators=[DataRequired()])
    task01_img = FileField('Question 01 img', validators=[
                           FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Save the Writing Paper')


class WritingpaperoneForm(FlaskForm):
    task01_answer = TextAreaField(
        'Answer', validators=[DataRequired(), Length(min=150)])
    submit = SubmitField('Save Your answer')
