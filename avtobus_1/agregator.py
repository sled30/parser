#!/usr/bin/python
from selenium.webdriver import Firefox
# import requests
# from requests import Response
# from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

uri = "https://agregatoreat.ru"
urn = "/purchases/new/page/"
base_page = str(1)
link = uri + urn
url = link + base_page


def get_page(url):
    webdriver = "/home/sled/work/coding/parser/avtobus_1/lib/"
    driver = Firefox(webdriver)
    driver.get(url)
    data = driver.page_source
#    time.sleep(5)
    driver.close()

    return data

def parse_first_page(page):
    try:
        first_date_advert = re.findall(r'<\/div><\/span><\/div><div data-\w{1}-[a-z,0-9]{8,9}.{178}Стартовая&nbsp;цена:.{63}(\d{1,6},.{0,2}&nbsp;руб).{100,}href=\"(\/purchase\/\d{3,}\/order-info)\".{30,}(\d{18}).{50,}Статус закупки:.{40,67}>(\D{4,})</div><!.{231}([^\d<,]{2,}).{4,}>([А-Я .-]{3,}).{30,}контракта: (\d{2}.\d{2}.\d{2})', page)
        return first_date_advert
    except Exception as e:
        print('parse_first_page')
        print(e)

def get_max_num_page(date):
    try:

        max_num_page = re.search(r'item cursor-pointer px13 last\">(\d{1,3})', date)

        return max_num_page[1]

    except Exception as e:
        print('get_max_num_page(date)')
        print(e)

def check_need_info(title):
    try:
        find = re.search(r'автобусы', title)
        if find:
            find = re.search(r'ремонтное', string)
            if find is None:
                return 1
        find = re.search(r'перевозка', title)
        if find:
            find = re.search(r'машины', string)
            if find is None:
                return 1
        find = re.search(r'транспорное', title)
        if find:
            find = re.search(r'спецтехники', string)
            if find is None:
                return 1
        find = re.search(r'транспорные' , title)
        if find:
            find = re.search(r'продажа', string)
            if find is None:
                return 1
        find = re.search(r'автобусов' , title)
        if find:
            find = re.search(r'специальный транспорт', string)
            if find is None:
                return 1
        find = re.search(r'микроавтобусы' , title)
        if find:
            find = re.search(r'грузов', string)
            if find is None:
                return 1
        find = re.search(r'транспортное сопровождение' , title)
        if find:
            find = re.search(r'промышленнных', string)
            if find is None:
                return 1
        find = re.search(r'транспортное обслуживание' , title)
        if find:
            find = re.search(r'отходов', string)
            if find is None:
                return 1
        find = re.search(r'транспорных услуг' , title)
        if find:
            find = re.search(r'страхование', string)
            if find is None:
                return 1
        find = re.search(r'транспортного средства' , title)
        if find:
            find = re.search(r'осмотр', string)
            if find is None:
                return 1
        find = re.search(r'микроавтобусов' , title)
        if find:
            find = re.search(r'техническое обслуживание', string)
            if find is None:
                return 1
        find = re.search(r'транспортировка' , title)
        if find:
            find = re.search(r'оборудование', string)
            if find is None:
                return 1
        find = re.search(r'перевозка сотрудников' , title)
        if find:
            find = re.search(r'технологическим', string)
            if find is None:
                return 1
        find = re.search(r'регулярные перевозки' , title)
        if find:
            find = re.search(r'грузоперевозки', string)
            if find is None:
                return 1
        find = re.search(r'транспортных средств' , title)
        if find:
            return 1

        find = re.search(r'доставка сотрудников' , title)
        if find:
            return 1

        find = re.search(r'детей' , title)
        if find:
            return 1

        find = re.search(r'оферта' , title)
        if find:
            return 1

        find = re.search(r'цветов' , title)
        if find:
            return 1

    except Exception as e:
        print('Error check_need_info(title) ')
        print(e)
#    status = None



def parse_date(source_index_page, link):
    max_num = get_max_num_page(source_index_page)
    first_date = parse_first_page(source_index_page)
    for date in first_date:
        status = check_need_info(date[4])
        if status is not None:
            print('ебагуццооо')
        print(date[4])
        print(status)





#############################################################################################################################################################
#
#
#############################################################################################################################################################
#
#
#############################################################################################################################################################



source_index_page = get_page(url)
if source_index_page:
    parse_date(source_index_page, link)





#for date in first_date:
#    parse_advisor(uri+date[1])
#    break
