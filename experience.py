# Import dependencies
from flask import (
    Blueprint, flash, render_template, redirect, session, request, url_for)
from bson.objectid import ObjectId

# Import database instance of PyMongo
from database import mongo


# Create Blueprint to be imported to app.py
experience = Blueprint(
    'experience', __name__, static_folder='static', template_folder='templates'
    )

@experience.route('/create_exp', methods=["GET", "POST"])
def create_exp():
    if request.method == "POST": 
        experience = {
            "experience_name": request.form.get("experience_name"), 
            "category_name": request.form.get("category_name"),
            "img_address": request.form.get("img_address"),
            "description": request.form.get("description"),
            "created_by": session["user"]
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

@experience.route('/save_bucketlist/<exp_id>', methods=['GET','POST'])
def save_bucketlist(exp_id):
    if request.method == 'POST': 
        username = mongo.db.users.find_one({'username': session['user']})
        bucketlist = username['bucketlist']

        mongo.db.users.update_one(
            username, 
            {'$push': {'bucketlist': ObjectId(exp_id)}}
        )
        flash('Experience saved to Bucket List')
        return redirect(url_for('experience_info.html', exp_id=experience_id))