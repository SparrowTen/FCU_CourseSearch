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
            print(Unit_data)
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
    
    # 所有學院
    Dept_data = {}
    for degree in 1,3,4,5:
        GetDeptList(Dept_data,degree)
    print("\n## 學院列表：（" + str(len(Dept_data)) + " 筆資料）")
    # Show(Dept_data)
    dataframe = pd.Series(Dept_data, index = Dept_data.keys()) 
    dataframe.to_csv(dir + "csv\\Dept_data.csv")
    with open(dir + "json\\Dept_data.json", 'w', encoding='utf-8') as f:
        d = json.dumps(Dept_data, ensure_ascii=False)
        f.write(d)

    # 所有系所
    # Unit_data = {}
    # for degree in 1,3,4,5:
    #     for deptId in Dept_data.values():
    #         GetUnitList(Unit_data, degree, deptId)
    # print("\n## 系所列表：（" + str(len(Unit_data)) + " 筆資料）")
    # # Show(Unit_data)
    # dataframe = pd.Series(Unit_data, index = Unit_data.keys()) 
    # dataframe.to_csv(dir + "csv\\Unit_data.csv")
    # with open(dir + "json\\Unit_data.json", 'w', encoding='utf-8') as f:
    #     d = json.dumps(Unit_data, ensure_ascii=False)
    #     f.write(d)
    
    for degree in 1,3,4,5:
        for deptId in Dept_data.values():
            Unit_data = {}
            GetUnitList(Unit_data, degree, deptId)
            if len(Unit_data) != 0:
                if not os.path.exists(dir + f"json\\unit\\"):
                    os.makedirs(dir + f"json\\unit\\")
                with open(dir + f"json\\unit\\{deptId}_unit.json", 'w', encoding='utf-8') as f:
                    d = json.dumps(Unit_data, ensure_ascii=False)
                    f.write(d)
    print("\n## 系所列表：（" + str(len(Unit_data)) + " 筆資料）")
    # Show(Unit_data)
    # dataframe = pd.Series(Unit_data, index = Unit_data.keys()) 
    # dataframe.to_csv(dir + "csv\\Unit_data.csv")
    

    # 所有班級
    # Class_data = {}
    # for degree in 1,3,4,5:
    #     for unitId in Unit_data.values():
    #         GetClassList(Class_data,degree,unitId)
    # print("\n## 班級列表：（" + str(len(Class_data)) + " 筆資料）")
    # # Show(Class_data)
    # dataframe = pd.Series(Class_data, index = Class_data.keys()) 
    # dataframe.to_csv(dir + "csv\\Class_data.csv")
    # with open(dir + "json\\Class_data.json", 'w', encoding='utf-8') as f:
    #     d = json.dumps(Class_data, ensure_ascii=False)
    #     f.write(d)