from flask import render_template,redirect,url_for
from . import main
from ..models import Pitch
from .forms import PitchForm
from flask_login import login_required

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title)

@main.route('/category/<string:category>')
def cat(category):

    '''
    View categories function that returns the pitches of a given category
    '''
#    pitches = get_pitches(category)
    #categories title
    title = 'Categories'

#    pitch = Pitches.get_pitches(pitches.category)

    return render_template('categories.html',title = title)#, pitches=pitches, pitch=pitch)

#submit a pitch view, need to change the unique id
@main.route('/submitpitch/<int:userid>', methods = ['GET','POST'])
@login_required
def new_pitch(userid):
    form = PitchForm()
#pitch id needs a unique number
    pitchid = userid

    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        description = form.description.data
        new_pitch = Pitches(pitchid,title,category,description)
        new_pitch.save_pitches()

    title = 'New Pitch'
    return render_template('new_pitch.html',title = title, pitch_form=form)
