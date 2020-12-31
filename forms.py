from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class XorEncryptionForm(FlaskForm):
    plaintext = StringField('Plain Text',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Encrypt using XOR')

class VignereEncrpytionForm(FlaskForm):
    #plaintext
    plaintext = StringField('Plain Text',
                           validators=[DataRequired(), Length(min=2, max=20)])
    key = StringField('Encrpytion Key',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Encrypt using Vignere')

class CeasarEncrpytion(FlaskForm):
    plaintext = StringField('Plain Text',
                           validators=[DataRequired(), Length(min=2, max=20)])
    key = IntegerField('Key', validators = [DataRequired()])
    submit = SubmitField('Encrypt using Ceasar')
