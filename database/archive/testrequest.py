import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time
import requests
from bs4 import BeautifulSoup
import html.parser
import io
import sys

dir = os.path.dirname(__file__)

# 讀取設定檔
def load_config():
    global setting
    with open(dir + './config.yml', encoding="utf-8") as f:
        setting = yaml.load(f, Loader=yaml.FullLoader)

# 開啟瀏覽器
def open_webdriver():
    global driver
    # options = {
    #     "browserName": "MicrosoftEdge",
    #     "version": "",
    #     "platform": "WINDOWS",
    #     "ms:edgeOptions": {
    #         "args": ["--inprivate"]
    #     }
    # }
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    driver = webdriver.Chrome(executable_path=dir + './chromedriver.exe')
    driver.get("https://coursesearch04.fcu.edu.tw//CourseOutline.aspx?lang=cht&courseid=1112CE0712400001001")

if __name__ == "__main__":
    open_webdriver()
    time.sleep(3)
    html_source = driver.page_source
    
    soup = BeautifulSoup(html_source,"lxml")
    # text = soup.get_text()
    text = soup.find_all("td",class_="ng-binding")
    for t in text:
        print(t)
    # resp = requests.post("https://coursesearch04.fcu.edu.tw//CourseOutline.aspx?lang=cht&courseid=1112CE0712400001001")
    # print(resp.text)
    # print(text)
    driver.quit()

