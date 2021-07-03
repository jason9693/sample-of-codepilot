# 2021년 네이버 뉴스 댓글 크롤링 코드


import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import time
import csv


def get_news_url():
    url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=sec&sid1=001&sid2=140'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    news_url = soup.select('#main_content > div.list_body.newsflash_body > ul > li > dl > dt > a')
    news_url_list = []
    for i in news_url:
        news_url_list.append(i.get('href'))
    return news_url_list


def get_news_text():
    news_url_list = get_news_url()
    for i in news_url_list:
        url = 'https://news.naver.com' + i
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        news_text = soup.select('#articleBodyContents')
        news_text_list = []
        for j in news_text:
            news_text_list.append(j.text)
        time.sleep(1)
        print(news_text_list)
        with open('news.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(news_text_list)
        f.close()
        time.sleep(1)
        print('저장완료')


get_news_text()
