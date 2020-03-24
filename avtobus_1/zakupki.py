import getinfo as commun
import re
#1
# https://zakupki.mos.ru/purchase/list?page=1&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22typeIn%22%3A%5B3%2C2%5D%2C%22nameLike%22%3A%22%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81%22%2C%22regionPaths%22%3A%5B%22.174936.%22%2C%22.123117.%22%2C%22.113362.%22%2C%22.148668.%22%2C%22.150644.%22%2C%22.91030.%22%2C%22.89253.%22%2C%22.76248.%22%2C%22.71049.%22%2C%22.70021.%22%2C%22.56969.%22%2C%22.45000.%22%2C%22.38590.%22%2C%22.1626.%22%2C%22.35803.%22%2C%22.157500.%22%2C%22.4422.%22%2C%22.2231.%22%2C%22.1668.%22%5D%2C%22startPriceGreatEqual%22%3A0%2C%22startPriceLessEqual%22%3A500000%2C%22publishDateGreatEqual%22%3A%2222.03.2020%2000%3A00%3A00%22%2C%22publishDateLessEqual%22%3A%2223.03.2020%2023%3A59%3A59%22%2C%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B20000002%5D%7D%2C%22tenderSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B5%5D%7D%7D&state=%7B%22currentTab%22%3A1%7D

#2
#https://zakupki.mos.ru/purchase/list?page=1&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22typeIn%22%3A%5B3%2C2%5D%2C%22startPriceGreatEqual%22%3A500000%2C%22publishDateGreatEqual%22%3A%2219.03.2020%2000%3A00%3A00%22%2C%22publishDateLessEqual%22%3A%2223.03.2020%2023%3A59%3A59%22%2C%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B20000002%5D%7D%2C%22tenderSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B5%5D%7D%7D&state=%7B%22currentTab%22%3A1%7D

#https://zakupki.mos.ru/purchase/list?page=1&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22typeIn%22%3A%5B3%2C2%5D%2C%22nameLike%22%3A%22%D0%BF%D0%BE%D0%B3%D1%83%D0%BB%D1%8F%D1%88%D0%BA%D0%B8_______%22%2C%22regionPaths%22%3A%5B%22.504.%22%2C%22.81809.%22%5D%2C%22publishDateGreatEqual%22%3A%2219.03.2020%2000%3A00%3A00%22%2C%22publishDateLessEqual%22%3A%2223.03.2020%2023%3A59%3A59%22%2C%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B20000002%5D%7D%2C%22tenderSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B5%5D%7D%7D&state=%7B%22currentTab%22%3A1%7D

url = 'https://zakupki.mos.ru/purchase/list?page=1&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22typeIn%22%3A%5B3%2C2%5D%2C%22nameLike%22%3A%22%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81%22%2C%22regionPaths%22%3A%5B%22.174936.%22%2C%22.123117.%22%2C%22.113362.%22%2C%22.148668.%22%2C%22.150644.%22%2C%22.91030.%22%2C%22.89253.%22%2C%22.76248.%22%2C%22.71049.%22%2C%22.70021.%22%2C%22.56969.%22%2C%22.45000.%22%2C%22.38590.%22%2C%22.1626.%22%2C%22.35803.%22%2C%22.157500.%22%2C%22.4422.%22%2C%22.2231.%22%2C%22.1668.%22%5D%2C%22startPriceGreatEqual%22%3A0%2C%22startPriceLessEqual%22%3A500000%2C%22publishDateGreatEqual%22%3A%2222.03.2020%2000%3A00%3A00%22%2C%22publishDateLessEqual%22%3A%2223.03.2020%2023%3A59%3A59%22%2C%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B20000002%5D%7D%2C%22tenderSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B5%5D%7D%7D&state=%7B%22currentTab%22%3A1%7D'


test = "https://zakupki.mos.ru/purchase/list?page=1&perPage=10&sortField=relevance&sortDesc=true&filter=%7B%22typeIn%22%3A%5B3%2C2%5D%2C%22publishDateGreatEqual%22%3A%2219.03.2020%2000%3A00%3A00%22%2C%22publishDateLessEqual%22%3A%2223.03.2020%2023%3A59%3A59%22%2C%22auctionSpecificFilter%22%3A%7B%7D%2C%22needSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B20000002%5D%7D%2C%22tenderSpecificFilter%22%3A%7B%22stateIdIn%22%3A%5B5%5D%7D%7D&state=%7B%22currentTab%22%3A1%7D"
page = commun.get_page(test)


def parse_global_info(page):
    regexp = re.compile(r'MainInfoNameHeader-\w{2}-[\d\w]{5,7}-\d [a-zA-Z\d]{5,7}\">[<span>]{,8}([^<]{3,}).{50,100}(https://[a-z.]{18}/#/[a-z]{9}/\d{6,9}).{30,100}MainInfoCustomerHeader-[^>]{3,}>([^<]{3,}).{300,400}PriceInfoNumber-[\w\d]{2}-[\d\w]{3,}-\d\W[\w]{2}-[\w]{3,5}\">[^<]{2,}.{100,300}alt=\"\">[<span>]{,6}([^<]{3,}).{100,300}alt=\"\">[<span>]{,6}([^<]{,30})')

    info = regexp.findall(page)
    return info

def get_max_num_page(page):
    regexp = re.compile(r'pageItem\" class=\"item\">(\d{1,4})<')
    number_page = regexp.findall(page)
    if number_page[1]:
        max_number = max(number_page, key=int)
        return max_number

    else:
        return 0


def logic_zakupki():
    page = commun.get_page(test)
    parse_global_info(page)




def main():
    pass
############################################################################################################################
############################################################################################################################
############################################################################################################################

page = commun.get_page(test)
max_page = get_max_num_page(page)
print(max_page)
