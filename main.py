#! /usr/bin/python3
import requests

#import urllib2
import tushare as ts
import http.cookiejar as HC
import urllib.parse
import urllib.request
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from lxml import html
#from urllib.request import urlopen
#url='https://movie.douban.com/' #éœ€è¦�çˆ¬æ•°æ�®çš„ç½‘å�€
#page=requests.Session().get(url) 
#tree=html.fromstring(page.text) 
#result=tree.xpath('//td[@class="title"]//a/text()') #èŽ·å�–éœ€è¦�çš„æ•°æ�®
#print(result)

url='http://tieba.baidu.com/f?kw=%E9%94%A4%E5%AD%90%E7%A7%91%E6%8A%80&ie=utf-8'

#print ("ç¬¬äºŒç§�æ–¹æ³•")

#url = ''
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
d = dict(parameter1="value1", parameter2="value2")
url.encode('utf_8')
data = urllib.parse.urlencode(d).encode("utf-8")

req = urllib.request.Request(url)
#with urllib.request.urlopen(req,data=data) as f:
resp = urllib.request.urlopen(req,data=None).read()
print(resp)
print('---------------------*** --- *** ------------------')
#html = resp
bf = BeautifulSoup(resp, features="lxml")
texts = bf.find_all('div', li="search_back_item j_search_back_item")
print(texts)
tree=html.fromstring(resp)
print(tree) 
print('---------------------*** --- *** ------------------')
#result=tree.xpath('//td[@class="title"]//a/text()') #èŽ·å�–éœ€è¦�çš„æ•°æ�®
#print(result)
    
#headers = { 'User-Agent' : user_agent }
#data = urllib.parse.urlencode(values)
#req = urllib.request.Request(url, data, headers)
#req = urllib.request.Request(url, data, headers)
#response = urllib.request.urlopen(req)
#the_page = response.read()
#print(the_page.decode("utf8"))
