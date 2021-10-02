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
    # Convert cursor object into python list
    experiences = list(mongo.db.experiences.find())
    return render_template('index.html', experiences=experiences)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
