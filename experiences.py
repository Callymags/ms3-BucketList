# Import dependencies
from flask import (
    Blueprint, flash, render_template, redirect, request, url_for)
from bson.objectid import ObjectId

# Import database instance of PyMongo
from database import mongo
