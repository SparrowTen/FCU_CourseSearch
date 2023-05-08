from flask import Blueprint, request, render_template, url_for, redirect, jsonify, flash, make_response
import requests
import json
import time
from user import User

register_blp = Blueprint('register_blp', __name__, template_folder= 'templates')

@register_blp.route('/')
def register():
    return render_template('register.html')

@register_blp.route('/submit',methods=['POST'])
def submit():
    std_id = request.form['std_id']
    std_name = request.form['std_name']
    pwd  = request.form['pwd']
    std_degree  = request.form['std_degree']
    std_dept   = request.form['std_dept']
    std_unit = request.form['std_unit']
    std_cls = request.form['std_cls']
    std_data = {
        "std_id" : std_id,"std_name":std_name,"pwd":pwd,"std_degree":std_degree,
        "std_dept":std_dept,"std_unit":std_unit,"std_cls":std_cls
    }
    r = requests.post(f"http://127.0.0.1:5000/API/Login/createAccount",data = std_data)
    print(r)
    return render_template('login.html')