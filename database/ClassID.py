# fork from HeiTang/FCU-ClassID

import requests
import os
import json
import pandas as pd

def GetDeptList(Dept_data,degree):
    payload = {
        "baseOptions":{
            "lang":"cht",
            "year":108,
            "sms":2
        },
        "degree":degree
    }
    payload = json.dumps(payload)
    url = "https://coursesearch04.fcu.edu.tw/Service/Search.asmx/GetDeptList"
    r = Post(url,payload)

    i = 0
    while(True):   
        try:
            seq = r['d'][i]['name']
            value = r['d'][i]['id']
            Dept_data.setdefault(seq,value)
            i=i+1
        except:
            return Dept_data
    
def GetUnitList(Unit_data,degree,deptId):
    payload = {
        "baseOptions":{
            "lang":"cht",
            "year":108,
            "sms":2
        },
        "degree":degree,
        "deptId":deptId
    }

    payload = json.dumps(payload)
    url = "https://coursesearch04.fcu.edu.tw/Service/Search.asmx/GetUnitList"
    r = Post(url,payload)
    # print(r)
    
    i = 0
    this_dept = {}
    while(True):
        try:
            dept_id = deptId
            # print(r['d'][i]['name'])
            # print(r['d'][i]['id'])
            seq = r['d'][i]['name']
            value = r['d'][i]['id']
            Unit_data.setdefault(seq,value)
            # Unit_data[dept_id][seq] = value
            i=i+1
        except:
            # print(Unit_data)
            return Unit_data

def GetClassList(Class_data, degree, unitId):
    payload = {
        "baseOptions":{
            "lang":"cht",
            "year":108,
            "sms":2
        },
        "degree":degree,
        "unitId":unitId
    }

    payload = json.dumps(payload)
    url = "https://coursesearch04.fcu.edu.tw/Service/Search.asmx/GetClassList"
    r = Post(url,payload)

    i = 0
    while(True):   
        try:
            seq = r['d'][i]['name']
            value = r['d'][i]['id']
            Class_data.setdefault(seq,value)
            i=i+1
        except:
            return Class_data

def Post(url,payload):

    headers = {
        "Accept": "*/*",
        "Accept-Language": 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
        "DNT": "1",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Content-Type":"application/json; charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36",
    }

    r = requests.post(url,headers=headers,data = payload)  
    r = r.text                                             
    r = r.replace('\\"','"' )            # 將 \" 過濾成 "
    r = r.replace('"d":"[{','"d": [{' )   
    r = r.replace('}]"}','}]}')
    r = json.loads(r)    
    return r                                                         

def Show(dict):
    list = dict.keys()
    for i in list:
        print(dict[i] + ":" + i)
    

if __name__ == '__main__': 

    dir = os.path.dirname(__file__) + "\\data\\id\\"

    degree_dept = {}
    dept_unit = {}
    unit_class = {}
    
    for degree in 1,3,4,5:
        Dept_data = {}
        GetDeptList(Dept_data,degree)
        degree_dept.setdefault(degree,Dept_data)
        
        for deptId in Dept_data.values():
            Unit_data = {}
            GetUnitList(Unit_data, degree, deptId)
            dept_unit.setdefault(deptId,Unit_data)
            
            
            for unitId in Unit_data.values():
                Class_data = {}
                GetClassList(Class_data,degree,unitId)
                unit_class.setdefault(unitId,Class_data)
                    
    # print(json.dumps(degree_dept, indent=4, ensure_ascii=False))
    # print(json.dumps(dept_unit, indent=4, ensure_ascii=False))
    # print(json.dumps(unit_class, indent=4, ensure_ascii=False))
    with open(dir + f"json\\degree_dept.json", 'w', encoding='utf-8') as f:
        d = json.dumps(degree_dept, ensure_ascii=False)
        f.write(d)
    with open(dir + f"json\\dept_unit.json", 'w', encoding='utf-8') as f:
        d = json.dumps(dept_unit, ensure_ascii=False)
        f.write(d)
    with open(dir + f"json\\unit_class.json", 'w', encoding='utf-8') as f:
        d = json.dumps(unit_class, ensure_ascii=False)
        f.write(d)