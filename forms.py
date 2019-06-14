from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.widgets import TextArea

class InputForm(FlaskForm):
    textInput = StringField("textInput",widget=TextArea())                #might put validations here
    submit = SubmitField ("Sum my text")


class OutputForm(FlaskForm):
    textOut = StringField("textInput")



