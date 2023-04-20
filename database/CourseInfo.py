# 111 / 1 / CC00100 / 48597 / 001
# 學年度 / 學期 / 班級 / sub_id / scr_dup

import json
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

class CourseInfo:
    def __init__(self, json_file):
        self.json_file = json_file
    
    def getUrl(self):
        self.year = self.json_file[0:3]
        self.sms = self.json_file[5]
        with open(dir + "\\data\\course\\" + self.year + "\\" + self.json_file, 'r', encoding='utf-8') as f:
            raw_data = json.loads(f.read())
        data = []
        for i in range(len(raw_data['d']['items'])):    
            link = "https://coursesearch04.fcu.edu.tw/CourseOutline.aspx?lang=cht&courseid="
            self.cls_id = raw_data['d']['items'][i]['cls_id']
            self.sub_id = raw_data['d']['items'][i]['sub_id']
            scr_dup = raw_data['d']['items'][i]['scr_dup']
            url = link + self.year + self.sms + self.cls_id + self.sub_id + scr_dup
            data_dict = {}
            data_dict['cls_id'] = self.cls_id
            data_dict['url'] = url
            data.append(data_dict)
        self.saveUrl(data)
        
    def open_webdriver(self, url):
        options = {
            "browserName": "MicrosoftEdge",
            "version": "",
            "platform": "WINDOWS",
            "ms:edgeOptions": {
                "args": ["--inprivate"]
            }
        }
        driver = webdriver.Edge(executable_path=dir + './msedgedriver.exe', capabilities=options)
        driver.get(url)
        return driver
    
    def getHtml(self, url):
        driver = self.open_webdriver(url)
        time.sleep(5)
        html_source = driver.page_source
        driver.quit()
        return html_source    
    
    def saveHtml(self, html_source):
        file_name = '{}{}-{}-{}.html'.format(str(self.year), str(self.sms), str(self.cls_id), str(self.sub_id))
        dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\\html\\course\\" + year + "\\"
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(dir + file_name, 'w', encoding='utf-8') as f:
            f.write(html_source)

    def saveUrl(self, data):
        file_name = self.json_file
        dir = os.path.dirname(__file__) + "\\data\\url\\" + year + "\\"
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(dir + file_name, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii = False, indent = 4, separators = (',', ': ')))
    
if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    years = os.listdir(dir + "\\data\\course")
    for year in years:
        json_path = dir + "\\data\\course" + "\\{}\\".format(str(year))
        json_files = os.listdir(json_path)
        for json_file in json_files:
            course = CourseInfo(json_file)
            course.getUrl()