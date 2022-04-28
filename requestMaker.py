import time

import requests
from bs4 import BeautifulSoup

class RequestMaker():
    def __init__(self,url,elementType,className):
        self.url = url
        self.elementType = elementType
        self.className = className

    def getCurent(self):
        try:
            html = BeautifulSoup(requests.get(self.url).text, 'html.parser')
            return int(html.find(self.elementType, class_=self.className).text)
        except:
            time.sleep(15)
            return self.getCurent()