import gspread
from oauth2client.service_account import ServiceAccountCredentials
import db
import time

# use creds to create a client to interact with the Google Drive API


def aut_sheet():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('tender-271908-439d364b4c77.json', scope)
    client = gspread.authorize(creds)

    return client

def open_sheet():
    """     """
    client = aut_sheet()
    sheet = client.open('Работа с тендерами').sheet2



    return sheet

def open_phase_1():
    """     """
    client = aut_sheet()
    sheet = client.open('Работа с тендерами').worksheet('фаза 1')

    return sheet_phase

def open_phase_2():
    """     """
    client = aut_sheet()

    sheet = client.open('Работа с тендерами').worksheet('фаза 2')

    return sheet_phase

def open_phase_3():
    """     """
    client = aut_sheet()

    sheet = client.open('Работа с тендерами').worksheet('фаза 3')

    return sheet_phase

def open_phase_4():
    """     """
    client = aut_sheet()

    sheet = client.open('Работа с тендерами').worksheet('фаза 4')

    return sheet_phase

def check_row_in_sheet(number):
    """    """
    sheet = open_sheet()
    find = sheet.findall(number)
    if len(find) > 0:
        return False
    else:
        return True
def save_report_zakupki():
    date = db.get_zakupki()
    sheets = open_sheet()

    for row in date:
        time.sleep(4)
        print(row)
        print(row[6])
        sheets.insert_row(row)


def save_report_agregator():
    """    """
    dates = db.get_agregator()

    sheets = open_sheet()

    for date in dates:
        status = check_row_in_sheet(date[0])

        if status == True:
            sheets.insert_row(date)

        else:
            pass
def save_report_b2b():
    dates = db.get_b2b()

    sheets = open_sheet()

    for date in dates:
        status = check_row_in_sheet(date[0])

        if status == True:
            in_write = (date[0],date[1], 'Null', 'Null', date[2], 'Null', date[3], date[4], 'Null', date[5], date[6])
            sheets.insert_row(in_write)

        else:
            pass

def main():
    """   """

    #save_report_agregator()
#    save_report_b2b()
    save_report_zakupki()

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################


main()
