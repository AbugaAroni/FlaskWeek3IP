from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch, User
from .forms import PitchForm, UpdateProfile
from .. import db
from flask_login import login_required
from flask_login import login_required, current_user

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
        new_pitch = Pitch(pitch_title=title,pitch_category=category,pitch_description=description, user=current_user)
        new_pitch.save_pitch()


        return redirect(url_for('main.profile',uname=current_user.username))

    title = 'New Pitch'
    return render_template('new_pitch.html',title = title, pitch_form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    userid = user.id
    pitches = Pitch.get_userpitch(userid)
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, pitches=pitches)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.update_profile',uname=user.username))

    return render_template('profile/update.html',form =form)
