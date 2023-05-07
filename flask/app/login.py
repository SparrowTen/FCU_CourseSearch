from flask import Blueprint, request, render_template, url_for, redirect, jsonify, flash, make_response
import requests
import json
import time
from user import User

login_blp = Blueprint('login_blp', __name__, template_folder= 'templates')

# 登入視窗
@login_blp.route('/')
def login():
    return render_template('login.html')

# 提交登入資料
@login_blp.route('/submit',methods=['POST'])
def submit():
    # 學號
    std_id = request.form['std_id']
    pwd = request.form['pwd']
    if std_id == None or pwd == None:
        return jsonify({'error': '參數錯誤'})
    if std_id != None and pwd != None:
        r = requests.get(f"http://localhost:5000/API/login/getAccount?std_id={std_id}&pwd={pwd}")
        if r == []:
            # print('無此帳號或密碼錯誤')
            return ('',200)
        else:
            user = User(std_id, pwd)
            res = make_response('login success')
            token = user.generate_token()
            res.set_cookie(key = 'fcu_token', value = token)
            # print('登入成功')
            return res

# 註冊視窗
@login_blp.route('/register')
def register():
    return render_template('register.html')