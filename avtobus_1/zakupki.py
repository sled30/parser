import getinfo as commun
import re
#1
# https://zakupki.mos.ru/purchase/list?page=1&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22typeIn%22%3A%5B3%2C2%5D%2C%22nameLike%22%3A%22%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81%22%2C%22regionPaths%22%3A%5B%22.174936.%22%2C%22.123117.%22%2C%22.113362.%22%2C%22.148668.%22%2C%22.150644.%22%2C%22.91030.%22%2C%22.89253.%22%2C%22.76248.%22%2C%22.71049.%22%2C%22.70021.%22%2C%22.56969.%22%2C%22.45000.%22%2C%22.38590.%22%2C%22.1626.%22%2C%22.35803.%22%2C%22.157500.%22%2C%22.4422.%22%2C%22.2231.%22%2C%22.1668.%22%5D%2C%22startPriceGreatEqual%22%3A0%2C%22startPriceLessEqual%22%3A500000%2C%22publishDateGreatEqual%22%3A%2222.03.2020%2000%3A00%3A00%22%2C%22publishDateLessEqual%22%3A%2223.03.2020%2023%3A59%3A59%22%2C%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B20000002%5D%7D%2C%22tenderSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B5%5D%7D%7D&state=%7B%22currentTab%22%3A1%7D

#2
#https://zakupki.mos.ru/purchase/list?page=1&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22typeIn%22%3A%5B3%2C2%5D%2C%22startPriceGreatEqual%22%3A500000%2C%22publishDateGreatEqual%22%3A%2219.03.2020%2000%3A00%3A00%22%2C%22publishDateLessEqual%22%3A%2223.03.2020%2023%3A59%3A59%22%2C%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B20000002%5D%7D%2C%22tenderSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B5%5D%7D%7D&state=%7B%22currentTab%22%3A1%7D

#https://zakupki.mos.ru/purchase/list?page=1&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22typeIn%22%3A%5B3%2C2%5D%2C%22nameLike%22%3A%22%D0%BF%D0%BE%D0%B3%D1%83%D0%BB%D1%8F%D1%88%D0%BA%D0%B8_______%22%2C%22regionPaths%22%3A%5B%22.504.%22%2C%22.81809.%22%5D%2C%22publishDateGreatEqual%22%3A%2219.03.2020%2000%3A00%3A00%22%2C%22publishDateLessEqual%22%3A%2223.03.2020%2023%3A59%3A59%22%2C%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B20000002%5D%7D%2C%22tenderSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B5%5D%7D%7D&state=%7B%22currentTab%22%3A1%7D

#url = 'https://zakupki.mos.ru/purchase/list?page=1&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22typeIn%22%3A%5B3%2C2%5D%2C%22nameLike%22%3A%22%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81%22%2C%22regionPaths%22%3A%5B%22.174936.%22%2C%22.123117.%22%2C%22.113362.%22%2C%22.148668.%22%2C%22.150644.%22%2C%22.91030.%22%2C%22.89253.%22%2C%22.76248.%22%2C%22.71049.%22%2C%22.70021.%22%2C%22.56969.%22%2C%22.45000.%22%2C%22.38590.%22%2C%22.1626.%22%2C%22.35803.%22%2C%22.157500.%22%2C%22.4422.%22%2C%22.2231.%22%2C%22.1668.%22%5D%2C%22startPriceGreatEqual%22%3A0%2C%22startPriceLessEqual%22%3A500000%2C%22publishDateGreatEqual%22%3A%2222.03.2020%2000%3A00%3A00%22%2C%22publishDateLessEqual%22%3A%2223.03.2020%2023%3A59%3A59%22%2C%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B20000002%5D%7D%2C%22tenderSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B5%5D%7D%7D&state=%7B%22currentTab%22%3A1%7D'


#test = "https://zakupki.mos.ru/purchase/list?page=1&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22typeIn%22%3A%5B3%2C2%5D%2C%22publishDateGreatEqual%22%3A%2219.03.2020%2000%3A00%3A00%22%2C%22publishDateLessEqual%22%3A%2223.03.2020%2023%3A59%3A59%22%2C%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B20000002%5D%7D%2C%22tenderSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B5%5D%7D%7D&state=%7B%22currentTab%22%3A1%7D"
#page = commun.get_page(test)


def parse_global_info(page):
    try:
        regexp = re.compile(r'MainInfoNameHeader-\w{2}-[\d\w]{5,7}-\d [a-zA-Z\d]{5,7}\">[<span>]{,8}([^<]{3,}).{50,100}(https://[a-z.]{18}/#/[a-z]{9}/\d{6,9}).{30,100}MainInfoCustomerHeader-[^>]{3,}>([^<]{3,}).{300,400}PriceInfoNumber-[\w\d]{2}-[\d\w]{3,}-\d\W[\w]{2}-[\w]{3,5}\">[^<]{2,}.{100,300}alt=\"\">[<span>]{,6}([^<]{3,}).{100,300}alt=\"\">[<span>]{,6}([^<]{,30})')

        info = regexp.findall(page)
        return info

    except Exception as e:
        print('error zakupki parse_global_info(page)')
        print(e)


