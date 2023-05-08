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

@app.route('/index.html')
def reindex():
    return redirect(url_for('index'))

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
    return render_template('result.html',data = r)

@app.route('/result/login.html')
def returnlogin():
    return redirect(url_for('login'))

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/result/register.html')
def returnregister():
    return redirect(url_for('register'))

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/login.html/submit')
def loginsubmit():
    return redirect(url_for('index'))

@app.route('/loginSID',methods=['POST'])
def loginSID():
    SID = request.form['SID']
    return redirect(url_for('index'))

@app.route('/focus',methods=['POST'])
def focus():
    select_id = request.values['select_id']
    cls_id = request.values['cls_id']
    print(select_id + " " + cls_id + " focus")
    return ('',200)

@app.route('/add',methods=['POST'])
def add():
    select_id = request.values['select_id']
    cls_id = request.values['cls_id']
    print(select_id + " " + cls_id + " add")
    return ('',200)

# @app.template_filter('get_focus')
# def get_focus(select_id,cls_id):
#     print(select_id,cls_id)


if __name__ == "__main__":
    app.run(debug=True, port=8000)