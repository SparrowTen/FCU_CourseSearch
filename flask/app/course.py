from flask import Blueprint, request, render_template, url_for, redirect
from user import User
import requests

course_blp = Blueprint('course_blp', __name__, template_folder= 'templates')

@course_blp.route('/focus',methods=['POST'])
def focus():
    scr_selcode = request.values['scr_selcode']
    cls_id = request.values['cls_id']
    token = request.cookies.get('fcu_token')
    std_id = request.cookies.get('fcu_std_id')
    
    if token == None and std_id == None:
        return ('',200)
    
    user = User(std_id)
    if user.certify_token(token):
        r = requests.post(f"http://localhost:5000/API/focus/add?std_id={std_id}&scr_selcode={scr_selcode}&cls_id={cls_id}")
    
    return ('',200)

@course_blp.route('/add',methods=['POST'])
def add():
    select_id = request.values['select_id']
    cls_id = request.values['cls_id']
    print(select_id + " " + cls_id + " add")
    return ('',200)