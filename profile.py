# Import dependencies
from flask import (
    Blueprint, flash, render_template, redirect, request, url_for)
from bson.objectid import ObjectId

# Import database instance of PyMongo
from database import mongo

# Create Blueprint to be imported to app.py
profile = Blueprint(
    'profile', __name__, static_folder='static', template_folder='templates'
    )

@user.route("/profile/<username>", methods=['GET', 'POST'])
def profile(username):
    # Grab the session user's username from db
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']
    return render_template('profile.html', username=username)