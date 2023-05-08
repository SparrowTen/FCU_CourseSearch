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
            
            # 匯入課表
            # r = db.execSelect(f"SELECT `curr_id` FROM `{year}{sms}_student` WHERE `std_id` = '{std_id}'")
            # curr_id = r[0]['curr_id']
            # days = ['一', '二', '三', '四', '五', '六', '日']
            # for day in days:
            #     db.exec(f"REPLACE INTO {year}{sms}_curriculum (`curr_id`, `day`) VALUES ('{curr_id}', '{day}')")
            # for day in days:
            #     for i in range(1, 15):
            #         for course in courseList:
            #             scr_selcode = course['scr_selcode']
            #             cls_id = course['cls_id']
            #             r = db.execSelect(f"SELECT `sub_name`, `scr_period` FROM {year}{sms}_course WHERE `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
            #             timeStr = r[0]['scr_period'].split(' ')[0]
            #             sub_name = r[0]['sub_name']
                        
            #             day = timeStr[1]
            #             timeList = [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
                        
            #             if '-' in timeStr:
            #                 start_time = timeStr.split(')')[1][0:2]
            #                 end_time = timeStr.split(')')[1][3:5]
            #                 for i in range(int(start_time), int(end_time) + 1):
            #                     timeList[i - 1] = f"{sub_name} {scr_selcode} {cls_id}"
            #             else:
            #                 time = int(timeStr.split(')')[0:2][1])
            #                 timeList[time] = f"{sub_name} {scr_selcode} {cls_id}"
                        
            #             dataDict = {}
            #             for i in range(0, 14):
            #                 if timeList[i] == None:
            #                     dataDict[i + 1] = ""
            #                 else:
            #                     dataDict[i + 1] = timeList[i][0:-1]
                        
            #             r = db.execSelect(f"SELECT `curr_id` FROM {year}{sms}_student WHERE `std_id` = \'{std_id}\'")
            #             curr_id = r[0]['curr_id']
                        
            #             for i in range(1, 15):
            #                 if dataDict[i] != "":
            #                     db.exec(f"UPDATE {year}{sms}_curriculum SET `{i}` = \'{dataDict[i]}\' WHERE `curr_id` = \'{curr_id}\' AND `day` = \'{day}\'")
                        
    return jsonify({'success': '創建成功'})