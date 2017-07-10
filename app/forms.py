from flask_wtf import Form
from wtforms import StringField, BooleanField,PasswordField,FloatField,SelectField \
                    ,SelectMultipleField,TextAreaField,DecimalField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
