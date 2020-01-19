#!/usr/bin/python
import os
#import sys
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
    date = int(date.timestamp())
    return date
def conn():
    connect = sqlite3.connect('data/mydb') # 'data/mydb'
    return connect
def create_db():
    """ create structure db """
    create_source = "CREATE TABLE IF NOT EXISTS `source` ( \
	           `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , \
            	  `phone` varchar(14) NOT NULL,  \
                  `time` varchar(20) NOT NULL, `ids` varchar(50) NOT NULL)"
    create_ids = "CREATE TABLE IF NOT EXISTS `ids` ( \
              	  `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , \
              	  `phone` varchar(14) NOT NULL, `date` INTEGER(20) NOT NULL, \
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

    create_source_index = "CREATE INDEX `phonees` ON `source` (`phone`, `time`)"
    create_ids_index = "CREATE INDEX `phone` ON `ids` (`phone`, `date`)"
    connect = conn()
    with connect:
        connect.execute(create_source)
        connect.execute(create_ids)
        connect.execute(create_source_index)
        connect.execute(create_ids_index)
        connect.close
        return True

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
        save_source(date, phone, source_ids)
        return 1

    else:
        response = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).\d{1,}.{1,}клиенту (\d{11,12}) отправлено: \{.{1,}failure\":(\d{1,}).{1,}\[(.{0,}\{\"error\":\"\w{1,}\"\}.{0,})\]", string)
        if response:
            date = serialase_date(response[1])
            phone = response[2]
            count_error = response[3]
            error = response[4]
            save_error(date, phone, error)
            return 1

def save_source(date, phone, source):
    """сохраняем данные об отправке"""
    sql= "INSERT INTO ids (phone, date) VALUES (?, ?)"
    connect = conn()
    cur = connect.cursor()
    try:
        with connect:
            cur.execute(sql, (phone, date))
            id = cur.lastrowid
            explod_ids = source.split(',')

            for num, ids in enumerate(explod_ids, start = 1):
                sql = "update ids set '{}_error' = '{}' where id = {}".format(num, ids, id)
                cur.execute(sql)

    except Exception as e:
        print(e)
def save_lor():
    pass
def save_error(date, phone, error):
    error_arr = error.split(',')
    for num, error in enumerate(error_arr, start=1):
        error_reg = re.search(r"(\"error\":\"NotRegistered|\"error\":\"MismatchSenderId\")", error)
        if error_reg:
            print(error_reg[1])
            ids = get_ids(phone, date, num)
            insert_error(phone, ids, date)
            #print(error_reg)
            print(phone, ids)
            write_report(phone, ids)


    #    write_report(phone, error)
def insert_error(phone, ids, date):
    print(phone, ids, date)
    try:
        sql = "INSERT INTO source (phone, time, ids) VALUES ('{}', '{}', '{}')".format(phone, date, ids)
        connect = conn()
        cur = connect.cursor()
        cur.execute(sql)
    except Exception as e:
        print(e)

def get_ids(phone, date, count):
    try:
        sql = "select `{}_error` from ids where phone='{}' and date BETWEEN '{}' and '{}'".format(count, phone, date-20, date)
        connect = conn()
        cur = connect.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for num, ids_tuple in enumerate(rows, start=1):
            if num > 1:
                print("В выборке найдена дополнительная строка с номером: "+phone+"\n")
                print(sql+"\n")
            if not ids_tuple[0]:
                print("в выборке нет данных: "+phone+"\n")
                print(sql+"\n")
            if num < 1:
                print(" на всякий случай 141 стр:"+phone+"\n")
                print(sql+"\n")

            ids = str(ids_tuple[0])
            return ids

    except Exception as e:
        print(e)
def write_report(phone, ids):

    """     """
    string = phone+" "+ids+"\n"
    with open("report-error.log", "a+") as f:
        f.write(string)
        f.close



                                            ######################################################################################################

create_db()
file_list = os.listdir(path = 'file/')
for file in file_list:
    read_file(file)
