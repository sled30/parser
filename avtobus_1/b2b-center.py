#!/usr/bin/python

import re
import getinfo as commun

def get_urn_advert(page):
    try:
        urn = re.findall(r'<tr><td><a href="(\/market\/.{10,}\/)"', page)

        return urn

    except Exception as e:
        print('get_urn_advert')
        print(e)
def get_advert_settings(url):
    page = get_page(url)
    print(page)



#page = get_page(url)
#urn_adverts = get_urn_advert(page)
#for urn_advert in urn_adverts:
#    url_advert = uri + urn_advert
#    get_advert_settings(url_advert)
def main():
    #https://www.b2b-center.ru/market/?f_keyword=%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81&searching=1&company_type=2&price_currency=0&date=1&trade=buy&lot_type=0#search-result
    uri = "https://www.b2b-center.ru"
    urn = "/market/?f_keyword=%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81&searching=1&company_type=2&price_currency=0&date=1&trade=buy&lot_type=0#search-result"
    url = uri + urn
    page = commun.get_page(url)
    print(page)


main()
