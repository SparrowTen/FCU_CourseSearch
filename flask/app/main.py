from flask import render_template, Flask,request
from flask_cors import CORS,cross_origin
from search import search_blp
from login import login_blp
from course import course_blp
from register import register_blp

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'sparrow10testkey'

app.register_blueprint(search_blp, url_prefix = '/search')
app.register_blueprint(login_blp, url_prefix = '/login')
app.register_blueprint(course_blp, url_prefix = '/course')
app.register_blueprint(register_blp, url_prefix = '/register')

@app.route('/')
def index():
    if 'fcu_token' in request.cookies:
        print("login")
        return render_template('index.html',login = "y")
    else:
        print("logout")
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000,host="0.0.0.0")