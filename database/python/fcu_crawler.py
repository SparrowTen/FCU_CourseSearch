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
        close_program()

# 關閉程式
def close_program():
    driver.quit()
    os._exit(0)

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
    except NoSuchElementException:
        print("error")

# 取得資料
def get_data():
    try:
        # 資料筆數
        resault = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div[1]/div[1]/div/div/div/span/span[2]')
        data_amount = int(resault.get_attribute('innerHTML').split(" ")[0])
        print("data find: " + str(data_amount))
        if data_amount != 0:
            # 存入字典
            data_dict = {}        
            data_th_name = ['c_selcode', 'c_name', 'c_credit', 'c_type', 'c_way','c_emi', 'c_class', 'c_info', 'c_people']
            data_tr_number = ['3', '5', '6', '7', '8', '9', '10', '11', '12']
            for c in range(1, data_amount + 1):
                c_code = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div[1]/div[3]/table/tbody/tr[' + str(c) + ']/td[4]').text
                temp_dict = {}
                for d in range(0, 9):
                    source = driver.find_element(By.XPATH, '/html/body/div[1]/div/md-content/div[1]/div[3]/table/tbody/tr[' + str(c) + ']/td[' + data_tr_number[d] + ']').text
                    if source == "":
                        source = "None"
                    temp_dict[data_th_name[d]] = source
                data_dict[c_code] = temp_dict
            print(data_dict)
            if (setting['file'] == "yaml"):
                file_name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
                yaml.dump(data_dict, open(dir + '/data/' + file_name + '.yml', 'w', encoding='utf-8'), allow_unicode=True)
            close_program()
        else:
            select_data()
        
    except NoSuchElementException:
        pass

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
        get_data()
        time.sleep(1)
        check_status()