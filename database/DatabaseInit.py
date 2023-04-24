import json
import os
import pymysql

class DatabaseInit:
    def __init__(self, json_file):
        self.json_file = json_file
        self.DBconfig = {
            'db': 'fcu',
            'host': 'localhost',
            'port': 3306,
            'user': 'root'
            # 'passwd': 'root'
        }

    def connDB(self):
        self.conn = pymysql.connect(**self.DBconfig)
        self.cursor = self.conn.cursor()
    
    def createTable(self, year, sms):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS `fcu`.`' + year + sms + '_course` (' +
                    '`scr_selcode` VARCHAR(8) NOT NULL , ' +
                    '`sub_id3` VARCHAR(8) NOT NULL , ' +
                    '`sub_name` TEXT NOT NULL , ' +
                    '`scr_credit` INT NOT NULL , ' +
                    '`scj_scr_mso` VARCHAR(2) NOT NULL , ' +
                    '`scr_period` TEXT NOT NULL , ' +
                    '`scr_precnt` INT NOT NULL , ' +
                    '`scr_acptcnt` INT NOT NULL , ' +
                    '`cls_id` VARCHAR(8) NOT NULL , ' +
                    'PRIMARY KEY (`scr_selcode`, `cls_id`)) ENGINE = InnoDB;')
        self.conn.commit()
    
    def insertData(self, year, sms):
        courseList = self.json_file
        # print(courseList['d']['items'])
        # os._exit(0)
        for course in courseList['d']['items']:
            scr_selcode = course['scr_selcode']
            sub_id3 = course['sub_id3']
            sub_name = course['sub_name']
            scr_credit = course['scr_credit']
            scj_scr_mso = course['scj_scr_mso']
            scr_period = course['scr_period']
            scr_precnt = course['scr_precnt']
            scr_acptcnt = course['scr_acptcnt']
            cls_id = course['cls_id']
            
            self.cursor.execute('INSERT INTO `fcu`.`' + year + sms + '_course` ('+
                                '`scr_selcode`, `sub_id3`, `sub_name`, `scr_credit`, `scj_scr_mso`, `scr_period`, `scr_precnt`, `scr_acptcnt`, `cls_id`) ' +
                                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (scr_selcode, sub_id3, sub_name, scr_credit, scj_scr_mso, scr_period, scr_precnt, scr_acptcnt, cls_id))
        self.conn.commit()
        
    def closeDB(self):
        self.conn.close()
        
if __name__ == "__main__":
    year = "111"
    dir = os.path.dirname(__file__) + "\\data\\course\\" + year + "\\"
    fileList = os.listdir(dir)
    for file_name in fileList:
        sms = file_name[3]
        with open(dir + file_name, 'r', encoding = 'utf-8') as f:
            file = json.loads(f.read())
        db = DatabaseInit(file)
        db.connDB()
        db.createTable(year, sms)
        db.insertData(year, sms)
        db.closeDB()