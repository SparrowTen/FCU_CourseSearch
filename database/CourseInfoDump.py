import json
import concurrent.futures
import os
import requests
from bs4 import BeautifulSoup


class PreCourse:
    def __init__(self, json_file, max_driver):
        self.json_file = json_file
        self.year = self.json_file[0:3]
        self.sms = self.json_file[3]
        self.dept = self.json_file[7:9]
        self.dir = os.path.dirname(__file__)
        self.max_driver = max_driver

    def loadJson(self):
        with open(self.dir + "\\data\\url\\" + self.year + "\\" + self.json_file, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        return data
    
    def splitData(self):
        data = self.loadJson()
        if data == []:
            return
        dataLists = []
        each = int(len(data) / self.max_driver)
        last = int(len(data) % self.max_driver)
        index = 0
        for i in range(0, self.max_driver):
            temp = []
            extra = 1 if last > 0 else 0
            for j in range(0, each + extra):
                temp.append(data[index + j])
            if last > 0:
                last -= 1
            index += each + extra
            dataLists.append(temp)
        return dataLists
    
    def multitip(self, dataLists):
        # 建立多執行緒任務
        with concurrent.futures.ThreadPoolExecutor(max_workers = self.max_driver) as executor:
            executor.map(self.getData, dataLists)
    
    def sortData(self, dataList):
        for i in range(0, len(dataList)):
            data = dataList[i]
            if data == []:
                continue
            self.scr_selcode = data['scr_selcode']
            self.cls_id = data['cls_id']
            self.requestData(data['url'])
            os._exit(0)
    
    
    def requestData(self, url):
        rs = requests.session()
        raw_js = BeautifulSoup(rs.get(url).content, "html.parser").find("script").text
        course_id = raw_js.split(';')[1].split(',')[1].replace(' \'', '').replace('\' )', '')
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://service120-sds.fcu.edu.tw',
            'Referer': 'https://service120-sds.fcu.edu.tw/W320104/index.htm?20220214',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
            'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        json_data = {
            'course_id': course_id
        }
        urlList = [
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getCourseInfo',
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getCourseDescr',
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getPreCourse',
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getCorrelation',
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getLearnOutcome',
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getEvoluationInfo',
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getTextbook',
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getSoftWare',
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getReference',
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getTeachSchedule',
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getEvoluationMethod',
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getTeachMethod'
        ]
        raw_dataList = []
        for url in urlList:
            response = rs.post(
                url=url,
                # cookies=cookies,
                headers=headers,
                json=json_data,
            )
            # print(response.text)
            # dataByString = self.stringProcess(response.text)
            # raw_dataList.append(json.loads(response.text))
            self.saveJson(json.loads(response.text), self.scr_selcode + '-' + self.cls_id + '-' + url.split('/')[6] +'.json')
            # print(json.loads(response.text)['d'])
        return raw_dataList

    def stringProcess(self, string):
        string = string.replace('\\"', '"' )            # 將 \" 過濾成 "
        string = string.replace('\\\"', '"')            # 將 \\" 過濾成 "
        string = string.replace('"d":"{', '"d": {' )   
        string = string.replace('"d":"[{', '"d": [{' )
        string = string.replace(']}"}', ']}}')
        string = string.replace('}]"}', '}]}')
        return string
    
    def saveJson(self, data,file_name):
        dir = os.path.dirname(__file__) + "\\data\\courseInfo\\111\\"
        if not os.path.exists(dir):
            os.mkdir(dir)
        with open(dir + file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
if __name__ == '__main__':
    dir = os.path.dirname(__file__) + "\\data\\url\\111\\"
    file_list = ["1111-1-CI.json"]
    # file_list = os.listdir(dir)
    for file in file_list:
        pre = PreCourse(file, 10)
        dataLists = pre.splitData()
        pre.sortData(dataLists[0])