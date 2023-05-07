from flask import Blueprint, request, render_template, url_for, redirect

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
    return redirect(url_for('index'))

# 註冊視窗
@login_blp.route('/register')
def register():
    return render_template('register.html')