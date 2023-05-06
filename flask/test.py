# fork from HeiTang/FCU-CourseData
import requests
import json, os, sys,io

SMS = [1, 2, 3, 4]    # 1:上學期 2:下學期 3:暑修上 4:暑修下
DEGREE = [1, 3, 4, 5] # 1:大學部 3:碩士班 4:博士班 5:進修班
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

class CourseDump:
    def __init__(self, year, sms):
        self.headers = {
            "Content-Type":"application/json; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36",
        }

        self.payload = {
            "baseOptions": {
                "lang": "cht",
                "year": year,
                "sms": sms
            }
        }
    def getUnitList(self, degree, dept_id):
        self.payload["unit"] = ""
        url = 'https://coursesearch03.fcu.edu.tw/Service/Search.asmx/GetUnitList'
        r = requests.post(url, headers = self.headers, data = json.dumps(self.payload))
        r = self.stringProcess(r.text)
        unit = json.loads(r)['d']
        return unit

    def getDeptList(self):
        self.payload["degree"] = "1"
        url = 'https://coursesearch03.fcu.edu.tw/Service/Search.asmx/GetDeptList'
        r = requests.post(url, headers = self.headers, data = json.dumps(self.payload))
        r = self.stringProcess(r.text)
        dept = json.loads(r)['d']
        return dept

    def getCourseList(self, degree, dept_id):
        self.payload["typeOptions"] = {
            "degree": degree,
            "deptId": dept_id,
            "unitId": "*",
            "classId": "*"
        }

        url = "https://coursesearch04.fcu.edu.tw/Service/Search.asmx/GetType1Result"
        r = requests.post(url, headers = self.headers, data = json.dumps(self.payload))
        r = self.stringProcess(r.text)
        r = json.loads(r)                                                            # JSON -> dict
        return r

    def saveFile(self, data, path, file_name):
        with open(os.path.join(path, file_name), 'w', encoding='utf-8') as f:
            f.write(data)
            f.flush()
            f.close() 

    def stringProcess(self, string):
        string = string.replace('\\"', '"' )            # 將 \" 過濾成 "
        string = string.replace('\\\"', '"')            # 將 \\" 過濾成 "
        string = string.replace('"d":"{', '"d": {' )   
        string = string.replace('"d":"[{', '"d": [{' )
        string = string.replace(']}"}', ']}}')
        string = string.replace('}]"}', '}]}')
        return string
    
if __name__ == '__main__':
    course = CourseDump(111, 2)
    dept = course.getDeptList()
    print(dept)