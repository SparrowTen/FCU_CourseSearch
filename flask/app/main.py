from flask import render_template, Flask

from search import search_blp
from login import login_blp
from course import course_blp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sparrow10testkey'

app.register_blueprint(search_blp, url_prefix = '/search')
app.register_blueprint(login_blp, url_prefix = '/login')
app.register_blueprint(course_blp, url_prefix = '/course')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)