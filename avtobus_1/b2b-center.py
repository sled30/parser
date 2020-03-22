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
#    print(page)

def parse_global_info(date):
    date = re.findall(r'<a href=\"(\/market\/[a-z-0-9]{3,}\/tender-\d{7}\/)\"[ a-z=\"-]{10,38}>([^<]{10,})<[^>]{10,39}>([^<]{4,})[^>].{42,}\"visited\">([^<]{3,})<.{27}(\d{2}.\d{2}.\d{4} \d{2}:\d{2}).{24}(\d{2}.\d{2}.\d{4} \d{2}:\d{2})', date)

    return date

def parse_advert(url):
    print(url)

def max_num_page(date):
    max_num = re.findall(r'a title=\"\d{1,5} - (\d{1,5})\" href=\"\/market\/[^>]{3,}>(\d{1,4})<', date)
#    print(max_num)

def get_region(date):
    region = re.search(r'Адрес места поставки товара, проведения работ или оказания услуг:</td><td>([^<]{5,})', date)

    return region[1]

def main():

    #https://www.b2b-center.ru/market/?f_keyword=%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81&searching=1&company_type=2&price_currency=0&date=1&trade=buy&lot_type=0#search-result
    uri = "https://www.b2b-center.ru"
    urn = "/market/?f_keyword=автобус&searching=1&company_type=2&price_currency=0&date=1&trade=all#search-result"
    url = uri + urn
    page = commun.get_page(url)
    dates = parse_global_info(page)
    max_num_page(page)

    for date in dates:
        check_ferst = commun.check_need_info(date[1])
        check_second = commun.check_need_info(date[2])

        if check_ferst or check_second:
            url = uri + date[0]
            advert_page = commun.get_page(url)
            region = get_region(advert_page)

        #    print(advert_page)
            #print(date)

            #print(url)
        #print(check_ferst, check_second)

main()

#<a href=\"(\/market\/[a-z-0-9]{3,}\/tender-\d{7}\/)\"[ a-z=\"-]{10,38}>([^<]{10,})<[^>]{10,39}>([^<]{4,})[^>].{42,}\"visited\">([^<]{3,})<.{27}(\d{2}.\d{2}.\d{4} \d{2}:\d{2}).{24}(\d{2}.\d{2}.\d{4} \d{2}:\d{2})
##
#a title=\"\d{1,5} - (\d{1,5})\" href=\"\/market\/\?from=\d{1,5}\">\d{1,5}</a>\n  #стараницы
##
#?f_keyword=автобус&searching=1&company_type=2&price_currency=0&date=1&trade=all&from=110#search-result # следующая
