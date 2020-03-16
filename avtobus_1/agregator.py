#!/usr/bin/python
from selenium.webdriver import Firefox
# import requests
# from requests import Response
# from selenium import webdriver
from bs4 import BeautifulSoup
import re

uri = "https://agregatoreat.ru"
urn = "/purchases/new"
url = uri + urn


def get_page(url):
    webdriver = "/home/sled/work/coding/parser/avtobus_1/lib/"
    driver = Firefox(webdriver)
    driver.get(url)
    data = driver.page_source
    driver.close()

    return data

def parse_first_page(page):
    try:
        first_date_advert = re.findall(r'<\/div><\/span><\/div><div data-\w{1}-[a-z,0-9]{8,9}.{178}Стартовая&nbsp;цена:.{63}(\d{1,6},.{0,2}&nbsp;руб).{100,}href=\"(\/purchase\/\d{3,}\/order-info)\".{30,}(\d{18}).{50,}Статус закупки:.{40,67}>(\D{4,})</div><!.{231}([^\d<,]{2,}).{4,}>([А-Я .-]{3,}).{30,}контракта: (\d{2}.\d{2}.\d{2})', page)
        return first_date_advert
    except Exception as e:
        print('parse_first_page')
        print(e)

def parse_advisor(url):
    pass

source_index_page = get_page(url)
first_date = parse_first_page(source_index_page)

for date in first_date:
    print(date[4])
