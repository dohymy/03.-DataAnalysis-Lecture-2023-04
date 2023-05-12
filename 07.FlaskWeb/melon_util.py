from flask import Flask, render_template, request
import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup

def melon():
    url = 'https://www.melon.com/chart/'
    result = requests.get(url)
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text, 'html.parser')
    trs = soup.select('tbody > tr')
    tr = trs[0]
    line = []
    for tr in trs:
        rank = tr.select_one('.rank ').get_text().split('\n')[0].strip()
        img = tr.select_one('.image_typeAll > img')['src']
        title = tr.select_one('.ellipsis.rank01').get_text().strip()
        artist = tr.select_one('.ellipsis.rank02').get_text().strip()
        album = tr.select_one('.ellipsis.rank03').get_text().strip()
        line.append({'순위':rank, '이미지':img, '제목':title, '아티스트':artist, '앨범':album})
    return line
