from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# 定義數據庫連接
db = pymysql.connect(host='localhost', port=3306, user='root', password='', database='fcu')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/fcu'

@app.route('/1112_selected/<string:std_id>', methods=['GET'])
def get_1112_student_by_std_id(std_id):
    query = f"SELECT s.scr_selcode, c.sub_name,s.cls_id FROM 1112_selected s join 1112_course c on s.scr_selcode=c.scr_selcode WHERE s.std_id='{std_id}'"
    cur = db.cursor()
    cur.execute(query)
    # 檢索查詢結果
    course_list = []
    for row in cur.fetchall():
        course = {
            'scr_selcode': row[0],
            'sub_name': row[1],
            'cls_id' : row[2],
        }

        course_list.append(course)
    cur.close()
    db.close()
    # 返回JSON格式數據
    return jsonify(course_list)

if __name__ == '__main__':
    app.run()
    