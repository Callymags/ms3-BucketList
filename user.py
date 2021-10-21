from flask import (
    Blueprint, flash, render_template, redirect, request, session, url_for
)
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from database import mongo
from utils import is_logged_in

# Create Blueprint to be imported to app.py
user = Blueprint(
    'user', __name__, static_folder='static', template_folder='templates'
    )


@user.route("/register", methods=['GET', 'POST'])
def register():
    """
    Posts new user data to the database
    """
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
        register_user = {
            'username': request.form.get("username").lower(),
            'email': request.form.get("email").lower(),
            # Use werkzeug security helpers
            'password': generate_password_hash(request.form.get('password')), 
            'bucket_list': []
        }
        # Call users collection on MongoDB
        mongo.db.users.insert_one(register_user)

        # Put the new user into session cookie
        session['user'] = request.form.get('username').lower()
        flash('Registration Successful!')
        return redirect(url_for('user.profile', username=session['user']))
    else:     
        return render_template("register.html")


@user.route("/log_in", methods=['GET', 'POST'])
def log_in():
    """
    Performs log in validation for user when inputting their log in details
    """
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
    else:
        return render_template('login.html')


@user.route("/profile/<username>/", methods=['GET', 'POST'])
def profile(username):
    """
    Generates the user's profile. Queries the mongo database to find username, 
    email, bucket_list and the experiences the user has created
    """
    # Only queries db if user is logged in
    if is_logged_in():
        username = mongo.db.users.find_one(
            {'username': session['user']})['username']
        email = mongo.db.users.find_one(
            {'username': session['user']})['email']
        experiences = list(mongo.db.experiences.find({'added_by': session['user']}))
        # Queries database to see if experience is in the user's bucket list
        user_bucket_list = mongo.db.users.find_one(
            {"username": session["user"]})["bucket_list"]
        # creates an empty array
        bucket_lists = []

        # Each of the users saved experiences is appended to the empty array.
        # The bucket_lists array allows us to get the experience info needed to generate
        # cards for Bucket List section of profile
        for exp_id in user_bucket_list:
            exp_id = mongo.db.experiences.find_one({"_id": ObjectId(exp_id)})
            bucket_lists.append(exp_id)
        return render_template(
            'profile.html', 
            username=username, 
            email=email,
            experiences=experiences,
            user_bucket_list= user_bucket_list,
            bucket_lists=bucket_lists)
    # Redirects user to log in screen if they are not logged in                          
    else:
        flash("You need to log in to perform this operation")
        return redirect(url_for('user.log_in'))


@user.route("/log_out")
def log_out():
    """
    Removes user's session cookie and redirects them to log in page
    """
    if is_logged_in():
        # Remove user's session cookie
        flash('You are logged out')
        session.pop('user')
        return redirect(url_for('user.log_in'))
    # Redirects user to log in screen if they are not logged in                          
    else:
        flash("You need to log in to perform this operation")
        return redirect(url_for('user.log_in'))


@user.route("/update_password/<username>", methods=['GET', 'POST'])
def change_password(username):
    """
    User can change password by inserting new password into input field.
    This new password will be updated in the database 
    """
    # Only performs action if user is logged in
    if is_logged_in():
        # Supports form data being posted to the database. 
        if request.method == 'POST':
            new_password = generate_password_hash(request.form.get('updated-password'))

            mongo.db.users.update_one(
                {'username': username},
                {'$set': {'password': new_password}}
                )
            flash("Password Updated Successfully")
            return redirect(url_for("user.profile", username=session['user']))
        else:
            # Supports GET request to get change password page
            return render_template(
                "update_password.html", username=username)
    # Redirect user to log in screen if not logged in. 
    else: 
        flash('You need to log in to perform that operation')
        return redirect(url_for('user.log_in'))


@user.route("/delete_profile")
def delete_profile():
    """
    User can delete their profile information from database. 
    """
    # Only performs action if user is logged in
    if is_logged_in():
        mongo.db.users.delete_one({'username': session['user']})
        session.pop('user')
        flash('Profile Successfully Deleted')
        return redirect(url_for("home"))
    # Redirects user to log in screen if they are not logged in
    else:
        flash('You need to log in to perform that operation')
        return redirect(url_for('user.log_in'))
