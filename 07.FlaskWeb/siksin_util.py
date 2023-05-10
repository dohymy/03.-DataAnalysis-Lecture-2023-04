from flask import Flask, render_template, request
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote

def siksin(place):
    base_url = 'https://www.siksinhot.com/search'
    url = f'{base_url}?keywords={quote(place)}'
    results = requests.get(url)
    soup = BeautifulSoup(results.text, 'html.parser')
    lis = soup.select('.localFood_list > li')
    li = lis[0]
    line = []
    for li in lis:
        img = li.find('img')['src']
        title = li.select_one('.textBox > h2').get_text()
        score = li.select_one('.textBox > .score').get_text()
        a_tags = li.select('.cate > a')
        location = a_tags[0].get_text()
        menu = a_tags[1].get_text()
        line.append({'이미지':img, '상호명':title, '별점':score, '위치':location,'메뉴':menu})
    return line