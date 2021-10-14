# Import dependencies
from flask import (
    Blueprint, flash, render_template, redirect, session, request, url_for)
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId

# Import database instance of PyMongo
from database import mongo


# Create Blueprint to be imported to app.py
experience = Blueprint(
    'experience', __name__, static_folder='static', template_folder='templates'
    )

def get_exp_paginate(offset=0, per_page=8):
    """
    Sets the parameters for the pagination
    on the experiences page
    """
    # pagination adapted from mozillazg (credited in README)
    experiences = list(mongo.db.experiences.find())
    return experiences[offset: offset + per_page]

def get_exp_paginate_desc(offset=0, per_page=8):
    """
    Sets the parameters for the pagination in reverse order
    on the experiences page
    """
    # pagination adapted from mozillazg (credited in README)
    experiences = list(mongo.db.experiences.find().sort("_id", -1))
    return experiences[offset: offset + per_page]

def filter_exp_cat_paginate(category, offset=0, per_page=8):
    """
    Sets the parameters for the pagination
    when filtering the experiences by categories
    """
    if category == "Activity":
        experiences = list(mongo.db.experiences.find({"category_name": "Activity"}))
    elif category == "Event":
        experiences = list(mongo.db.experiences.find({"category_name": "Event"}))
    else:
        experiences = list(mongo.db.experiences.find({"category_name": "Travel"}))
    return experiences[offset: offset + per_page]


@experience.route('/create_exp', methods=["GET", "POST"])
def create_exp():
    if request.method == "POST": 
        experience = {
            "experience_name": request.form.get("experience_name"), 
            "category_name": request.form.get("category_name"),
            "img_address": request.form.get("img_address"),
            "description": request.form.get("description"),
            "added_by": session["user"]
        }
        mongo.db.experiences.insert_one(experience)
        flash("Experience Successfully Added!")
        return redirect(url_for("user.profile", username=session['user']))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("create_experience.html", categories=categories)


@experience.route('/exp_info/<exp_id>')
def exp_info(exp_id):
    info = mongo.db.experiences.find_one({'_id': ObjectId(exp_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("experience_info.html", info=info, categories=categories)

@experience.route("/edit_exp/<exp_id>", methods=['GET', 'POST'])
def edit_exp(exp_id):
    if request.method == "POST": 
        edit = {
            "experience_name": request.form.get("experience_name"), 
            "category_name": request.form.get("category_name"),
            "img_address": request.form.get("img_address"),
            "description": request.form.get("description"),
            "added_by": session["user"]
        }
        mongo.db.experiences.update({'_id': ObjectId(exp_id)}, edit)
        flash("Experience Successfully Updated!")
        return redirect(url_for('experience.exp_info', username=session['user'], exp_id=exp_id))

    experience = mongo.db.experiences.find_one({'_id': ObjectId(exp_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_experience.html", experience=experience, categories=categories)


@experience.route('/delete_exp/<exp_id>')
def delete_exp(exp_id):
    mongo.db.experiences.remove({'_id': ObjectId(exp_id)})
    flash('Experience Successfully Deleted')
    return redirect(url_for("user.profile", username=session['user']))



@experience.route('/get_exp')
def get_exp():
    experiences = list(mongo.db.experiences.find().sort("_id", 1))
    # pagination adapted from mozillazg (credited in README)
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 8
    total = len(experiences)
    pagination_exp = get_exp_paginate(
        offset=page*per_page-per_page, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                    css_framework='bootstrap4')
    return render_template(
        'search.html', experiences=pagination_exp,
        page=page, per_page=per_page, pagination=pagination)

@experience.route('/search', methods=['GET', 'POST'])
def search():
    experiences = list(mongo.db.experiences.find().sort("_id", 1))
    query = request.form.get("query", "")
    results = ""
    if request.method == "POST": 
        results = list(mongo.db.experiences.find({"$text": {"$search": query}}))
        return render_template(
            'search.html', results=results, experiences=experiences)

@experience.route('/filter/<filter_type>/<order>')
def filter(filter_type, order):
    """
    Filter all experiences to show either latest or oldest uploads.
    """

    if order == 'ascending':
        experiences = list(mongo.db.experiences.find().sort(filter_type))
        page, per_page, offset = get_page_args(
            page_parameter='page', per_page_parameter='per_page')
        per_page = 8
        total = len(experiences)
        pagination_exp = get_exp_paginate(
            offset=page*per_page-per_page, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                        css_framework='bootstrap4')
        return render_template(
            'search.html', experiences=pagination_exp,
            page=page, per_page=per_page, pagination=pagination)

    else:
        experiences = list(mongo.db.experiences.find().sort(filter_type))
        page, per_page, offset = get_page_args(
            page_parameter='page', per_page_parameter='per_page')
        per_page = 8
        total = len(experiences)
        pagination_exp = get_exp_paginate_desc(
            offset=page*per_page-per_page, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                        css_framework='bootstrap4')
        return render_template(
            'search.html', experiences=pagination_exp,
            page=page, per_page=per_page, pagination=pagination)
        

@experience.route('/filter/<category>')
def categories(category):
    """
    Filters the experiences by their categories
    and renders them to the search.html template
    """

    # returns a list of all experiences in Activity category
    if category == 'Activity':
        experiences = list(
            mongo.db.experiences.find({"category_name": "Activity"}))

    # returns a list of all experiences in Event category
    elif category == "Event":
        experiences = list(
            mongo.db.experiences.find({"category_name": "Event"}))

    # returns a list of all experiences in Travel category
    else:
        experiences = list(
            mongo.db.experiences.find({"category_name": "Travel"}))

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 8
    total = len(experiences)
    pagination_exp = filter_exp_cat_paginate(
        category, offset=page*per_page-per_page, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, 
        css_framework='bootstrap4')
    return render_template(
        "search.html",
        experiences=pagination_exp,
        page=page,
        per_page=per_page,
        pagination=pagination,
        )
