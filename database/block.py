import json
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

class CourseBlock:
    def __init__(self, json_file):
        self.json_file = json_file
        self.year = self.json_file[0:3]
        self.sms = self.json_file[5]

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
        dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\\html\\course\\" + self.year + "\\"
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(dir + file_name, 'w', encoding='utf-8') as f:
            f.write(html_source)

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    # url = os.listdir(dir + "\\data\\url\\111")
    course = CourseBlock("1112-1-CI.json")
    with open(dir + "\\data\\url\\111\\1112-1-CI.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    for d in data:
        course.getHtml(d["url"])