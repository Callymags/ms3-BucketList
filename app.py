# Import dependencies
import os
from flask import Flask, render_template

# Import database instance of PyMongo
from database import mongo

# Import user blueprint from user file
from user import user

# Import experience blueprint from experience file
from experience import experience

# Import experience blueprint from experience file
from categories import categories

# Import environment variables only when os can find 
# existing file path for env.py file
if os.path.exists('env.py'):
    import env

# Create instance of Flask that will be stored in app var
app = Flask(__name__)

# Register Blueprints
app.register_blueprint(user)
app.register_blueprint(experience)
app.register_blueprint(categories)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

# Initiate PyMongo instance
mongo.init_app(app)

@app.route('/')
@app.route('/home')
def home():
    """
    Convert cursor object into python list
    Sort experiences by latest experiences added to db
    Limit query to last 8 results in db
    """
    experiences = list(mongo.db.experiences.find().sort("_id", -1).limit(8))
    return render_template('index.html', experiences=experiences)

@app.errorhandler(404)
def page_not_found(e):
    """
    Error handling for 404 error. 
    """
    return render_template('404.html'), 404

@app.errorhandler(405)
def method_not_allowed(e):
    """
    Error handling for 405 error. 
    """
    return render_template('405.html'), 405


@app.errorhandler(500)
def internal_server_error(e):
    """
    Error handling for 500 error. 
    """
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
