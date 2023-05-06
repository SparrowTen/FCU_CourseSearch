from flask import  request,render_template,flash,abort,url_for,redirect,Flask
import MySQLdb
import sys,io
from flask_cors import CORS,cross_origin
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST', 'GET'])
def submit():
     dic = {}
     if request.method == 'POST':
        dic['Degree'] = request.form['Degree']
        dic['College'] = request.form['College']
        return str(dic)
     else:
        return render_template('index.html')
     
# @app.route('/ajax/degree')
# def degree():


if __name__ == "__main__":
    app.run(debug=True, port=8000)