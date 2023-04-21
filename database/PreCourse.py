import json
import concurrent.futures
import os
from selenium import webdriver

class PreCourse:
    def __init__(self, json_file, max_driver):
        self.json_file = json_file
        self.year = self.json_file[0:3]
        self.sms = self.json_file[3]
        self.dept = self.json_file[7:9]
        self.dir = os.path.dirname(__file__)
        self.max_driver = max_driver
    
    # /html/body/div/div[1]/div[1]/div/div[3]/div/div/div[1]/table[2]/tbody
    
    def openDriver(self):
        options = {
            "browserName": "MicrosoftEdge",
            "version": "",
            "platform": "WINDOWS",
            "ms:edgeOptions": {
                "args": ["--inprivate"]
            }
        }
        driver = webdriver.Edge(executable_path = dir + "\\webdriver\\" + './msedgedriver.exe', capabilities=options)
        return driver
    
    def loadJson(self):
        with open(self.dir + "\\data\\url\\" + self.year + "\\" + self.json_file, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        return data
    
    def getData(self):
        data = self.loadJson()
        datas = []
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
            index += j
            datas.append(temp)
        print(json.dumps(datas, indent=4, ensure_ascii=False))
    
    # def multitip(self, data):
        
    
    #     # 建立多個 driver 
    #     with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #         executor.map(scrape, urls)
    
if __name__ == '__main__':
    # dir = os.path.dirname(__file__) + "\\data\\url\\111\\"
    file_list = "1111-1-AS.json"
    # file_list = os.listdir(dir)
    pre = PreCourse(file_list, 10)
    data = pre.getData()