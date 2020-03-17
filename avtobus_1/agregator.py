#!/usr/bin/python
from selenium.webdriver import Firefox
# import requests
# from requests import Response
# from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time


def get_page(url):
    webdriver = "/home/sled/work/coding/parser/avtobus_1/lib/"
    driver = Firefox(webdriver)
    driver.get(url)
    data = driver.page_source
    driver.close()

    return data

def parse_first_page(page):
    try:

        first_date_advert = re.findall(r'<\/div><\/span><\/div><div data-\w{1}-[a-z,0-9]{8,9}.{178}Стартовая&nbsp;цена:.{63}(\d{1,6},.{0,2}&nbsp;руб).{100,}href=\"\/purchase\/\d{3,}\/order-info\".{30,}(\d{18}).{50,}Статус закупки:.{40,67}>(\D{4,})</div><!.{231}([^\d<,]{2,}).{4,}>([А-Я .-]{3,}).{30,}контракта: (\d{2}.\d{2}.\d{2}).{60,}href=\"(/purchase/\d{5,}/order-info)', page)
        return first_date_advert
    except Exception as e:
        print('parse_first_page')
        print(e)

def get_max_num_page(date):
    try:

        max_num_page = re.search(r'item cursor-pointer px13 last\">(\d{1,3})', date)

        return int(max_num_page[1])

    except Exception as e:
        print('get_max_num_page(date)')
        print(e)

def check_need_info(title):
    try:
        find = re.search(r'автобусы', title)
        if find:
            find = re.search(r'ремонтное', title)
            if find is None:
                return 1
        find = re.search(r'перевозка', title)
        if find:
            find = re.search(r'машины', title)
            if find is None:
                return 1
        find = re.search(r'транспорное', title)
        if find:
            find = re.search(r'спецтехники', title)
            if find is None:
                return 1
        find = re.search(r'транспорные' , title)
        if find:
            find = re.search(r'продажа', title)
            if find is None:
                return 1
        find = re.search(r'автобусов' , title)
        if find:
            find = re.search(r'специальный транспорт', title)
            if find is None:
                return 1
        find = re.search(r'микроавтобусы' , title)
        if find:
            find = re.search(r'грузов', title)
            if find is None:
                return 1
        find = re.search(r'транспортное сопровождение' , title)
        if find:
            find = re.search(r'промышленнных', title)
            if find is None:
                return 1
        find = re.search(r'транспортное обслуживание' , title)
        if find:
            find = re.search(r'отходов', title)
            if find is None:
                return 1
        find = re.search(r'транспорных услуг' , title)
        if find:
            find = re.search(r'страхование', title)
            if find is None:
                return 1
        find = re.search(r'транспортного средства' , title)
        if find:
            find = re.search(r'осмотр', title)
            if find is None:
                return 1
        find = re.search(r'микроавтобусов' , title)
        if find:
            find = re.search(r'техническое обслуживание', title)
            if find is None:
                return 1
        find = re.search(r'транспортировка' , title)
        if find:
            find = re.search(r'оборудование', title)
            if find is None:
                return 1
        find = re.search(r'перевозка сотрудников' , title)
        if find:
            find = re.search(r'технологическим', title)
            if find is None:
                return 1
        find = re.search(r'регулярные перевозки' , title)
        if find:
            find = re.search(r'грузоперевозки', title)
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

        find = re.search(r'Заправ' , title)
        if find:
            return 1

    except Exception as e:
        print('Error check_need_info(title) ')
        print(e)
#    status = None

def get_advert_info(advert_page):
    print(advert_page)
    print("https://agregatoreat.ru" + advert_page[6])
    source_advert = get_page("https://agregatoreat.ru" + advert_page[6])
    print(source_advert)


def logic_work():

    uri = "https://agregatoreat.ru"
    urn = "/purchases/new/page/"
    base_page = str(1)
    link = uri + urn
    url = link + base_page

    try:
        source_index_page = get_page(url)
        if source_index_page:
            max_page = get_max_num_page(source_index_page)
            parse_date(source_index_page)
            for number in range(2, max_page):
                #print(link + str(number))
                page = get_page(link + str(number))
                parse_date(page)
                #print(uri + urn )
    except Exception as e:
        pass



def parse_date(source_index_page):
#    max_num = get_max_num_page(source_index_page)
    first_date = parse_first_page(source_index_page)
    for date in first_date:
        #print(date)
        status = check_need_info(date[3])
        if status is not None:
            get_advert_info(date)

def get_name_company(page):
    name_company = re.search(r'Наименование</div>.{179}([а-яА-Я \"-]{3,})', page)
    return name_company







#############################################################################################################################################################
#
#
#############################################################################################################################################################
#
#
#############################################################################################################################################################
logic_work()


#    parse_date(source_index_page, link)
