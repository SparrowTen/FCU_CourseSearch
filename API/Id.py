from flask import Blueprint, request, jsonify
from APIDataBase import APIDataBase

id_blp = Blueprint('getIdList', __name__)
db = APIDataBase('localhost', 3306, 'root', 'fcu')

@id_blp.route('/getDept', methods=['GET'])
def getDept():
    degree = request.args.get('degree')
    return jsonify(db.execSelect(f"SELECT `dept_id`, `dept_name` FROM `degree_dept` WHERE `degree` = \'{degree}\'"))

@id_blp.route('/getUnit', methods=['GET'])
def getUnit():
    dept_id = request.args.get('dept_id')
    return jsonify(db.execSelect(f"SELECT `unit_id`, `unit_name` FROM `dept_unit` WHERE `dept_id` = \'{dept_id}\'"))

@id_blp.route('/getClass', methods=['GET'])
def getClass():
    unit_id = request.args.get('unit_id')
    return jsonify(db.execSelect(f"SELECT `cls_id`, `cls_name` FROM `unit_class` WHERE `unit_id` = \'{unit_id}\'"))