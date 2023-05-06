from flask import Flask,render_template

@app.route('/')
def index():
    return render_template('index.html')

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"