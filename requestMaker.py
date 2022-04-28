import requests
import csv
from bs4 import BeautifulSoup

class RequestMaker():
    def __init__(self,url,elementType,className):
        self.url = url
        self.elementType = elementType
        self.className = className

    def getCurent(self):
        html = BeautifulSoup(requests.get(self.url).text, 'html.parser')
        return int(html.find(self.elementType,class_=self.className).text)