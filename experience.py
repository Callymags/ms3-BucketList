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


@experience.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get("query")
    experiences = list(mongo.db.experiences.find({"$text": {"$search": query}}))
    print(query)
    print(experiences)
    return render_template('search.html', experiences=experiences)