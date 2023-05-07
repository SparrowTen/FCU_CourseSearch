from flask import Blueprint, request, jsonify
from APIDataBase import APIDataBase

getAccount_blp = Blueprint('getAccount', __name__)
db = APIDataBase('localhost', 3306, 'root', 'fcu')

@getAccount_blp.route('/getAccount', methods=['GET', 'POST'])
def getAccount():
    if request.method == 'POST':
        std_id = request.values['std_id']
        email = request.values['email']
        pwd = request.values['pwd']
        
        if std_id == None or email == None and pwd == None:
            return jsonify({'error': '參數錯誤'})
        
        if std_id != None and pwd != None:
            data = db.execSelect(f"SELECT * FROM `Account` WHERE `std_id` = '{std_id}' AND `pwd` = '{pwd}'")
        if email != None and pwd != None:
            data = db.execSelect(f"SELECT * FROM `Account` WHERE `email` = '{email}' AND `pwd` = '{pwd}'")
        
        if data == []:
            return jsonify({'error': '查無資料'})
        
        return jsonify(data)

@getAccount_blp.route('/createAccount', methods=['GET', 'POST'])
def createAccount():
    if request.method == 'POST':
        std_id = request.values['std_id']
        email = request.values['email']
        pwd = request.values['pwd']

        if std_id == None or email == None and pwd == None:
            return jsonify({'error': '參數錯誤'})

        if std_id != None and pwd != None:
            db.execSelect(f"REPLACE INTO `Account` (`std_id`, `email`, `pwd`) VALUES ('{std_id}', '{email}', '{pwd}')")