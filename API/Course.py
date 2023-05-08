from flask import Blueprint, request, jsonify, redirect, url_for
from APIDataBase import APIDataBase

Course_blp = Blueprint('Course', __name__)
db = APIDataBase('localhost', 3306, 'root', 'fcu')

# 新增課程
def addCourse(year, sms, std_id, scr_selcode, cls_id, focus = False):
    # 取得原始時間資料和課程名稱
    r = db.execSelect(f"SELECT `sub_name`, `scr_period` FROM {year}{sms}_course WHERE `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
    rawStr = str(r[0]['scr_period'])
    sub_name = r[0]['sub_name']
    
    # 取得星期幾
    dayKeys = ['(一)', '(二)', '(三)', '(四)', '(五)', '(六)', '(日)']
    rawtimeList = []
    for dayKey in dayKeys:
        this_day_count = rawStr.count(dayKey)
        for i in range(0, this_day_count):
            rawtimeList.append(rawStr[rawStr.find(dayKey, i):rawStr.find(dayKey, i) + 8])
    
    # 處理時間資料
    for timeStr in rawtimeList:
        # 取得學生的 curr_id
        r = db.execSelect(f"SELECT `curr_id` FROM {year}{sms}_student WHERE `std_id` = \'{std_id}\'")
        curr_id = r[0]['curr_id']
        
        # 取得星期幾
        day = timeStr[1]
        
        # 取得該星期幾的課表
        r = db.execSelect(f"SELECT * FROM {year}{sms}_curriculum WHERE `curr_id` = \'{curr_id}\' AND `day` = \'{day}\'")
        if r == []:
            db.exec(f"REPLACE INTO {year}{sms}_curriculum (`curr_id`, `day`) VALUES ('{curr_id}', '{day}')")
        timeList = {}
        for i in range(1, 15):
            timeList[i] = r[0][str(i)]
            # timeList.append(r[0][str(i)])
        
        # 取得第幾節
        if '-' in timeStr:
            start_time = timeStr.split(')')[1][0:2]
            end_time = timeStr.split(')')[1][3:5]
            for i in range(int(start_time), int(end_time) + 1):
                if timeList[i] != '' and focus == False:
                    return False
                if focus:
                    timeList[i] = timeList[i] + f" f{sub_name}{scr_selcode}{cls_id}"
                else:
                    timeList[i] = f"{sub_name}{scr_selcode}{cls_id}"
        else:
            time = int(timeStr.split(')')[1][0:2])
            # print(time)
            if timeList[time] != '' and focus == False:
                return False
            if focus:
                timeList[time] = timeList[time] + f" f{sub_name}{scr_selcode}{cls_id}"
            else:
                timeList[time] = f"{sub_name}{scr_selcode}{cls_id}"
    
        dataDict = {}
        # print(timeList)
        for i in range(1, 15):
            if timeList[i] == '':
                dataDict[i] = ''
            else:
                dataDict[i] = timeList[i][0:-1]
        
        # 更新課表
        for i in range(1, 15):
            db.exec(f"UPDATE {year}{sms}_curriculum SET `{i}` = \'{dataDict[i]}\' WHERE `curr_id` = \'{curr_id}\' AND `day` = \'{day}\'")
    
    return True

@Course_blp.route('/add', methods=['GET', 'POST'])
def add():
    year = "111"
    sms = "2"
    std_id = request.values['std_id']
    scr_selcode = request.values['scr_selcode']
    cls_id = request.values['cls_id']
    
    if addCourse(year, sms, std_id, scr_selcode, cls_id):
        return jsonify({'success': '加選成功'})
    else:
        return jsonify({'error': '加選失敗，衝堂'})

@Course_blp.route('/focus', methods=['POST'])
def focus():
    year = "111"
    sms = "2"
    std_id = request.values['std_id']
    scr_selcode = request.values['scr_selcode']
    cls_id = request.values['cls_id']
    if addCourse(year, sms, std_id, scr_selcode, cls_id, focus=True):
        return jsonify({'success': '關注成功'})
    else:
        return jsonify({'error': '關注失敗，衝堂'})
    
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
        # print(currDict)
    return currDict