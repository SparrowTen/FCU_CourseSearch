from flask import Blueprint, request, jsonify
from APIDataBase import APIDataBase

getIdList_blp = Blueprint('getIdList', __name__)
db = APIDataBase('localhost', 3306, 'root', 'fcu')

@getIdList_blp.route('/getIdList', methods=['GET'])
def getIdList():
    year = request.args.get('year')
    sms = request.args.get('sms')
    degree = request.args.get('degree')
    dept = request.args.get('dept')
    unit = request.args.get('unit')
    # cls_id = request.args.get('cls_id')
    
    if year == None and sms == None and degree == None and dept == None and unit == None:
        return jsonify({'error': '參數錯誤'})
        
    # dept
    if degree != None and dept == None and unit == None:
        data = db.execSelect('SELECT * FROM `dept_id`')
    
    # unit
    if degree != None and dept != None and unit == None:
        data = db.execSelect('SELECT * FROM `unit_id`')
    
    # cls_id
    if degree != None and dept != None and unit != None:
        data = db.execSelect('SELECT * FROM `cls_id`')
    
    if data == []:
        return jsonify({'error': '查無資料'})
    
    return jsonify(data)