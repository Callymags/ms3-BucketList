from flask import (
    Blueprint, flash, render_template, redirect, request, session, url_for
)
from werkzeug.security import generate_password_hash, check_password_hash

# Import database instance of PyMongo
from database import mongo

# Create Blueprint to be imported to app.py
auth = Blueprint(
    'auth', __name__, static_folder='static', template_folder='templates'
    )



@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Check if username already exists
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})

        # Display flash message to user if username already exists
        if existing_user:
            flash('Username already exists')
            # Redirect user so they can try again
            return redirect(url_for('auth.register'))

        # If no existing user is found
        register = {
            'username': request.form.get('username').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        # Call users collection on MongoDB
        mongo.db.users.insert_one(register)

        # put user into session cookie
        session['user'] = request.form.get('username').lower()
        flash('Registration successful!')

    return render_template('register.html')
