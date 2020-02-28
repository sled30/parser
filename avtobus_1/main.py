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

        return okpd[1]
    except Exception as e:
        print(e)
def get_eat_advert(page):
    try:
        eat = re.search(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}-\d{1,2}-\d{1,2}-\d{1,2}-\d{1,2}-\d{1,2}-\d{1,2})', page)

        return eat[1]

    except Exception as e:
        print(e)
def get_provisioner(page):
    try:
        provisioner = re.search(r'Поставщик:\n.{117}\n\s{2,20}(.{1,})', page)

        return provisioner[1]


    except Exception as e:
        print(e)
def get_unit(page):
    try:
        unit = re.search(r'Единица измерения:\s(.{1,})\n', page)

        return unit[1]

    except Exception as e:
        print('get_unit')
        print(e)
def get_amount(page):
    try:
        amount = re.search(r'Количество:\s(.{1,})\n', page)

        return amount[1]

    except Exception as e:
        print('get_amount')
        print(e)
def get_cost(page):
    try:
        cost = re.search(r'price-product">(.{1,})<\/div', page)

        return cost[1]

    except Exception as e:
        print('get_cost')
        print(e)

source_index_page = get_page(url)
urn_adverts = parse_page_to_link(source_index_page)

for urn_advert in urn_adverts:
    url_advert = uri + urn_advert
    page_advert = get_page(url_advert)
    #print(page_advert)
    title = get_title_advert(page_advert)

    okpd = get_okpd_advert(page_advert)

    eat = get_eat_advert(page_advert)

    provisioner = get_provisioner(page_advert)

    unit = get_unit(page_advert)
    #print(unit)

    amount = get_amount(page_advert)

    cost = get_cost(page_advert)

    print(cost)


    print('#################################################')

    #print(title)
