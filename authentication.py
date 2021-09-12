from flask import (
    Blueprint, flash, render_template, redirect, request, session, url_for
)
from werkzeug.security import generate_password_hash, check_password_hash

# Import database instance of PyMongo
from database import mongo

@authentication.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')