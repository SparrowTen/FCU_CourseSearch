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
        year = self.json_file[0:3]
        sms = self.json_file[5]
        with open(dir + "\\data\\course\\" + year + "\\" + self.json_file, 'r', encoding='utf-8') as f:
            raw_data = json.loads(f.read())
        for i in range(len(raw_data['d']['items'])):    
            link = "https://coursesearch04.fcu.edu.tw/CourseOutline.aspx?lang=cht&courseid="
            cls_id = raw_data['d']['items'][i]['cls_id']
            sub_id = raw_data['d']['items'][i]['sub_id']
            scr_dup = raw_data['d']['items'][i]['scr_dup']
            url = link + year + sms + cls_id + sub_id + scr_dup
        return url
    
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

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    years = os.listdir(dir + "\\data\\course")
    for year in years:
        json_path = dir + "\\data\\course" + "\\{}\\".format(str(year))
        json_files = os.listdir(json_path)
        for json_file in json_files:
            course = CourseInfo(json_file)
            url = course.getUrl()
            html_source = course.getHtml(url)
            print(url)
            print(html_source)
            os._exit(0)