#!/usr/bin/python
from selenium.webdriver import Firefox
# import requests
# from requests import Response
# from selenium import webdriver
from bs4 import BeautifulSoup
import re

url = "https://agregatoreat.ru/search/p/автобусы/klassifikator-eat-classifier-eat"

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


source_index_page = get_page(url)
url_advert = parse_page_to_link(source_index_page)
