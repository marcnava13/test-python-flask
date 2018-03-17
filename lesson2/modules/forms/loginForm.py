from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email field is required'), 
        Email(message='Invalid email addredss')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password field is required')
    ])