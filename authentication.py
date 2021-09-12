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
    return render_template('register.html')
