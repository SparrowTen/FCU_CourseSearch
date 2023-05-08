from flask import Blueprint, request, jsonify, redirect, url_for
from APIDataBase import APIDataBase
from flask_cors import CORS

course_blp = Blueprint('Course', __name__)
db = APIDataBase('localhost', 3306, 'root', 'fcu')
CORS(course_blp)

@course_blp.route('/add', methods=['GET', 'POST'])
def add():
    year = "111"
    sms = "2"
    std_id = request.values['std_id']
    scr_selcode = request.values['scr_selcode']
    cls_id = request.values['cls_id']
    
    # 判斷是否有此課程
    r = db.execSelect(f"SELECT * FROM {year}{sms}_course WHERE `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
    if r == []:
        return jsonify({'error': '課程不存在'})
    
    sub_name = r[0]['sub_name']
    scr_credit = r[0]['scr_credit']
    
    # 取得學分數
    r = db.execSelect(f"SELECT SUM(`scr_credit`) AS sum FROM `{year}{sms}_selected` WHERE `std_id` = \'{std_id}\';")
    std_credit = r[0]['sum']
    
    # 判斷學分數是否超過上限
    if std_credit + scr_credit > 25:
        return jsonify({'error': '學分數超過上限'})
    
    # 判斷是否重名
    r = db.execSelect(f"SELECT * FROM `{year}{sms}_selected` WHERE `std_id` = \'{std_id}\' AND `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
    for cls in r:
        if cls['sub_name'] == sub_name:
            return jsonify({'error': '課程已存在，不得重複加選'})
    
    ## 判斷是否有衝堂
    # 取得已選課程時間
    r = db.execSelect(f"SELECT * FROM `{year}{sms}_selected` WHERE `std_id` = \'{std_id}\'")
    
    selected_currDict = {
        "學號": "",
        "已選學分": "",
        "最高學分": "25",
        "一": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "二": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "三": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "四": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "五": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "六": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "日": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            }
    }
    
    for cls in r:
        scr_selcode = cls['scr_selcode']
        cls_id = cls['cls_id']
        r = db.execSelect(f"SELECT `scr_period` FROM `{year}{sms}_course` WHERE `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
        scr_period = r[0]['scr_period']
        
        # 取得星期幾
        dayKeys = ['(一)', '(二)', '(三)', '(四)', '(五)', '(六)', '(日)']
        rawtimeList = []
        for dayKey in dayKeys:
            this_day_count = scr_period.count(dayKey)
            for i in range(0, this_day_count):
                rawtimeList.append(scr_period[scr_period.find(dayKey, i):scr_period.find(dayKey, i) + 8])
        
        # 處理時間資料
        for timeStr in rawtimeList:
            
            # 取得星期幾
            day = timeStr[1]
            
            # 取得第幾節
            if '-' in timeStr:
                start_time = timeStr.split(')')[1][0:2]
                end_time = timeStr.split(')')[1][3:5]
                for i in range(int(start_time), int(end_time) + 1):
                    selected_currDict[day][i]['add'].append("t")
            else:
                time = int(timeStr.split(')')[1][0:2])
                selected_currDict[day][time]['add'].append("t")
    
    # print(selected_currDict['一'][3]['add'][0])
    
    # 取得加選課程時間
    r = db.execSelect(f"SELECT * FROM {year}{sms}_course WHERE `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
    
    add_currDict = {
        "一": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "二": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "三": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "四": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "五": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "六": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "日": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            }
    }
    
    for cls in r:
        scr_selcode = cls['scr_selcode']
        cls_id = cls['cls_id']
        r = db.execSelect(f"SELECT `scr_period` FROM `{year}{sms}_course` WHERE `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
        scr_period = r[0]['scr_period']
        
        # 取得星期幾
        dayKeys = ['(一)', '(二)', '(三)', '(四)', '(五)', '(六)', '(日)']
        rawtimeList = []
        for dayKey in dayKeys:
            this_day_count = scr_period.count(dayKey)
            for i in range(0, this_day_count):
                rawtimeList.append(scr_period[scr_period.find(dayKey, i):scr_period.find(dayKey, i) + 8])
        
        # 處理時間資料
        for timeStr in rawtimeList:
            
            # 取得星期幾
            day = timeStr[1]
            
            # 取得第幾節
            if '-' in timeStr:
                start_time = timeStr.split(')')[1][0:2]
                end_time = timeStr.split(')')[1][3:5]
                for i in range(int(start_time), int(end_time) + 1):
                    add_currDict[day][i]['add'].append("t")
            else:
                time = int(timeStr.split(')')[1][0:2])
                add_currDict[day][time]['add'].append("t")
    
    # 判斷是否有課程衝堂
    for day in add_currDict:
        for time in range(1, 15):
            if len(add_currDict[day][time]['add']) != 0:
                if len(selected_currDict[day][time]['add']) != 0:
                    return jsonify({'error': '課程衝堂'})
    
    db.exec(f"REPLACE INTO `{year}{sms}_selected` (`std_id`, `scr_selcode`, `cls_id`) VALUES (\'{std_id}\', \'{scr_selcode}\', \'{cls_id}\');")
    
    return jsonify({'success': '加選成功'})

@course_blp.route('/focus', methods=['POST'])
def focus():
    year = "111"
    sms = "2"
    std_id = request.values['std_id']
    scr_selcode = request.values['scr_selcode']
    cls_id = request.values['cls_id']
    
    # 判斷是否有此課程
    r = db.execSelect(f"SELECT * FROM {year}{sms}_course WHERE `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
    if r == []:
        return jsonify({'error': '課程不存在'})
    
    
    # 判斷是否重複關注
    r = db.execSelect(f"SELECT * FROM `{year}{sms}_focused` WHERE `std_id` = \'{std_id}\' AND `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
    for cls in r:
        if cls['scr_selcode'] == scr_selcode and cls['cls_id'] == cls_id:
            return jsonify({'error': '課程已存在，不得重複關注'})
    
    db.exec(f"REPLACE INTO `{year}{sms}_focused` (`std_id`, `scr_selcode`, `cls_id`) VALUES (\'{std_id}\', \'{scr_selcode}\', \'{cls_id}\');")
    
    return jsonify({'success': '關注成功'})

@course_blp.route('/getCurriculum', methods=['GET'])
def getCurriculum():
    year = "111"
    sms = "2"
    std_id = request.args.get('std_id')
    
    # 取學生姓名
    r = db.execSelect(f"SELECT `std_name` FROM `{year}{sms}_student` WHERE `std_id` = \'{std_id}\'")
    std_name = r[0]['std_name']
    
    # 總學分數
    r = db.execSelect(f"SELECT SUM(`scr_credit`) AS sum FROM `{year}{sms}_selected` WHERE `std_id` = \'{std_id}\';")
    std_credit = r[0]['sum']
    
    # 已選課程清單
    r = db.execSelect(f"SELECT * FROM `{year}{sms}_selected` WHERE `std_id` = \'{std_id}\'")
    
    currDict = {
        "學號": "",
        "已選學分": "",
        "最高學分": "25",
        "一": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "二": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "三": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "四": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "五": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "六": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            },
        "日": {
            1: {
                "add": [],
                "focus": []
                },
            2: {
                "add": [],
                "focus": []
                },
            3: {
                "add": [],
                "focus": []
                },
            4: {
                "add": [],
                "focus": []
                },
            5: {
                "add": [],
                "focus": []
                },
            6: {
                "add": [],
                "focus": []
                },
            7: {
                "add": [],
                "focus": []
                },
            8: {
                "add": [],
                "focus": []
                },
            9: {
                "add": [],
                "focus": []
                },
            10: {
                "add": [],
                "focus": []
                },
            11: {
                "add": [],
                "focus": []
                },
            12: {
                "add": [],
                "focus": []
                },
            13: {
                "add": [],
                "focus": []
                },
            14: {
                "add": [],
                "focus": []
                }
            }
    }
    currDict["學號"] = std_id
    currDict["姓名"] = std_name
    currDict["已選學分"] = std_credit
    currDict["最高學分"] = "25"
    
    for cls in r:
        scr_selcode = cls['scr_selcode']
        cls_id = cls['cls_id']
        r = db.execSelect(f"SELECT * FROM `{year}{sms}_course` WHERE `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
        classData = r[0]
        scr_period = r[0]['scr_period']
        
        # 取得星期幾
        dayKeys = ['(一)', '(二)', '(三)', '(四)', '(五)', '(六)', '(日)']
        rawtimeList = []
        for dayKey in dayKeys:
            this_day_count = scr_period.count(dayKey)
            for i in range(0, this_day_count):
                rawtimeList.append(scr_period[scr_period.find(dayKey, i):scr_period.find(dayKey, i) + 8])
        
        # 處理時間資料
        for timeStr in rawtimeList:
            
            # 取得星期幾
            day = timeStr[1]
            
            # 取得第幾節
            if '-' in timeStr:
                start_time = timeStr.split(')')[1][0:2]
                end_time = timeStr.split(')')[1][3:5]
                for i in range(int(start_time), int(end_time) + 1):
                    if len(currDict[day][i]['add']) == 0:
                        currDict[day][i]['add'].append(classData)
                    # currDict[day][i]['add'].append(cls)
            else:
                time = int(timeStr.split(')')[1][0:2])
                if len(currDict[day][time]['add']) == 0:
                    currDict[day][time]['add'].append(classData)
                # currDict[day][time]['add'].append(cls)
    
    # 關注課程清單
    r = db.execSelect(f"SELECT * FROM `{year}{sms}_focused` WHERE `std_id` = \'{std_id}\'")
    
    for cls in r:
        scr_selcode = cls['scr_selcode']
        cls_id = cls['cls_id']
        r = db.execSelect(f"SELECT `scr_period` FROM `{year}{sms}_course` WHERE `scr_selcode` = \'{scr_selcode}\' AND `cls_id` = \'{cls_id}\'")
        scr_period = r[0]['scr_period']
        
        # 取得星期幾
        dayKeys = ['(一)', '(二)', '(三)', '(四)', '(五)', '(六)', '(日)']
        rawtimeList = []
        for dayKey in dayKeys:
            this_day_count = scr_period.count(dayKey)
            for i in range(0, this_day_count):
                rawtimeList.append(scr_period[scr_period.find(dayKey, i):scr_period.find(dayKey, i) + 8])
        
        # 處理時間資料
        for timeStr in rawtimeList:
            
            # 取得星期幾
            day = timeStr[1]
            
            # 取得第幾節
            if '-' in timeStr:
                start_time = timeStr.split(')')[1][0:2]
                end_time = timeStr.split(')')[1][3:5]
                for i in range(int(start_time), int(end_time) + 1):
                    currDict[day][i]['focus'].append(classData)
            else:
                time = int(timeStr.split(')')[1][0:2])
                currDict[day][time]['focus'].append(classData)
    
    
    return currDict