from flask import render_template, Flask
from search import search_blp

app = Flask(__name__)

app.register_blueprint(search_blp, url_prefix = '/')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)