def get_max_num_page(page):
    try:
        regexp = re.compile(r'pageItem\" class=\"item\">(\d{1,})<')

        number_page = regexp.findall(page)
        print(number_page)
        if len(number_page) > 0:
            max_number = max(number_page, key=int)
            return max_number

        else:
            return False

    except Exception as e:
        print('zakupki get_max_num_page(page)')
        print(e)


def check_find_page(page, link):
#    print(link)
    regexp = re.compile(r'Найдено <b>([^<])')
    find = regexp.findall(page)
    print("find  ", find)
    if len(find) > 0:
        
        return page

    else :
        page = commun.get_page(link)
        check_find_page(page, link)
        return page
    #else:
    #    return True


def logic_zakupki(link, state):
    page = commun.get_page(link)

    status = check_find_page(page, link)
    if status == False:
        print("не найдено")
        return False
    #print(status)
    info = parse_global_info(status)

    if state == 'start':
        max_page = get_max_num_page(status)
        ## TODO: save
        return max_page
    elif state == 'load':
        print('save')

def phase_1():
    #https://zakupki.mos.ru/purchase/list?page=1&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22typeIn%22%3A%5B3%2C2%5D%2C%22nameLike%22%3A%22%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81%22%2C%22regionPaths%22%3A%5B%22.174936.%22%2C%22.123117.%22%2C%22.113362.%22%2C%22.148668.%22%2C%22.150644.%22%2C%22.91030.%22%2C%22.89253.%22%2C%22.76248.%22%2C%22.71049.%22%2C%22.70021.%22%2C%22.56969.%22%2C%22.45000.%22%2C%22.38590.%22%2C%22.1626.%22%2C%22.35803.%22%2C%22.157500.%22%2C%22.4422.%22%2C%22.2231.%22%2C%22.1668.%22%5D%2C%22startPriceGreatEqual%22%3A0%2C%22startPriceLessEqual%22%3A500000%2C%22publishDateGreatEqual%22%3A%2222.03.2020%2000%3A00%3A00%22%2C%22publishDateLessEqual%22%3A%2223.03.2020%2023%3A59%3A59%22%2C%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B20000002%5D%7D%2C%22tenderSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B5%5D%7D%7D&state=%7B%22currentTab%22%3A1%7D
    uri = "https://zakupki.mos.ru/purchase/list?page="
    #urn = "&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22typeIn%22%3A%5B3%2C2%5D%2C%22nameLike%22%3A%22%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81%22%2C%22regionPaths%22%3A%5B%22.174936.%22%2C%22.123117.%22%2C%22.113362.%22%2C%22.148668.%22%2C%22.150644.%22%2C%22.91030.%22%2C%22.89253.%22%2C%22.76248.%22%2C%22.71049.%22%2C%22.70021.%22%2C%22.56969.%22%2C%22.45000.%22%2C%22.38590.%22%2C%22.1626.%22%2C%22.35803.%22%2C%22.157500.%22%2C%22.4422.%22%2C%22.2231.%22%2C%22.1668.%22%5D%2C%22startPriceGreatEqual%22%3A0%2C%22startPriceLessEqual%22%3A500000%2C%22publishDateGreatEqual%22%3A%2222.03.2020%2000%3A00%3A00%22%2C%22publishDateLessEqual%22%3A%2223.03.2020%2023%3A59%3A59%22%2C%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B20000002%5D%7D%2C%22tenderSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B5%5D%7D%7D&state=%7B%22currentTab%22%3A1%7D"

    urn = "&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%7D%2C%22tenderSpecificFilter%22%3A%7B%7D%7D&state=%7B%22currentTab%22%3A1%7D"
    link = uri + str(1) + urn


    max_page = logic_zakupki(link, 'start')
    for page in range(2, int(max_page)):
        link = uri + str(page) + urn
        logic_zakupki(link, 'loader')







def main():
    pass


phase_1()
############################################################################################################################
############################################################################################################################
############################################################################################################################
#1&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%7D%2C%22tenderSpecificFilter%22%3A%7B%7D%7D&state=%7B%22currentTab%22%3A1%7D
#uri = "https://zakupki.mos.ru/purchase/list?page="
#urn = "&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%7D%2C%22tenderSpecificFilter%22%3A%7B%7D%7D&state=%7B%22currentTab%22%3A1%7D"

#link = uri + str(1) + urn
#url = link + base_page
#print(link)

#page = commun.get_page(link)

#

#info = parse_global_info(page)
#print(info)
#if len(info)< 1:
#    page = commun.get_page(link)

#    #
#    info = parse_global_info(page)
#    print(info)

#max_page = get_max_num_page(page)
#for value in info:
#    print(value)
#print(max_page)
#if max_page is not False:
#    for num in range(2, int(max_page)):
#        link = uri + str(num) + urn
#        logic_zakupki(link)
