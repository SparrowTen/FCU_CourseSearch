from flask import Blueprint, request, jsonify
from APIDataBase import APIDataBase

from Course import addCourse

login_blp = Blueprint('login', __name__)
db = APIDataBase('localhost', 3306, 'root', 'fcu')

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

        if std_id != None and pwd != None:
            db.exec(f"REPLACE INTO `account` (`std_id`, `pwd`) VALUES ('{std_id}', '{pwd}')")
            db.exec(f"REPLACE INTO `{year}{sms}_student` (`std_id`, `std_name`, `std_degree`, `std_dept`, `std_unit`, `std_cls`, `std_credit`) VALUES ('{std_id}', '{std_name}', '{std_degree}', '{std_dept}', '{std_unit}', '{std_cls}', 0)")
            
            courseList = []
            
            # 初始化課表
            curr_id = db.execSelect(f"SELECT `curr_id` FROM `{year}{sms}_student` WHERE `std_id` = \'{std_id}\'")[0]['curr_id']
            days = ['一', '二', '三', '四', '五', '六', '日']
            for day in days:
                db.exec(f"REPLACE INTO `{year}{sms}_curriculum` (`curr_id`, `day`) VALUES (\'{curr_id}\', \'{day}\')")
            
            # 匯入必修
            r = db.execSelect(f"SELECT * FROM `{year}{sms}_course` WHERE `cls_id` = '{std_cls}' AND `scj_scr_mso` = \'必修\'")
            for course in r:
                # if course not in courseList:
                courseList.append(course)
                db.exec(f"REPLACE INTO `{year}{sms}_selected` (`std_id`, `scr_selcode`, `cls_id`, `scr_credit`) VALUES ('{std_id}', '{course['scr_selcode']}', '{course['cls_id']}', '{course['scr_credit']}')")
                if addCourse(year, sms, std_id, course['scr_selcode'], course['cls_id']) == False:
                    return jsonify({'error': '匯入必修課程失敗'})
                
            # 更新學分數
            r = db.execSelect(f"SELECT SUM(`scr_credit`) AS sum FROM `{year}{sms}_selected` WHERE `std_id` = \'{std_id}\';")
            # print(r[0]['sum'])
            std_credit = r[0]['sum']
            db.exec(f"UPDATE `{year}{sms}_student` SET `std_credit` = \'{std_credit}\' WHERE `std_id` = \'{std_id}\';")
            
    return jsonify({'success': '創建成功'})