# Import dependencies
import os
from flask import Flask

# Import environment variables only when os can find 
# existing file path for env.py file
if os.path.exists('env.py'):
    import env


# Create instance of Flask that will be stored in app var
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            