from flask import Blueprint, request, render_template, url_for, redirect

course_blp = Blueprint('course_blp', __name__, template_folder= 'templates')

@course_blp.route('/focus',methods=['POST'])
def focus():
    select_id = request.values['select_id']
    cls_id = request.values['cls_id']
    print(select_id + " " + cls_id + " focus")
    return ('',200)

@course_blp.route('/add',methods=['POST'])
def add():
    select_id = request.values['select_id']
    cls_id = request.values['cls_id']
    print(select_id + " " + cls_id + " add")
    return ('',200)