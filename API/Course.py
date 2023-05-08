from flask import Blueprint, request, jsonify, redirect, url_for
from APIDataBase import APIDataBase

Course_blp = Blueprint('Course', __name__)
db = APIDataBase('localhost', 3306, 'root', 'fcu')

@Course_blp.route('/add', methods=['GET', 'POST'])
def add():
    year = "111"
    sms = "2"
    std_id = request.values['std_id']
    scr_selcode = request.values['scr_selcode']
    cls_id = request.values['cls_id']
    
    r = db.execSelect(f"SELECT `sub_name`, `scr_period` FROM {year}{sms}_course WHERE `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
    timeStr = r[0]['scr_period'].split(' ')[0]
    sub_name = r[0]['sub_name']
    # print(sub_name)
    
    day = timeStr[1]
    timeList = [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    
    if '-' in timeStr:
        start_time = timeStr.split(')')[1][0:2]
        end_time = timeStr.split(')')[1][3:5]
        for i in range(int(start_time), int(end_time) + 1):
            timeList[i - 1] = f"{sub_name} {scr_selcode} {cls_id}"
    else:
        time = timeStr.split(')')[0:2]
        timeList[time - 1] = f"{sub_name} {scr_selcode} {cls_id}"
    
    dataDict = {}
    for i in range(0, 14):
        if timeList[i] == None:
            dataDict[i + 1] = ""
        else:
            dataDict[i + 1] = timeList[i][0:-1]
    
    r = db.execSelect(f"SELECT `curr_id` FROM {year}{sms}_student WHERE `std_id` = \'{std_id}\'")
    curr_id = r[0]['curr_id']
    
    for i in range(1, 15):
        db.exec(f"UPDATE {year}{sms}_curriculum SET `{i}` = \'{dataDict[i]}\' WHERE `curr_id` = \'{curr_id}\' AND `day` = \'{day}\'")
    
    return ('', 200)

@Course_blp.route('/focus', methods=['POST'])
def focus():
    year = "111"
    sms = "2"
    std_id = request.values['std_id']
    scr_selcode = request.values['scr_selcode']
    cls_id = request.values['cls_id']
    
    r = db.execSelect(f"SELECT `sub_name`, `scr_period` FROM {year}{sms}_course WHERE `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
    timeStr = r[0]['scr_period'].split(' ')[0]
    sub_name = r[0]['sub_name']
    
    day = timeStr[1]
    timeList = [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    
    if '-' in timeStr:
        start_time = timeStr.split(')')[1][0:2]
        end_time = timeStr.split(')')[1][3:5]
        for i in range(int(start_time), int(end_time) + 1):
            timeList[i - 1] = f"{sub_name} {scr_selcode} {cls_id}"
    else:
        time = timeStr.split(')')[0:2]
        timeList[time - 1] = f"{sub_name} {scr_selcode} {cls_id}"
    
    dataDict = {}
    focus = "f "
    for i in range(0, 14):
        if timeList[i] == None:
            dataDict[i + 1] = ""
        else:
            dataDict[i + 1] = focus + timeList[i][0:-1]
    
    r = db.execSelect(f"SELECT `curr_id` FROM {year}{sms}_student WHERE `std_id` = \'{std_id}\'")
    curr_id = r[0]['curr_id']
    
    for i in range(1, 15):
        db.exec(f"UPDATE {year}{sms}_curriculum SET `{i}` = \'{dataDict[i]}\' WHERE `curr_id` = \'{curr_id}\' AND `day` = \'{day}\'")
    
    return ('', 200)

@Course_blp.route('/getCurriculum', methods=['POST'])
def getCurriculum():
    year = "111"
    sms = "2"
    std_id = request.values['std_id']
    
    currDict = {
        "學號": std_id
    }
    for i in range(1, 8):
        r = db.execSelect(f"SELECT `curr_id` FROM {year}{sms}_student WHERE `std_id` = \'{std_id}\'")
        curr_id = r[0]['curr_id']
        day = 0
        if i == 1:
            day = "一"
        elif i == 2:
            day = "二"
        elif i == 3:
            day = "三"
        elif i == 4:
            day = "四"
        elif i == 5:
            day = "五"
        elif i == 6:
            day = "六"
        elif i == 7:
            day = "日"
            
        r = db.execSelect(f"SELECT * FROM {year}{sms}_curriculum WHERE `curr_id` = \'{curr_id}\' AND `day` = \'{day}\'")
        # print(r)
        if r == []:
            for i in range(1, 15):
                currDict[day] = ""
                # print("none")
        else:
            dayDict = {}
            for i in range(1, 15):
                dayDict[i] = r[0][f"{i}"]
                
            currDict[day] = dayDict
        print(currDict)
    return currDict