import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time

dir = os.path.dirname(__file__)

# 讀取設定檔
def load_config():
    global setting
    with open(dir + './config.yml', encoding="utf-8") as f:
        setting = yaml.load(f, Loader=yaml.FullLoader)

# 開啟瀏覽器
def open_webdriver():
    global driver
    options = {
        "browserName": "MicrosoftEdge",
        "version": "",
        "platform": "WINDOWS",
        "ms:edgeOptions": {
            "args": ["--inprivate"]
        }
    }
    driver = webdriver.Edge(executable_path=dir + './msedgedriver.exe', capabilities=options)
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
            time.sleep(0.5)
            md_select = driver.find_element(By.XPATH, '//*[@id="' + setting['select_list'][select] + '"]')
            driver.execute_script("arguments[0].click();", md_select)
            time.sleep(0.5)
            md_option = driver.find_element(By.XPATH, '//*[@id="' + setting['select_option'][select] + '"]')
            driver.execute_script("arguments[0].click();", md_option)
        time.sleep(0.5)
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
        time.sleep(1)
        check_status()