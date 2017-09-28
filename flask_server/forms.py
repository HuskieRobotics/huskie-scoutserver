import flask
from wtforms import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class ScoutForm(Form):
    points = IntegerField('points')
