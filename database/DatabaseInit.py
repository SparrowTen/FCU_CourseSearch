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
        
    def insertDegreeDeptData(self, json_file):
        degreeDeptList = json_file
        for degree in degreeDeptList.keys():
            for dept_name in degreeDeptList[degree].keys():
                self.cursor.execute('REPLACE INTO `fcu`.`degree_dept` ('+
                                    '`degree` , ' +
                                    '`dept_name` , ' +
                                    '`dept_id`) ' +
                                    'VALUES (%s, %s, %s);'
                                    , (degree, dept_name, degreeDeptList[degree][dept_name]))
        self.conn.commit()
    
    def insertDeptUnitData(self, json_file):
        deptUnitList = json_file
        for dept_id in deptUnitList.keys():
            for unit_name in deptUnitList[dept_id].keys():
                self.cursor.execute('REPLACE INTO `fcu`.`dept_unit` ('+
                                    '`dept_id` , ' +
                                    '`unit_name` , ' +
                                    '`unit_id`) ' +
                                    'VALUES (%s, %s, %s);'
                                    , (dept_id, unit_name, deptUnitList[dept_id][unit_name]))
        self.conn.commit()
    
    def insertUnitClassData(self, json_file):
        unitClassList = json_file
        for unit_id in unitClassList.keys():
            for class_name in unitClassList[unit_id].keys():
                self.cursor.execute('REPLACE INTO `fcu`.`unit_class` ('+
                                    '`unit_id` , ' +
                                    '`cls_name` , ' +
                                    '`cls_id`) ' +
                                    'VALUES (%s, %s, %s);'
                                    , (unit_id, class_name, unitClassList[unit_id][class_name]))
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
                    '`sub_id3` VARCHAR(10) NOT NULL , ' +
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
                    '`std_cls` VARCHAR(7) NOT NULL , ' +
                    '`std_credit` INT NOT NULL , ' +
                    '`curr_id` INT NOT NULL , ' +
                    'PRIMARY KEY (`std_id`)) ENGINE = InnoDB;')
        db.exec(sql)
        sql = (f'CREATE TABLE IF NOT EXISTS `fcu`.`{year}{sms}_curriculum` (' +
                    '`curr_id` INT NOT NULL , ' +
                    '`day` VARCHAR(1) NOT NULL , ' +
                    '`1` TEXT NOT NULL , ' +
                    '`2` TEXT NOT NULL , ' +
                    '`3` TEXT NOT NULL , ' +
                    '`4` TEXT NOT NULL , ' +
                    '`5` TEXT NOT NULL , ' +
                    '`6` TEXT NOT NULL , ' +
                    '`7` TEXT NOT NULL , ' +
                    '`8` TEXT NOT NULL , ' +
                    '`9` TEXT NOT NULL , ' +
                    '`10` TEXT NOT NULL , ' +
                    '`11` TEXT NOT NULL , ' +
                    '`12` TEXT NOT NULL , ' +
                    '`13` TEXT NOT NULL , ' +
                    '`14` TEXT NOT NULL , ' +
                    'PRIMARY KEY (`curr_id`, `day`)) ENGINE = InnoDB;')
        db.exec(sql)
        sql = (f'CREATE TABLE IF NOT EXISTS `fcu`.`{year}{sms}_selected` (' +
                '`std_id` VARCHAR(8) NOT NULL , ' + 
                '`scr_selcode` VARCHAR(8) NOT NULL , ' + 
                '`cls_id` VARCHAR(8) NOT NULL , ' + 
                '`scr_credit` INT NOT NULL , ' + 
                'PRIMARY KEY (`std_id`, `scr_selcode`, `cls_id`)) ENGINE = InnoDB;')
        db.exec(sql)
        db.insertCourseData(year, sms, file)
    
    db.exec('CREATE TABLE IF NOT EXISTS `fcu`.`Account` (' +
            '`std_id` VARCHAR(8) NOT NULL , ' +
            '`pwd` VARCHAR(32) NOT NULL , ' +
            'PRIMARY KEY (`std_id`)) ENGINE = InnoDB;')
    
    dir = os.path.dirname(__file__) + "\\data\\id\\json"
    with open(dir + "\\degree_dept.json", 'r', encoding = 'utf-8') as f:
        file = json.loads(f.read())
    db.exec('CREATE TABLE IF NOT EXISTS `fcu`.`degree_dept` (' +
            '`degree` INT NOT NULL , ' +
            '`dept_id` VARCHAR(2) NOT NULL ,' +
            '`dept_name` TEXT NOT NULL , ' +
            'PRIMARY KEY (`degree`, `dept_id`)) ENGINE = InnoDB;')
    db.insertDegreeDeptData(file)
    
    dir = os.path.dirname(__file__) + "\\data\\id\\json"
    with open(dir + "\\dept_unit.json", 'r', encoding = 'utf-8') as f:
        file = json.loads(f.read())
    db.exec('CREATE TABLE IF NOT EXISTS `fcu`.`dept_unit` (' +
            '`dept_id` VARCHAR(2) NOT NULL , ' +
            '`unit_id` VARCHAR(4) NOT NULL ,' +
            '`unit_name` TEXT NOT NULL , ' +
            'PRIMARY KEY (`dept_id`, `unit_id`)) ENGINE = InnoDB;')
    db.insertDeptUnitData(file)
    
    dir = os.path.dirname(__file__) + "\\data\\id\\json"
    with open(dir + "\\unit_class.json", 'r', encoding = 'utf-8') as f:
        file = json.loads(f.read())
    db.exec('CREATE TABLE IF NOT EXISTS `fcu`.`unit_class` (' +
            '`unit_id` VARCHAR(4) NOT NULL ,' +
            '`cls_id` VARCHAR(7) NOT NULL , ' +
            '`cls_name` TEXT NOT NULL , ' +
            'PRIMARY KEY (`unit_id`, `cls_id`)) ENGINE = InnoDB;')
    db.insertUnitClassData(file)
    
    db.closeDB()