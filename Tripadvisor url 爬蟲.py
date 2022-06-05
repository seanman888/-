from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os

def url_list(brand):
    brand_URL = [] #標題網址
    for i in range(0,31,30):
        driver.get(f'https://www.tripadvisor.com.tw/Search?q={brand}&searchSessionId=C662145C5679A9B6AFEA91FDC51F87C41648888392784ssid&sid=0B8456A9ED4E41908D08DCBB7B0822911649568966364&blockRedirect=true&ssrc=m&geo=293910&o={i}&rf=1')
    #     driver.get(f'https://www.tripadvisor.com.tw/Search?q={brand}&searchSessionId=C662145C5679A9B6AFEA91FDC51F87C41648888392784ssid&sid=0B8456A9ED4E41908D08DCBB7B0822911649568966364&blockRedirect=true&ssrc=m&geo=293910&o=0&rf=1')
        driver.implicitly_wait(30)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source)
        titles = soup.find_all('div',{'class':'result-title'}) #標題
        http_URL = soup.find_all('a',{'class':'review_count'}) #標題網址
        for title,URL in zip(titles,http_URL):
            if brand in title.text:
                brand_URL.append(URL.get('href'))
    print('總共筆數：',len(brand_URL))
    return brand_URL

if __name__=='__main__':
    chrome_path = os.path.abspath('chromedriver') 
    driver = webdriver.Chrome(chrome_path) 
    driver.get('https://www.google.com.tw/?hl=zh_TW')
    ni = url_list('夏慕尼')  # 13筆正常
    mini = url_list('12MINI') # 3 筆
    enjoy_duck = url_list('享鴨') # 1 筆
    blue_flower = url_list('青花驕') # 5 筆
    hokaido = url_list('聚 -') #  筆
    putien = url_list('莆田') # 8 筆
    yiqi = url_list('藝奇') # 13 筆    
    pinpig = url_list('品田牧場') # 21 筆
    wang = url_list('王品') #  11 筆
    city = url_list('西堤') #  39 筆
    oburn = url_list('原燒') #  22 筆
    house = url_list('陶板屋') #  38 筆
    twelve = url_list('石二鍋') #  47 筆
    hot7 = url_list('hot 7') #  16 筆
