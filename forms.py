from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField

from wtforms import validators

def length_honeypot (form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('The field must empty')

class CommentForm(Form):
    username =  StringField('Username',
        [ 
            validators.Required(message='Username field is required'),
            validators.length(min=4, max=25, message='Username enter not valid')
        ]
    )
    email = EmailField('Email'
        [
            validators.Required(message='Email field is required')
            validators.Email(message='Email isn\'t valid')
        ]
    )
    comment = TextField('Comment')
    honeypot = HiddenField('', [ length_honeypot ])