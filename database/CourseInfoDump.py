import json
import concurrent.futures
import os
import requests
from bs4 import BeautifulSoup
import time

class PreCourse:
    def __init__(self, json_file, max_t):
        self.json_file = json_file
        self.year = self.json_file[0:3]
        self.sms = self.json_file[3]
        self.dept = self.json_file[7:9]
        self.dir = os.path.dirname(__file__)
        self.max_t = max_t

    def loadJson(self):
        with open(self.dir + "\\data\\url\\" + self.year + "\\" + self.json_file, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        return data
    
    def splitData(self):
        data = self.loadJson()
        if data == []:
            return
        dataLists = []
        each = int(len(data) / self.max_t)
        last = int(len(data) % self.max_t)
        index = 0
        for i in range(0, self.max_t):
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
        with concurrent.futures.ThreadPoolExecutor(max_workers = self.max_t) as executor:
            executor.map(self.sortData, dataLists)
    
    def sortData(self, jsonDataList):
        output = []
        for i in range(0, len(jsonDataList)):
            JsonData = jsonDataList[i]
            if JsonData == []:
                continue
            self.scr_selcode = JsonData['scr_selcode']
            self.cls_id = JsonData['cls_id']
            dataList = self.requestData(JsonData['url'])
            # for i in range(0, len(dataList)):
            #     for data in dataList[i]:
            #         for key in data:
            #             output[key] = data[key]
            # print(output)
            # self.saveJson(output, self.scr_selcode + '-' + self.cls_id + '.json')
            output.append(dataList)
        self.saveJson(output, str(self.json_file))
    
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
            string = response.text

        print(self.scr_selcode + '-' + self.cls_id + ' ' + 'requests success')
        self.saveJson(raw_dataList, self.scr_selcode + '-' + self.cls_id + '.json')
        os._exit(0)
        return raw_dataList
    
    def stringProcess(self, string):
        string = string.replace('"[', '[')
        string = string.replace(']"', ']')
        string = string.replace('\\r\\n', '')
        # string = string.replace('"d":"{', '"d": {' )   
        # string = string.replace('"d": "[{', '"d": [{' )
        # string = string.replace('}]"}', '}]}')
        # string = string.replace(']}"}', ']}}')
        return string
    
    def saveJson(self, data, file_name):
        dir = os.path.dirname(__file__) + "\\data\\courseInfo\\111\\"
        if not os.path.exists(dir):
            os.mkdir(dir)
        # dir = dir + self.json_file.split('.')[0] + "\\"
        # if not os.path.exists(dir):
            # os.mkdir(dir)
        with open(dir + file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii = False, indent = 4, separators = (',', ': '))
        print(file_name + ' save success')
        
if __name__ == '__main__':
    dir = os.path.dirname(__file__) + "\\data\\url\\111\\"
    file_list = ["1111-1-CI.json"]
    # file_list = os.listdir(dir)
    start_time = time.time()
    for file in file_list:
        pre = PreCourse(file, 10)
        dataLists = pre.splitData()
        # pre.multitip(dataLists)
        pre.sortData(dataLists[0])
    end_time = time.time()
    print('執行時間：' + str(end_time - start_time) + '秒')