# Import dependencies
from flask import (
    Blueprint, flash, render_template, redirect, session, request, url_for)
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from database import mongo
from utils import (
    is_logged_in, get_exp_paginate, exp_paginate_desc, filter_exp_cat_paginate,
    is_admin)

# Create Blueprint to be imported to app.py
experience = Blueprint(
    'experience', __name__, static_folder='static', template_folder='templates'
    )


@experience.route('/create_exp', methods=["GET", "POST"])
def create_exp():
    """
    Creates new experience in the database
    """
    # References functions in utils.py file
    if is_logged_in():
        # Post method inserts new experience into database
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
        # Get method to retrieve category choices for dropdown
        else:
            categories = mongo.db.categories.find().sort("category_name", 1)
            return render_template(
                "create_experience.html",
                categories=categories)
    # Redirects user to log in screen if they are not logged in                          
    else:
        flash("You need to log in to perform this operation")
        return redirect(url_for('user.log_in'))


@experience.route('/exp_info/<exp_id>')
def exp_info(exp_id):
    """
    Renders a specific experience card's information 
    """
    # Queries database to see if experience is in the user's bucket list
    if is_logged_in():
        user_bucket_list = mongo.db.users.find_one(
        {"username": session["user"]})["bucket_list"]
        info = mongo.db.experiences.find_one({'_id': ObjectId(exp_id)})
        return render_template(
        "experience_info.html", 
        info=info, 
        user_bucket_list=user_bucket_list)
    # Redirects user to log in screen if they are not logged in                          
    else:
        flash("You need to log in to perform this operation")
        return redirect(url_for('user.log_in'))


@experience.route("/edit_exp/<exp_id>", methods=['GET', 'POST'])
def edit_exp(exp_id):
    """
    Allows the admin or the user that created the experience 
    to edit the experience details
    """
    # References functions in utils.py file
    if is_logged_in() or is_admin():
        # Updates the experience with new information
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
            return redirect(url_for('experience.exp_info', 
            username=session['user'], 
            exp_id=exp_id))
        # GET method retrieves expereince data that user can update
        else: 
            experience = mongo.db.experiences.find_one({'_id': ObjectId(exp_id)})
            categories = mongo.db.categories.find().sort("category_name", 1)
            return render_template("edit_experience.html", 
            experience=experience, 
            categories=categories)
    # Redirects user to log in screen if they are not logged in                          
    else:
        flash("You need to log in to perform this operation")
        return redirect(url_for('user.log_in'))


@experience.route('/delete_exp/<exp_id>')
def delete_exp(exp_id):
    """
    Allows an experience to be deleted by the admin or by the user who created the experience. 
    The experience will be removed from all users' bucket lists upon deletion
    """
    # References functions in utils.py file
    if is_logged_in() or is_admin():
        # Removes experience from all users' Bucket Lists
        bucket_lists = list(mongo.db.users.find({'bucket_list': ObjectId(exp_id)}))
        for bucket_list in bucket_lists: 
            mongo.db.users.update_many(
                bucket_list, {'$pull': {'bucket_list': ObjectId(exp_id)}} 
                )
        # Removes experience from database
        mongo.db.experiences.remove({'_id': ObjectId(exp_id)})
        flash('Experience Successfully Deleted')
        return redirect(url_for("user.profile", username=session['user']))
    # Redirects user to log in screen if they are not logged in                          
    else:
        flash("You need to log in to perform this operation")
        return redirect(url_for('user.log_in'))


@experience.route('/get_exp')
def get_exp():
    """
    Retrieves all experiences from database and renders them on the Experiences page
    """
    if is_logged_in():
        experiences = list(mongo.db.experiences.find().sort('_id', 1))
        # Queries database to see if experience is in the user's bucket list
        user_bucket_list = mongo.db.users.find_one(
            {"username": session["user"]})["bucket_list"]
        # pagination adapted from mozillazg (credited in README)
        page, per_page, offset = get_page_args(
            page_parameter='page', per_page_parameter='per_page')
        per_page = 8
        total = len(experiences)
        pagination_exp = get_exp_paginate(offset=page*per_page-per_page, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total, 
            css_framework='bootstrap4')
        return render_template(
            'experiences.html', 
            experiences=pagination_exp,
            page=page, 
            per_page=per_page, 
            pagination=pagination, 
            user_bucket_list=user_bucket_list)
    # Redirects user to log in screen if they are not logged in                          
    else:
        flash("You need to log in to perform this operation")
        return redirect(url_for('user.log_in'))


