import json, re
from threading import Thread
import concurrent.futures
import os
import requests
from bs4 import BeautifulSoup
import time

class PreCourse:
    def __init__(self, json_file):
        self.json_file = json_file
        self.year = self.json_file[0:3]
        self.sms = self.json_file[3]
        self.dept = self.json_file[7:9]
        self.dir = os.path.dirname(__file__)
        
        self.loadJson()
        self.sortData()

    def loadJson(self):
        with open(self.dir + "\\data\\url\\" + self.year + "\\" + self.json_file, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.json_data = data
    
    def sortData(self):
        output = []
        for i in range(0, len(self.json_data)):
            data = self.json_data[i]
            if data == []:
                continue
            self.scr_selcode = data['scr_selcode']
            self.cls_id = data['cls_id']
            request_data_list = self.requestData(data['url'])
            if request_data_list == []:
                continue
            temp_dict = {}
            temp_dict['scr_selcode'] = self.scr_selcode
            temp_dict['cls_id'] = self.cls_id
            temp_dict['PreCourse'] = request_data_list
            for PreCourse in temp_dict['PreCourse']:
                PreCourse['pre_subid3'] = PreCourse['pre_subid3'].replace(' ', '')
            output.append(temp_dict)
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
            # 'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getCourseInfo',
            # 'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getCourseDescr',
            'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getPreCourse',
            # 'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getCorrelation',
            # 'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getLearnOutcome',
            # 'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getEvoluationInfo',
            # 'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getTextbook',
            # 'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getSoftWare',
            # 'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getReference',
            # 'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getTeachSchedule',
            # 'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getEvoluationMethod',
            # 'https://service120-sds.fcu.edu.tw/W320104/action/getdata.aspx/getTeachMethod'
        ]
        raw_dataList = []
        for url in urlList:
            response = rs.post(
                url=url,
                # cookies=cookies,
                headers=headers,
                json=json_data,
            )
            string = json.loads(response.text)['d']
            if (string != ''):
                raw_dataList.append(json.loads(string)[0])
        
        print(self.scr_selcode + '-' + self.cls_id + ' ' + 'requests success')
        return raw_dataList
    
    def saveJson(self, data, file_name):
        dir = os.path.dirname(__file__) + "\\data\\courseInfo\\" + self.year + "\\"
        if not os.path.exists(dir):
            os.mkdir(dir)
        if data != []:
            with open(dir + file_name, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii = False, indent = 4, separators = (',', ': '))
                f.flush()
                f.close()
            print(file_name + ' save success')
        
if __name__ == '__main__':
    # 資料範圍
    years = [110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100]
    for year in years:
        dir = os.path.dirname(__file__) + "\\data\\url\\" + str(year) + "\\"
        file_list = os.listdir(dir)
        start_time = time.time()
        # multi-threading
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(PreCourse, file_list)
        end_time = time.time()
        print('執行時間：' + str(end_time - start_time) + '秒')