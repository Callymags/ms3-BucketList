# Import dependencies
import os
from flask import Flask, render_template

# Import database instance of PyMongo
from database import mongo

# Import environment variables only when os can find 
# existing file path for env.py file
if os.path.exists('env.py'):
    import env


# Create instance of Flask that will be stored in app var
app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

# Initiate PyMongo instance
mongo.init_app(app)


@app.route('/')
@app.route('/get_index')
def get_index():
    experiences = mongo.db.experiences.find()
    return render_template('index.html', experiences=experiences)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
