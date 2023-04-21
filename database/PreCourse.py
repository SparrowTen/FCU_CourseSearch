import json
from multiprocessing import Pool
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
    
    def loadData(self):
        with open(self.dir + "\\data\\url\\" + self.year + "\\" + self.json_file, 'r', encoding='utf-8') as f:
            self.data = json.loads(f.read())
    
    def MultigetData(self):
        d_pool = []
        d_pool = Pool(processes = self.max_driver)
        for i in range(0, self.max_driver):
            d_pool.apply_async(self.openDriver)
    
    
if __name__ == '__main__':
    