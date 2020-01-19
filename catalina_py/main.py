import os
import sys
import re
import time
import dateutil
import datetime
import dateutil.parser
import sqlite3

def read_file(file):
    with open('file/' + file) as line:
        for row in line:
            parser(row)
    line.close()
def serialase_date(date):
    """ переводит формат времени в таймштамп"""
    date = dateutil.parser.parse(date)
    return date.timestamp()
def conn():
    connect = sqlite3.connect(db)
    return connect

def parser(string):
    """
    date.timestamp() возвращает таймштамп
    source[2] возвращает телефон
    source[3] возвращает ид отправленного
    """
    source = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{1,3}).{1,}для клиента (\d{11,12}).{1,}\[(.{1,})\]", string)
    if source:
        date = serialase_date(source[1])
        phone = source[2]
        source_ids = source[3]
        return 1

    else:
        response = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).\d{1,}.{1,}клиенту (\d{11,12}) отправлено: \{.{1,}failure\":(\d{1,}).{1,}\[(.{0,}\{\"error\":\"\w{1,}\"\}.{0,})\]", string)
        if response:
            date = serialase_date(response[1])
            phone = response[2]
            count_error = response[3]
            error = response[4]
            return 1

def save_source():
    pass
def save_lor():
    pass
def work_sqlite():
    pass


file_list = os.listdir(path = 'file/')
for file in file_list:
    read_file(file)