@experience.route('/search', methods=['GET', 'POST'])
def search():
    """
    Compares search query to experience_name in database
    """
    if is_logged_in():
        # Queries database to see if experience is in the user's bucket list
        user_bucket_list = mongo.db.users.find_one(
            {"username": session["user"]})["bucket_list"]
        query = request.form.get("query", "")
        results = list(mongo.db.experiences.find(
            {"$text": {"$search": query}})) if request.method == "POST" else ""
        return render_template(
            'search.html', 
            results=results, 
            user_bucket_list=user_bucket_list)
    # Redirects user to log in screen if they are not logged in                          
    else:
        flash("You need to log in to perform this operation")
        return redirect(url_for('user.log_in'))


@experience.route('/filter/<filter_type>/<order>')
def filter(filter_type, order):
    """
    Filter all experiences to show either latest or oldest uploads.
    """
    if is_logged_in():
        # Pagination will use different pagination functions depending on the order 
        pagination_fn = get_exp_paginate if order == "ascending" else exp_paginate_desc
        experiences = list(mongo.db.experiences.find().sort(filter_type))
        # Queries database to see if experience is in the user's bucket list
        user_bucket_list = mongo.db.users.find_one(
            {"username": session["user"]})["bucket_list"]
        page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
        per_page = 8
        total = len(experiences)
        pagination_exp = pagination_fn(
            offset=page*per_page-per_page, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                    css_framework='bootstrap4')
        return render_template(
            'experiences.html', 
            experiences=pagination_exp,
            page=page, 
            per_page=per_page, 
            pagination=pagination, 
            user_bucket_list=user_bucket_list)
    # Redirects user to log in screen if they are not logged in                          
    else:
        flash("You need to log in to perform this operation")
        return redirect(url_for('user.log_in'))
       

@experience.route('/filter/<category>')
def categories(category):
    """
    Filters the experiences by their categories
    and renders them to the search.html template
    """
    if is_logged_in():
        # Queries database to see if experience is in the user's bucket list
        user_bucket_list = mongo.db.users.find_one(
            {"username": session["user"]})["bucket_list"]
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
            "experiences.html",
            experiences=pagination_exp,
            page=page,
            per_page=per_page,
            pagination=pagination,
            user_bucket_list=user_bucket_list
            )
    # Redirects user to log in screen if they are not logged in                          
    else:
        flash("You need to log in to perform this operation")
        return redirect(url_for('user.log_in'))


@experience.route("/add_bucket_list/<exp_id>", methods=["GET", "POST"])
def add_bucket_list(exp_id):
    """
    Filters the experience by object Id and pushes 
    the experience id to user's bucket_list array in DB
    """
    if is_logged_in():
        user = mongo.db.users.find_one({"username": session["user"]})
        saved = user['bucket_list']
        # checks if the experience is already in the user's
        # bucket_list array
        if ObjectId(exp_id) in saved:
            flash("Experience Already Saved to Bucket List")
            return redirect(url_for("user.profile", username=session['user']))

        user["bucket_list"].append(ObjectId(exp_id))
        mongo.db.users.update_one({"username": session["user"]},
                        {"$set": {"bucket_list": user["bucket_list"]}})
        flash('Experience Added to Bucket List')
        return redirect(url_for("user.profile", username=session['user']))
    # Redirects user to log in screen if they are not logged in                          
    else:
        flash("You need to log in to perform this operation")
        return redirect(url_for('user.log_in'))


@experience.route("/remove_bucket_list/<exp_id>", methods=["GET", "POST"])
def remove_bucket_list(exp_id):
    """
    Filters the experience by object Id and removes it  
    from the user's bucket_list array
    """
    if is_logged_in():
        user = mongo.db.users.find_one({"username": session["user"]})
        # Remove experience
        user['bucket_list'].remove(ObjectId(exp_id))
        mongo.db.users.update_one(
            {'username': session['user']}, 
            {'$set': {'bucket_list': user['bucket_list']}})
        flash('Experience Removed from Bucket List')
        return redirect(url_for("user.profile", username=session['user']))
    # Redirects user to log in screen if they are not logged in                          
    else:
        flash("You need to log in to perform this operation")
        return redirect(url_for('user.log_in'))
