# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

import os
import time
import csv
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from urllib.parse import quote_plus
import glob
import re

driver = webdriver.Chrome('C:\python\driver/chromedriver.exe')

searchList = []
for start in range(1, 25, 1):
    baseUrl = f'http://ec2-54-180-4-52.ap-northeast-2.compute.amazonaws.com:8090/board/review/?pageNum={start}'
    driver.get(baseUrl)

    html = driver.page_source
    soup = bs(html, "html.parser")

    r = soup.find_all('table')[-1].find_all('tr')[1:]

    for i in r:
        temp = []
        temp.append(i.select('td')) # 제목
        print()
        searchList.append(temp)

driver.close()

f = open('test.csv', 'w', newline='')
csvWriter = csv.writer(f)
for i in searchList:
    # 한줄씩 써 내려감
    csvWriter.writerow(i)
f.close()


s = str(input('Input Searching Text : '))

p = re.compile(s)

for i in glob.glob(r'test.csv'):
    with open(i, 'r') as f:
        for x, y in enumerate(f.readlines(),1):
            m = p.findall(y)
            if m:
                print('File %s [ %d ] Line Searching : %s' %(i,x,m))
                print('Full Line Text : %s' %y)
        print()