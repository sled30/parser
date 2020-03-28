#!/usr/bin/python
from selenium.webdriver import Firefox

from selenium.webdriver.firefox.options import Options
import time
# import requests
# from requests import Response
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta

def get_time():

    curent_date = datetime.today()
    tomorrow = timedelta(days = 1)
    date = curent_date - tomorrow

    return (date.strftime("%d.%m.%Y"), curent_date.strftime("%d.%m.%Y"))


def get_page(url):
    options = Options()
    options.headless = True
    options.add_argument("--enable-javascript")
    driver = webdriver.Firefox(options = options, executable_path=r'/home/sled/work/coding/parser/avtobus_1/lib/geckodriver')
    driver.get_cookies()
    driver.get(url)
#    driver.set_page_load_timeout(20)

    driver.set_script_timeout(4)
    data = driver.page_source
    driver.close()

    return data

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

        find = re.search(r'ремонт' , title)
        if find:
            return 1

    except Exception as e:
        print('Error check_need_info(title) ')
        print(e)
#    status = None
def find_string(phase):
    find_string = ('автобусы',
                   'транспорное',
                   'транспорное',
                   'транспорные',
                   'автобусов',
                   'микроавтобусы',
                   'транспортное сопровождение',
                   'транспортное обслуживание',
                   'транспорных услуг',
                   'транспортного средства',
                   'микроавтобусов',
                   'транспортировка',
                   'перевозка сотрудников',
                   'регулярные перевозки',
                   'транспортных средств',
                   'доставка сотрудников',
                   'детей',
                   'оферта')
    find_string_2 = ('гужевой',
                      'гужевые повозки',
                      'с помощью животных')
    find_string_3 = ('конная амуниция кожа',
                     'седла',
                     'уздечки',
                     'нагайки',
                     'недоузки',
                     'ногавки',
                     'вальтрапы',
                     'подпруги',
                     'элементы упряжи из кожи',
                     'потники',
                     'стремена',
                     'упряж кожа',
                     'попоны')

    find_string_4 = ('эксукурсионное',
                     'проведение экскурсий',
                     'экскурсии')

    if phase == 1:
        return find_string
    elif phase == 2:
        return find_string
    elif phase == 3:
        return find_string_2 + find_string_3
    elif phase == 4:
        return find_string_4
