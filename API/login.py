from flask import Blueprint, request, jsonify
from APIDataBase import APIDataBase
from flask_cors import CORS

login_blp = Blueprint('login', __name__)
db = APIDataBase('localhost', 3306, 'root', 'fcu')
CORS(login_blp)

@login_blp.route('/getAccount', methods=['GET', 'POST'])
def getAccount():
    if request.method == 'POST':
        std_id = request.values['std_id']
        pwd = request.values['pwd']
        
        if std_id == None and pwd == None:
            return jsonify({'error': '參數錯誤'})
        
        if std_id != None and pwd != None:
            data = db.execSelect(f"SELECT * FROM `Account` WHERE `std_id` = '{std_id}' AND `pwd` = '{pwd}'")
        
        if data == []:
            return jsonify({'error': '查無資料'})
        
        return jsonify(data)

@login_blp.route('/createAccount', methods=['GET', 'POST'])
def createAccount():
    if request.method == 'POST':
        year = "111"
        sms = "2"
        std_id = request.values['std_id']
        pwd = request.values['pwd']
        std_name = request.values['std_name']
        std_degree = request.values['std_degree']
        std_dept = request.values['std_dept']
        std_unit = request.values['std_unit']
        std_cls = request.values['std_cls']

        if std_id == None or pwd == None:
            return jsonify({'error': '參數錯誤'})

        r = db.execSelect(f"SELECT * FROM `account` WHERE `std_id` = '{std_id}'")
        if r != []:
            return jsonify({'error': '此學號已被註冊'})
        
        if std_id != None and pwd != None:
            db.exec(f"REPLACE INTO `account` (`std_id`, `pwd`) VALUES ('{std_id}', '{pwd}')")
            db.exec(f"REPLACE INTO `{year}{sms}_student` (`std_id`, `std_name`, `std_degree`, `std_dept`, `std_unit`, `std_cls`) VALUES ('{std_id}', '{std_name}', '{std_degree}', '{std_dept}', '{std_unit}', '{std_cls}')")
            
            courseList = []
            
            # 匯入必修
            r = db.execSelect(f"SELECT * FROM `{year}{sms}_course` WHERE `cls_id` = '{std_cls}' AND `scj_scr_mso` = \'必修\'")
            for course in r:
                courseList.append(course)
                print
                db.exec(f"REPLACE INTO `{year}{sms}_selected` (`std_id`, `scr_selcode`, `cls_id`, `scr_credit`) VALUES ('{std_id}', '{course['scr_selcode']}', '{course['cls_id']}', '{course['scr_credit']}')")
                
            
    return jsonify({'success': '創建成功'})