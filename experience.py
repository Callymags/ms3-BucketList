# Import dependencies
from flask import (
    Blueprint, flash, render_template, redirect, request, url_for)
from bson.objectid import ObjectId

# Import database instance of PyMongo
from database import mongo


# Create Blueprint to be imported to app.py
experience = Blueprint(
    'experience', __name__, static_folder='static', template_folder='templates'
    )

@experience.route('/create_exp')
def create_exp():
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("create_experience.html", categories=categories)
