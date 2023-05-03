from flask import Flask, render_template, request
import requests
import pandas as pd
from bs4 import BeautifulSoup

def crawling():
    base_url = 'http://book.interpark.com'
    suburl = '/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028'
    res = requests.get(base_url + suburl)
    soup = BeautifulSoup(res.text)
    lis = soup.select('.rankBestContentList > ol > li')
    lines = []
    for li in lis:
        rank_data = li.select('.rankBtn_ctrl')
        if len(rank_data) == 1:
            rank = int(rank_data[0]['class'][-1][-1])
        else:
            rank = int(rank_data[0]['class'][-1][-1] + rank_data[1]['class'][-1][-1]) 
        img = li.select_one('.coverImage').find('img')['src']
        href = li.select_one('.coverImage').find('a')['href']
        title = li.select_one('.itemName').get_text().strip()
        author = li.select_one('.author').get_text().strip()
        company = li.select_one('.company').get_text().strip()
        price = li.select_one('.price > em').get_text().strip()
        lines.append({'순위':rank, '제목':title, '이미지':img, 'href':base_url + href, '저자':author, '출판사':company, '가격':price})
    return lines