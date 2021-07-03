# 캠퍼스픽 크롤링 코드


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import csv


# 크롤링 함수
def get_text(URL):
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    return soup


# 각 학교 페이지 크롤링
def get_page(URL):
    soup = get_text(URL)
    table = soup.find('table', {'class': 'table_list'})
    tr = table.find_all('tr')
    td = tr[1].find_all('td')
    td_list = []
    for t in td:
        td_list.append(t.text)
    return td_list


# 학교 페이지 크롤링 함수
def get_school_page(URL):
    soup = get_text(URL)
    table = soup.find('table', {'class': 'table_list'})
    tr = table.find_all('tr')
    td = tr[1].find_all('td')
    td_list = []
    for t in td:
        td_list.append(t.text)
    return td_list


if __name__ == '__main__':
    # 각 학교 페이지 크롤링
    URL = 'http://www.campuspick.com/school/list.php?page=1'
    td_list = get_page(URL)
    print(td_list)

    
    