from flask import (
    Blueprint, flash, render_template, redirect, request, session, url_for
)
from werkzeug.security import generate_password_hash, check_password_hash
# Need to render object Id in order to find documents from Mongo DB
from bson.objectid import ObjectId

# Import database instance of PyMongo
from database import mongo

# Create Blueprint to be imported to app.py
auth = Blueprint(
    'auth', __name__, static_folder='static', template_folder='templates'
    )


@auth.route("/register", methods=['GET', 'POST'])
def register():
    # Check if requested method is equal to Post
    if request.method == "POST":
        # Check if username already exists within db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # Display flash message to user if username already exists
        if existing_user:
            flash("Username already exists")
            # Redirect user back to register to try again
            return redirect(url_for("auth.register"))
        
        # Check if email already exists within db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        # Display flash message to user if email already exists
        if existing_email:
            flash("Email already exists")
            # Redirect user back to register to try again
            return redirect(url_for("auth.register"))


        # If no existing user is found
        register = {
            'username': request.form.get("username").lower(),
            'email': request.form.get("email").lower(),
            # Use werkzeug security helpers
            'password': generate_password_hash(request.form.get('password'))
        }
        # Call users collection on MongoDB
        mongo.db.users.insert_one(register)

        # Put the new user into session cookie
        session['user'] = request.form.get('username').lower()
        # Display flash message to user after username is placed into session cookie
        flash('Registration Successful!')
        return redirect(url_for('auth.profile', username=session['user']))
        
    return render_template("register.html")


@auth.route("/log_in", methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST': 
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})

        if existing_user: 
        # Ensure hashed password matches user input 
            if check_password_hash(
                existing_user['password'], request.form.get('password')):
                # Put new user into session cookie
                session['user'] = request.form.get('username').lower()
                flash('Welcome, {}'.format(request.form.get('username')))
                return redirect(url_for(
                    'auth.profile', username=session['user']))
            else: 
                # invalid password 
                flash('Incorrect username and/or password')
                return redirect(url_for('auth.log_in'))
        else:
            # username doesn't exist 
            flash('Incorrect username and/or password')
            return redirect(url_for('auth.log_in'))
    
    return render_template('login.html')


@auth.route("/profile/<username>", methods=['GET', 'POST'])
def profile(username):
    # Grab the session user's username from db
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']
    email = mongo.db.users.find_one(
        {'username': session['user']})['email']
    return render_template('profile.html', username=username, email=email)
