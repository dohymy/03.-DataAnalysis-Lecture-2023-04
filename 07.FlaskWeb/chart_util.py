from flask import Flask, render_template, request
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

def chart():
    url = 'https://www.genie.co.kr/chart/top200'
    result = requests.get(url)
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text, 'html.parser')
    trs = soup.select('tr.list')
    now = datetime.now()
    ymd = now.strftime('%Y%M%d')
    hh = now.strftime('%H')
    lines = []
    base_url = 'https://www.genie.co.kr/chart/top200?ditc=D'
    for page in range(1,5):
        url = f'{base_url}&{ymd}&{hh}&pg={page}'
        result = requests.get(url, headers=header)
        soup = BeautifulSoup(result.text, 'html.parser')
        trs = soup.select('tr.list')
        for tr in trs:
            rank = tr.select_one('.number').get_text().split('\n')[0].strip()
            img = 'https:' + tr.select_one('.cover > img')['src']
            title = tr.select_one('.title.ellipsis').get_text().split('\n')[-1].strip()
            artist = tr.select_one('.artist.ellipsis').string.strip()
            album = tr.select_one('.albumtitle.ellipsis').string.strip()
            lines.append({'순위':rank, '이미지':img, '제목':title, '아티스트':artist, '앨범':album})
    return lines