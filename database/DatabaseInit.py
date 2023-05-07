import json
import os
import pymysql

class DatabaseInit:
    def __init__(self):
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
    
    def exec(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
    
    def insertCourseData(self, year, sms, json_file):
        courseList = json_file
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
            
            self.cursor.execute('REPLACE INTO `fcu`.`' + year + sms + '_course` ('+
                                '`scr_selcode`, `sub_id3`, `sub_name`, `scr_credit`, `scj_scr_mso`, `scr_period`, `scr_precnt`, `scr_acptcnt`, `cls_id`) ' +
                                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
                                , (scr_selcode, sub_id3, sub_name, scr_credit, scj_scr_mso, scr_period, scr_precnt, scr_acptcnt, cls_id))
        self.conn.commit()
    
    def insertClsData(self, json_file):
        clsList = json_file
        for cls in clsList.keys():
            # print(clsList[cls], cls)
            self.cursor.execute('REPLACE INTO `fcu`.`class_id` ('+
                                '`cls_id`, `cls_name`) ' +
                                'VALUES (%s, %s);'
                                , (clsList[cls], cls))
        self.conn.commit()
    
    def insertDeptData(self, json_file):
        deptList = json_file
        for dept in deptList.keys():
            self.cursor.execute('REPLACE INTO `fcu`.`dept_id` ('+
                                '`dept_id`, `dept_name`) ' +
                                'VALUES (%s, %s);'
                                , (deptList[dept], dept))
        self.conn.commit()
    
    def insertUnitData(self, json_file):
        unitList = json_file
        for unit in unitList.keys():
            # print(unit, unitList[unit])
            self.cursor.execute('REPLACE INTO `fcu`.`unit_id` ('+
                                '`unit_id`, `unit_name`) ' +
                                'VALUES (%s, %s);'
                                , (unitList[unit], unit))
        self.conn.commit()
    
    def closeDB(self):
        self.conn.close()
        
if __name__ == "__main__":
    year = "111"
    dir = os.path.dirname(__file__) + "\\data\\course\\" + year + "\\"
    fileList = os.listdir(dir)
    
    db = DatabaseInit()
    db.connDB()
    
    for file in fileList:
        sms = file[3]
        with open(dir + file, 'r', encoding = 'utf-8') as f:
            file = json.loads(f.read())
        sql = (f'CREATE TABLE IF NOT EXISTS `fcu`.`{year}{sms}_course` (' +
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
        db.exec(sql)
        sql = (f'CREATE TABLE IF NOT EXISTS `fcu`.`{year}{sms}_student` (' +
                    '`std_id` VARCHAR(8) NOT NULL , ' +
                    '`std_name` TEXT NOT NULL , ' +
                    '`std_degree` INT NOT NULL , ' +
                    '`std_dept` VARCHAR(2) NOT NULL , ' +
                    '`std_unit` VARCHAR(4) NOT NULL , ' +
                    '`std_class` VARCHAR(7) NOT NULL , ' +
                    '`curr_id` INT NOT NULL , ' +
                    '`acc_id` INT NOT NULL , ' +
                    'PRIMARY KEY (`std_id`)) ENGINE = InnoDB;')
        db.exec(sql)
        sql = (f'CREATE TABLE IF NOT EXISTS `fcu`.`{year}{sms}_curriculum` (' +
                    '`curr_id` INT NOT NULL , ' +
                    '`mon` TEXT NOT NULL , ' +
                    '`tue` TEXT NOT NULL , ' +
                    '`wed` TEXT NOT NULL , ' +
                    '`thu` TEXT NOT NULL , ' +
                    '`fri` TEXT NOT NULL , ' +
                    '`sat` TEXT NOT NULL , ' +
                    '`sun` TEXT NOT NULL , ' +
                    'PRIMARY KEY (`curr_id`)) ENGINE = InnoDB;')
        db.exec(sql)
        db.insertCourseData(year, sms, file)
    
    
    # dir = os.path.dirname(__file__) + "\\data\\id\\json\\"
    # fileList = os.listdir(dir)

    # for file in fileList:
    #     file_name = file.split('.')[0]
    #     # print(file_name)
    #     with open(dir + file, 'r', encoding = 'utf-8') as f:
    #         file = json.loads(f.read())
    #     if (file_name == 'class_id'):
    #         sql = (f'CREATE TABLE IF NOT EXISTS `fcu`.`{file_name}` (' +
    #                     '`cls_id` VARCHAR(7) NOT NULL , ' +
    #                     '`cls_name` TEXT NOT NULL , ' +
    #                     'PRIMARY KEY (`cls_id`)) ENGINE = InnoDB;')
    #     if (file_name == 'dept_id'):
    #         sql = (f'CREATE TABLE IF NOT EXISTS `fcu`.`{file_name}` (' +
    #                     '`dept_id` VARCHAR(2) NOT NULL , ' +
    #                     '`dept_name` TEXT NOT NULL , ' +
    #                     'PRIMARY KEY (`dept_id`)) ENGINE = InnoDB;')
    #     if (file_name == 'unit_id'):
    #         sql = (f'CREATE TABLE IF NOT EXISTS `fcu`.`{file_name}` (' +
    #                     '`unit_id` VARCHAR(2) NOT NULL , ' +
    #                     '`unit_name` TEXT NOT NULL , ' +
    #                     'PRIMARY KEY (`unit_id`)) ENGINE = InnoDB;')
    #     db.exec(sql)
    #     if (file_name == 'class_id'):
    #         db.insertClsData(file)
    #     if (file_name == 'dept_id'):
    #         db.insertDeptData(file)
    #     if (file_name == 'unit_id'):
    #         db.insertUnitData(file)
    
    db.exec('CREATE TABLE IF NOT EXISTS `fcu`.`Account` (' +
            '`std_id` VARCHAR(8) NOT NULL , ' +
            '`pwd` VARCHAR(32) NOT NULL , ' +
            'PRIMARY KEY (`std_id`)) ENGINE = InnoDB;')
    
    db.closeDB()