from flask import Blueprint, request, render_template, url_for, redirect
import json
import requests
from flask_cors import CORS,cross_origin

search_blp = Blueprint('search_blp', __name__, template_folder= 'templates')
CORS(search_blp)

# 點擊搜尋按鈕
@search_blp.route('/submit', methods=['GET', 'POST'])
def submit():
    print('test')
    if request.method == 'POST':
        std_cls = request.form['std_cls']
        return redirect(url_for('search_blp.result', Classid = std_cls))
    else:
        return render_template('index.html')

# 搜尋結果
@search_blp.route('/<Classid>')
def result(Classid):
    r = requests.get(f"http://127.0.0.1:5000/API/getCourse?year=111&sms=2&cls_id={Classid}")
    print(r.text)
    r = json.loads(r.text)
    if 'fcu_token' in request.cookies:
        return render_template('result.html',data = r,login = "y")
    else:
        return render_template('result.html',data = r)

# 從搜尋結果登入視窗
@search_blp.route('/login.html')
def returnlogin():
    return redirect(url_for('login_blp.login'))

# 從搜尋結果註冊視窗
@search_blp.route('/register.html')
def returnregister():
    return redirect(url_for('login_blp.register'))

