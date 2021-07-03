# 카카오번역


import requests
import json
import os
import sys
import time
from datetime import datetime
from kakao_api_key import *


# 번역할 문장을 입력 받는다.
def get_input_sentence():
    return input("번역할 문장을 입력하세요: ")


# 번역할 문장을 받아온 후, 배열로 바꾼다.
def get_translated_sentence(input_sentence):
    data = {
        'source': 'ko',
        'target': 'en',
        'text': input_sentence
    }
    headers = {'X-KakaoAK': kakao_api_key}
    url = 'https://kapi.kakao.com/v1/translation/translate'
    res = requests.post(url, headers=headers, data=data)
    translated_sentence = res.json()['result']['translated_text']
    return translated_sentence


# 번역한 문장을 출력한다.
def print_translated_sentence(translated_sentence):
    print("번역 결과:", translated_sentence)
    return


# 번역한 문장을 파일에 저장한다.
def save_translated_sentence(translated_sentence):
    f = open("translated_sentence.txt", "w")
    f.write(translated_sentence)
    f.close()
    return


# 인자로 받은 문장을 파일에서 읽어온다.
def get_translated_sentence_from_file():
    f = open("translated_sentence.txt", "r")
    translated_sentence = f.read()
    f.close()
    return translated_sentence


# 번역한 문장을 파일에서 읽어온다.
def get_translated_sentence_from_file():
    f = open("translated_sentence.txt", "r")
    translated_sentence = f.read()
    f.close()
    return translated_sentence


if __name__ == '__main__':
    while True:
        input_sentence = get_input_sentence()
        translated_sentence = get_translated_sentence(input_sentence)
        print_translated_sentence(translated_sentence)
        save_translated_sentence(translated_sentence)
        translated_sentence = get_translated_sentence_from_file()
        print_translated_sentence(translated_sentence)
        time.sleep(5)