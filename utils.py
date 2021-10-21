from flask import session
from database import mongo


def is_logged_in():
    return session.get("user")


def is_admin():
    return is_logged_in() == "admin"


def get_exp_paginate(offset=0, per_page=8):
    """
    Sets the parameters for the pagination
    on the experiences page
    """
    # pagination adapted from mozillazg (credited in README)
    experiences = list(mongo.db.experiences.find())
    return experiences[offset: offset + per_page]


def exp_paginate_desc(offset=0, per_page=8):
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
