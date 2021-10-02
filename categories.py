# Import dependencies
from flask import (
    Blueprint, flash, render_template, session, redirect, request, url_for)
from bson.objectid import ObjectId

# Import database instance of PyMongo
from database import mongo

categories = Blueprint(
    'categories', __name__, static_folder='static', template_folder='templates'
    )

@categories.route('/get_categories')
def get_categories():
    categories= list(mongo.db.categories.find().sort('category_name', 1))
    return render_template('categories.html', categories=categories)