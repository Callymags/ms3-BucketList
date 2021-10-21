# Import dependencies
from flask import (
    Blueprint, flash, render_template, redirect, request, url_for)
from bson.objectid import ObjectId
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
        all_categories = list(mongo.db.categories.find().sort('category_name', 1))
        return render_template(
            'categories.html', 
            all_categories=all_categories)
    else: 
        flash('You need to be an admin to view this page')
        return redirect(url_for('user.log_in'))


@categories.route('/add_category', methods=['GET', 'POST'])
def add_category():
    """
    Allows admin to add new categories for experiences
    """
    if is_admin():
        if request.method == 'POST': 
            # POSTS form data to db
            category = {
                'category_name': request.form.get('category_name')
            }
            mongo.db.categories.insert_one(category)
            flash('Category Successfully Added')
            return redirect(url_for('categories.get_categories'))
        else:
            # GETs the form template
            return render_template('add_category.html')
    else: 
        flash('You need to be an admin to view this page')
        return redirect(url_for('user.log_in'))


@categories.route('/delete_cat/<cat_id>')
def delete_cat(cat_id):
    """
    Allows admin to delete categories for experiences
    """
    if is_admin():
        mongo.db.categories.remove({'_id': ObjectId(cat_id)})
        flash('Category Successfully Deleted')
        return redirect(url_for('categories.get_categories'))
    else: 
        flash('You need to be an admin to view this page')
        return redirect(url_for('user.log_in'))
