#!/usr/bin/python
from selenium.webdriver import Firefox
# import requests
# from requests import Response
# from selenium import webdriver
from bs4 import BeautifulSoup
import re

uri = "https://agregatoreat.ru"
urn = "/search/p/автобусы/klassifikator-eat-classifier-eat"
url = uri + urn


def get_page(url):
    webdriver = "/home/sled/work/coding/parser/avtobus_1/lib/"
    driver = Firefox(webdriver)
    driver.get(url)
    data = driver.page_source
    driver.close()

    return data

def parse_page_to_link(page):
    url_advert = re.findall(r'<a data-v-bd072e2c=\"\" href=\"(/p/.{0,}=Classifier_EAT)', page)

    return url_advert

def get_title_advert(page):
    try:
        title_advert = re.search(r'class=\"mb20 fs24 mt0 cl-black product-name uppercase\">\n(.{0,})', page)

        return title_advert[1].strip()

    except Exception as e:
        print(e)
def get_okpd_advert(page):
    try:
        okpd = re.search(r'Код по ОКПД2:\s(\d{1,4}.\d{1,4}.\d{1,5}.\d{1,5})', page)

        return okpd
    except Exception as e:
        print(e)
def get_eat_advert(page):
    try:
        eat = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}-\d{1,2}-\d{1,2}-\d{1,2}-\d{1,2}-\d{1,2}-\d{1,2}', page)

        return eat

    except Exception as e:
        print(e)



source_index_page = get_page(url)
urn_adverts = parse_page_to_link(source_index_page)

for urn_advert in urn_adverts:
    url_advert = uri + urn_advert
    page_advert = get_page(url_advert)
    print(page_advert)
    title = get_title_advert(page_advert)
    okpd = get_okpd_advert(page)
    eat = get_eat_advert(page)
    
    #print(title)
