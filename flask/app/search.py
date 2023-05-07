from flask import Blueprint, request, render_template, url_for, redirect
import json
import requests

search_blp = Blueprint('search_blp', __name__, template_folder= 'templates')

# 點擊搜尋按鈕
@search_blp.route('/submit', methods=['GET', 'POST'])
def submit():
    print('test')
    if request.method == 'POST':
        Class_id = request.form['Classid']
        return redirect(url_for('search_blp.result', Classid = Class_id))
    else:
        return render_template('index.html')

# 搜尋結果
@search_blp.route('/<Classid>')
def result(Classid):
    r = requests.get(f"http://localhost:5000/API/getCourse?year=111&sms=1&cls_id={Classid}")
    r = json.loads(r.text)
    print(r)
    return render_template('result.html',data = r)

# 從搜尋結果登入視窗
@search_blp.route('/login.html')
def returnlogin():
    return redirect(url_for('login_blp.login'))

# 從搜尋結果註冊視窗
@search_blp.route('/register.html')
def returnregister():
    return redirect(url_for('login_blp.register'))