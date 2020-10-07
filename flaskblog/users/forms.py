from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from flask_login import current_user
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[
        DataRequired(), Length(min=5, max=15)])
    lastname = StringField('Last Name', validators=[
        DataRequired(), Length(min=5, max=15)])
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=4, max=50)])
    email = StringField('E-mail Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'This username is taken. Please choose a diffrent one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'This email is taken. Please choose a diffrent one')


class LoginForm(FlaskForm):
    email = StringField('E-mail Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')


class UpdateAccountForm(FlaskForm):
    firstname = StringField('First Name', validators=[
        DataRequired(), Length(min=5, max=15)])
    lastname = StringField('Last Name', validators=[
        DataRequired(), Length(min=5, max=15)])
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=4, max=20)])
    email = StringField('E-mail Address', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_firstname(self, firstname):
        if firstname.data != current_user.firstname:
            user = User.query.filter_by(firstname=firstname.data).first()
            if user:
                raise ValidationError(
                    'This firstname is taken. Please choose a diffrent one')

    def validate_lastname(self, lastname):
        if lastname.data != current_user.lastname:
            user = User.query.filter_by(lastname=lastname.data).first()
            if user:
                raise ValidationError(
                    'This lastname is taken. Please choose a diffrent one')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'This username is taken. Please choose a diffrent one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'This email is taken. Please choose a diffrent one')


class RequestResetForm(FlaskForm):
    email = StringField('E-mail Address', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[
                             DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
