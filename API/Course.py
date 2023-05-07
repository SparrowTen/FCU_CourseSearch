from flask import Blueprint, request, jsonify
from APIDataBase import APIDataBase

Course_blp = Blueprint('Course', __name__)
db = APIDataBase('localhost', 3306, 'root', 'fcu')

# @Course_blp.route('/add', methods=['POST'])
# def add():
    