from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators
from wtforms.fields import IntegerField, SelectField, BooleanField, DateTimeField, SubmitField

class PersonNewForm(FlaskForm):
    name = StringField("name",[validators.Length(min=3, max=80, message="Skriv in mellan 2 och 80 tecken")])
    