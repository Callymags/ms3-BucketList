# Import dependencies
from flask import (
    Blueprint, flash, render_template, session, redirect, request, url_for)
from bson.objectid import ObjectId

# Import database instance of PyMongo
from database import mongo

from utils import is_admin


categories = Blueprint(
    'categories', __name__, static_folder='static', template_folder='templates'
    )

@categories.route('/get_categories')
def get_categories():
    """
    Queries the database to find all categories in categories collection
    """
    # Will only render page if user is admin
    if is_admin():
        categories = list(mongo.db.categories.find().sort('category_name', 1))
        return render_template('categories.html', categories=categories)
    else: 
        flash('You need to be an admin to view this page')
        return redirect(url_for('user.log_in'))



@categories.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST': 
        category = {
            'category_name': request.form.get('category_name')
        }
        mongo.db.categories.insert_one(category)
        flash('Category Successfully Added')
        return redirect(url_for('categories.get_categories'))

    return render_template('add_category.html')


@categories.route('/delete_cat/<cat_id>')
def delete_cat(cat_id):
    mongo.db.categories.remove({'_id': ObjectId(cat_id)})
    flash('Category Successfully Deleted')
    return redirect(url_for('categories.get_categories'))


@categories.route('/filter/<filter_cat>/')
def filter(filter_cat):
    """
    Filter all experiences to show those related to a certain category.
    """

    experiences = list(mongo.db.experiences.find().sort(filter_cat))
    return render_template('search.html', experiences=experiences)
    