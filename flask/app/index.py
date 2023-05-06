from flask import  request,render_template,flash,abort,url_for,redirect,Flask
import MySQLdb
import sys,io,json
from flask_cors import CORS,cross_origin
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import requests

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        Class_id = request.form['Classid']
        return redirect(url_for('result',Classid = Class_id))
    else:
        return render_template('index.html')
    
@app.route('/result/<Classid>')
def result(Classid):
    r = requests.get(f"http://127.0.0.1:5000/API/?year=111&sms=1&cls_id={Classid}")
    r = json.loads(r.text)
    print(r)
    return render_template('result.html',data = r)
     
# @app.route('/ajax/degree')
# def degree():


if __name__ == "__main__":
    app.run(debug=True, port=8000)