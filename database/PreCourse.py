import json
import concurrent.futures
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class PreCourse:
    def __init__(self, json_file, max_driver):
        self.json_file = json_file
        self.year = self.json_file[0:3]
        self.sms = self.json_file[3]
        self.dept = self.json_file[7:9]
        self.dir = os.path.dirname(__file__)
        self.max_driver = max_driver

    def openDriver(self):
        options = {
            "browserName": "MicrosoftEdge",
            "version": "",
            "platform": "WINDOWS",
            "ms:edgeOptions": {
                "args": ["--inprivate"]
            }
        }
        driver = webdriver.Edge(executable_path = self.dir + "\\webdriver\\" + 'msedgedriver.exe', capabilities=options)
        return driver
    
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
        # print(json.dumps(dataList, indent=4, ensure_ascii=False))
    
    def getData(self, dataList):
        driver = self.openDriver()
        for i in range(0, len(dataList)):
            data = dataList[i]
            if data == []:
                continue
            driver.get(data['url'])
            time.sleep(5)
            preCourseList = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div[3]/div/div/div[1]/table[2]/tbody')
            for preCourse in preCourseList.find_elements(By.XPATH, 'tr'):
                preCourseID = preCourse.find_elements(By.XPATH, 'td').text
                print(preCourseID)
        driver.quit()
    
    def multitip(self, dataLists):
        # 建立多個 driver
        # for i in range(0, self.max_driver):
        with concurrent.futures.ThreadPoolExecutor(max_workers = self.max_driver) as executor:
            executor.map(self.getData, dataLists)
    
if __name__ == '__main__':
    dir = os.path.dirname(__file__) + "\\data\\url\\111\\"
    file_list = ["1111-1-AS.json"]
    # file_list = os.listdir(dir)
    for file in file_list:
        pre = PreCourse(file, 10)
        dataLists = pre.splitData()
        pre.multitip(dataLists)