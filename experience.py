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
