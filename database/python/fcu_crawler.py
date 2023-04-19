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
    
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

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
    driver = webdriver.Chrome(executable_path=dir + './chromedriver.exe')
    driver.get(setting['url'])

# 檢查網頁狀態
def check_status():
    html_source = driver.page_source
    if "courseSearch" not in html_source:
        print("web close")
        driver.quit()

# 選擇要讀取的分類
def select_data():
    try:
        for select in setting['select_list']:
            md_select = driver.find_element(By.XPATH, '//*[@id="' + setting['select_list'][select] + '"]')
            time.sleep(0.1)
            driver.execute_script("arguments[0].click();", md_select)
            time.sleep(0.1)
            md_option = driver.find_element(By.XPATH, '//*[@id="' + setting['select_option'][select] + '"]')
            time.sleep(0.1)
            driver.execute_script("arguments[0].click();", md_option)
            time.sleep(0.1)
        search_btn = driver.find_element(By.XPATH, '//*[@class="md-raised  md-primary md-button ng-scope"]')
        driver.execute_script("arguments[0].click();", search_btn)
        print("success")
        time.sleep(10)
    except NoSuchElementException:
        print("error")

if __name__ == "__main__":
    load_config()
    open_webdriver()

    while True:
        html_source = driver.page_source
        if "courseSearch" in html_source:
            print("web loaded")
            break
        else:
            print("web loading")
        time.sleep(1)

    # 網頁限於課務系統
    while(True):
        # print(driver.current_url)
        select_data()
        html_source = driver.page_source
        if "逢甲大學課程檢索系統" in html_source:
            time.sleep(1)
            check_status()
            print("Done")
            break
    
    html_source = driver.page_source
    soup = BeautifulSoup(html_source,"lxml")
    course_link = []
    for link in soup.find_all('a'):
        str = "https://coursesearch04.fcu.edu.tw/" + link.get('href')
        course_link.append(str)
    
    del course_link[0]
    print(course_link)
    driver.quit()
    
    for link in course_link:
        driver = webdriver.Chrome(executable_path=dir + './chromedriver.exe')
        driver.get(link)
        time.sleep(3)
        # html_source = driver.page_source
        # soup = BeautifulSoup(html_source,"lxml")
        driver.quit()