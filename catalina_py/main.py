import os
import time

def read_file(file):
    with open('file/' + file,'r') as line:
        string = line.read().split()
        line.readline
        print(string)
    #    time.sleep(1)
def parser_source():
    pass
def save_source():
    pass
def save_lor():
    pass
def work_sqlite():
    pass


file_list = os.listdir(path = 'file/')
for file in file_list:
    read_file(file)
