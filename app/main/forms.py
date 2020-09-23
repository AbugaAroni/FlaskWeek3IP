from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    category = SelectField('Pitch category', choices=[('Motivational', 'Motivational'), ('Famous', 'Famous'), ('Despair', 'Despair')], validators=[Required()])
    description = TextAreaField('Pitch category', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
