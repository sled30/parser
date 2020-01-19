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
    connect = sqlite3.connect("db")
    return connect
def create_db():
    """ create structure db """
    create_source = "CREATE TABLE IF NOT EXISTS `source` ( \
	           `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , \
            	  `phone` varchar(14) NOT NULL, `status` varchar(3) NOT NULL, \
                  `time` varchar(20) NOT NULL, `ids` varchar(50) NOT NULL)"
    create_ids = "CREATE TABLE IF NOT EXISTS `ids` ( \
              	  `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , \
              	  `phone` varchar(14) NOT NULL, `string_error` varchar(100) NOT NULL, \
                  `secund` varchar(2) NULL, `status` varchar(2) NULL, \
                  `1_error` varchar(100) NULL, `2_error` varchar(100) NULL, \
                  `3_error` varchar(100) NULL, `4_error` varchar(100) NULL, \
                  `5_error` varchar(100) NULL,  `6_error` varchar(100) NULL, \
                  `7_error` varchar(100) NULL, `8_error` varchar(100) NULL, \
                  `9_error` varchar(100) NULL, `10_error` varchar(100) NULL, \
                  `11_error` varchar(100) NULL,  `12_error` varchar(100) NULL, \
                  `13_error` varchar(100) NULL,  `14_error` varchar(100) NULL, \
                  `15_error` varchar(100) NULL, `16_error` varchar(100) NULL, \
                  `17_error` varchar(100) NULL, `18_error` varchar(100) NULL, \
                  `19_error` varchar(100) NULL, `20_error` varchar(100) NULL, \
                  `21_error` varchar(100) NULL, `22_error` varchar(100) NULL, \
                  `23_error` varchar(100) NULL,  `24_error` varchar(100) NULL, \
                  `25_error` varchar(100) NULL,  `26_error` varchar(100) NULL, \
                  `27_error` varchar(100) NULL, `28_error` varchar(100) NULL, \
                  `29_error` varchar(100) NULL, `30_error` varchar(100) NULL)"

    connect = conn()
#    connect = sqlite3.connect("db")
    with connect:
    #    conn = connect.cursor()
        connect.execute(create_source)
        connect.execute(create_ids)
        connect.close
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

create_db()
#file_list = os.listdir(path = 'file/')
#for file in file_list:
#    read_file(file)
