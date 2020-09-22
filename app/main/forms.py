from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    category = TextAreaField('Pitch category', validators=[Required()])
    description = TextAreaField('Pitch description', validators=[Required()])
    submit = SubmitField('Submit')
