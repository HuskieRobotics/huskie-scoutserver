from flask_wtf import Form
from wtforms import TextField,IntegerField,SubmitField,SelectField

class ContactForm(Form):
    name = TextField("name of student")