from flask import (
    Blueprint, flash, render_template, redirect, request, session, url_for
)
from werkzeug.security import generate_password_hash, check_password_hash
# Need to render object Id in order to find documents from Mongo DB
from bson.objectid import ObjectId

# Import database instance of PyMongo
from database import mongo

# Create Blueprint to be imported to app.py
user = Blueprint(
    'user', __name__, static_folder='static', template_folder='templates'
    )


@user.route("/register", methods=['GET', 'POST'])
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
            return redirect(url_for("user.register"))
        
        # Check if email already exists within db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        # Display flash message to user if email already exists
        if existing_email:
            flash("Email already exists")
            # Redirect user back to register to try again
            return redirect(url_for("user.register"))


        # If no existing user is found
        register = {
            'username': request.form.get("username").lower(),
            'email': request.form.get("email").lower(),
            # Use werkzeug security helpers
            'password': generate_password_hash(request.form.get('password')), 
            'bucket_list': []
        }
        # Call users collection on MongoDB
        mongo.db.users.insert_one(register)

        # Put the new user into session cookie
        session['user'] = request.form.get('username').lower()
        # Display flash message to user after username is placed into session cookie
        flash('Registration Successful!')
        return redirect(url_for('user.profile', username=session['user']))
        
    return render_template("register.html")


@user.route("/log_in", methods=['GET', 'POST'])
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
                    'user.profile', username=session['user']))
            else: 
                # invalid password 
                flash('Incorrect username and/or password')
                return redirect(url_for('user.log_in'))
        else:
            # username doesn't exist 
            flash('Incorrect username and/or password')
            return redirect(url_for('user.log_in'))
    
    return render_template('login.html')

@user.route("/profile/<username>/", methods=['GET', 'POST'])
def profile(username):
    # Grab the session user's username from db
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']
    email = mongo.db.users.find_one(
        {'username': session['user']})['email']
    experiences = list(mongo.db.experiences.find({'added_by': session['user']}))
    saved_exp = mongo.db.users.find_one(
        {'username': session['user']})['bucket_list']

    # creates an empty array
    bucket_lists = []

    # Each of the users saved experiences is appended to the empty array.
    # The bucket_lists array allows us to get the experience info needed to generate 
    # cards for Bucket List section of profile 
    for exp_id in saved_exp:
        exp_id = mongo.db.experiences.find_one({"_id": ObjectId(exp_id)})
        bucket_lists.append(exp_id)

    if session['user']:
        return render_template('profile.html', username=username, email=email,
          experiences=experiences, bucket_lists=bucket_lists)
    else:
        return redirect(url_for('user.log_in'))

@user.route("/log_out")
def log_out():
    # Remove user's session cookie
    flash('You are logged out')
    session.pop('user')
    return redirect(url_for('user.log_in'))

@user.route("/update_password/<username>", methods=['GET', 'POST'])
def change_password(username):  
    user = mongo.db.users.find_one({"username": username})

    if request.method == "GET":
        return render_template(
            "update_password.html", username=username)

    if request.method == 'POST':
        new_password = generate_password_hash(request.form.get('updated-password'))

        mongo.db.users.update_one(
            {'username': username},
            {'$set': {'password': new_password}}
            )
        flash("Password Updated Successfully")
        return redirect(url_for("user.profile", username=session['user']))
    else:
        flash("Passwords Do Not Match")
        return redirect(url_for("user.update_password", username=session['user']))

@user.route("/delete_profile")
def delete_profile():
    mongo.db.users.delete_one({'username': session['user']})
    session.pop('user')
    flash('Profile Successfully Deleted')
    return redirect(url_for("home"))
