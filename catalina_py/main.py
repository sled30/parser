import os
import sys
import re
import time

def read_file(file):
    with open('file/' + file) as line:
        for row in line:
            parser(row)
    line.close()
def parser(string):
    source = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{1,3}).{1,}для клиента (\d{11,12}).{1,}\[(.{1,})\]", string)
    if source:
        return 1
        #print(source[1])
    else:
        response = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).\d{1,}.{1,}клиенту (\d{11,12}) отправлено: \{.{1,}failure\":(\d{1,}).{1,}\[(.{0,}\{\"error\":\"\w{1,}\"\}.{0,})\]", string)
        if response:
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
