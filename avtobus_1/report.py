import gspread
from oauth2client.service_account import ServiceAccountCredentials
import db

# use creds to create a client to interact with the Google Drive API


def aut_sheet():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('tender-271908-439d364b4c77.json', scope)
    client = gspread.authorize(creds)

    return client

def open_sheet():
    """     """
    client = aut_sheet()
    sheet = client.open('Работа с тендерами').sheet1

    return sheet
def save_report_agregator():
    """    """
    dates = db.get_agregator()

    sheets = open_sheet()

    for date in dates:
        sheets.insert_row(date)



def main():
    """   """

    save_report_agregator()

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################


main()
