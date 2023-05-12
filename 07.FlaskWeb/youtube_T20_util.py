from flask import Flask, render_template, request
import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def crawling():
    url ='https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&sop=and&sst=subscriber_cnt&sod=desc&sfl=&stx=&sca=&page=1'
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    trs = soup.select('#list-skin > form:nth-child(4) > table > tbody > tr')
    driver = webdriver.Chrome('C:/Users/YONSAI/Downloads/chromedriver.exe')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source)
    trs = soup.select('.aos-init')
    tr = trs[0]
    def convert(s):
        s = s.replace('억','').replace('개','').replace(',','').replace('만','0000')
        return int(s)
    lines = []
    for tr in trs:
        rank = int(tr.select_one('.rank').get_text().strip())
        category = tr.select_one('.category').get_text().strip()[1:-1]
        channel = tr.select_one('.subject > h1 > a').get_text().strip()
        subscriber_cnt = convert(tr.select_one('.subscriber_cnt').get_text().strip())
        view_cnt = convert(tr.select_one('.view_cnt').get_text().strip())
        video_cnt = convert(tr.select_one('.video_cnt').get_text().strip())
        if rank <= 20:
            lines.append({
                '순위': rank, '카테고리':category, '채널명': channel, '구독자수': subscriber_cnt, '조회수': view_cnt,
                '비디오': video_cnt
        })
    driver.close()
    return lines

