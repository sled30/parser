import getinfo as commun
import re
import db


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

        if len(number_page) > 0:
            max_number = max(number_page, key=int)
            return max_number

        else:
            return False

    except Exception as e:
        print('zakupki get_max_num_page(page)')
        print(e)


def check_find_page(page, link):
    regexp = re.compile(r'Найдено <b>([^<])')
    find = regexp.findall(page)
    if len(find) > 0:

        return page

    else :
        page = commun.get_page(link)
        check_find_page(page, link)
        return page
    #else:
    #    return True
def serialize_date(string):

    first = re.search(r'с\W(\d{2}.\d{2}.\d{4})', string)
    if first is None:
        first = ('No found',"")
    end_date = re.search(r'до\W(\d{2}.\d{2}.\d{4})', string)
    if end_date is None:
        second = ('No found',"")


    return (first[0], end_date[0])

def logic_zakupki(link, state, phase):
    page = commun.get_page(link)

    status = check_find_page(page, link)

    if status == False:

        return False
    #status_find = commun.check_need_info()

    info = parse_global_info(status)

    if state == 'start':
        max_page = get_max_num_page(status)
        if info:

            for row in info:
                status_load = commun.check_need_info(row[0])
                print(row[0])
                print(status_load)
                if status_load == True:
                    date_advert = serialize_date(row[4])
                    date = (row[1], row[0], row[2], row[3], date_advert[0], date_advert[1], phase,)

                    db.save_zakupki(date)


        return max_page
    elif state == 'loader':
        if info:
            for row in info:
                status_load = commun.check_need_info(row[0])
                if status_load == True:
                    date_advert = serialize_date(row[4])
                    date = (row[1], row[0], row[2], row[3], date_advert[0], date_advert[1], phase,)

                    db.save_zakupki(date)




def phase_1():
    uri = "https://zakupki.mos.ru/purchase/list?page="

    load_keyword = commun.find_string(1)
    date = commun.get_time()

    for search in load_keyword:


        urn1 = '&perPage=10&sortField=relevance&sortDesc=true&filter={"typeIn"%3A[3%2C2]%2C"nameLike"%3A"' + search + '"%2C"'
        urn2 = 'regionPaths"%3A[".174936."%2C".123117."%2C".113362."%2C".148668."%2C".150644."%2C".91030."%2C".89253."%2C".76248."%2C".71049."%2C".70021."%2C".56969."%2C".45000."%2C".38590."%2C".1626."%2C".35803."%2C".157500."%2C".4422."%2C".2231."%2C".1668."]%2C"startPriceGreatEqual"%3A0%2C"startPriceLessEqual"%3A500000%2C"publishDateGreatEqual"%3A"' + date[0] + ' 00%3A00%3A00"%2C"publishDateLessEqual"%3A"' + date[1] + ' 23%3A59%3A59"%2C"auctionSpecificFilter"%3A{}%2C"needSpecificFilter"%3A{"stateIdIn"%3A[20000002]}%2C"tenderSpecificFilter"%3A{"stateIdIn"%3A[5]}}&state={"currentTab"%3A1}'

        link = uri + str(1) + urn1 + urn2

#        print('#################################')
#        print('#################################')
#        print(search)
#        print(link)
#        print('#################################')
#        print('#################################')

        max_page = logic_zakupki(link, 'start', '1')

        for page in range(2, int(max_page)):

            link = uri + str(page) + urn1 + search + urn2

            logic_zakupki(link, 'loader', '1')


def phase_2():
    uri = "https://zakupki.mos.ru/purchase/list?page="

    load_keyword = commun.find_string(2)
    date = commun.get_time()

    for search in load_keyword:


        urn1 = '&perPage=10&sortField=relevance&sortDesc=true&filter={"typeIn"%3A[3%2C2]%2C"nameLike"%3A"' + search + '"%2C"'
        urn2 = 'startPriceGreatEqual"%3A500000%2C"publishDateGreatEqual"%3A"' + date[0] +' 00%3A00%3A00"%2C"publishDateLessEqual"%3A"' + date[1] +' 23%3A59%3A59"%2C"auctionSpecificFilter"%3A{}%2C"needSpecificFilter"%3A{"stateIdIn"%3A[20000002]}%2C"tenderSpecificFilter"%3A{"stateIdIn"%3A[5]}}&state={"currentTab"%3A1}'

        link = uri + str(1) + urn1 + urn2

#        print('#################################')
#        print('#################################')
#        print(search)
#        print(link)
#        print('#################################')
#        print('#################################')

        max_page = logic_zakupki(link, 'start', '2')

        for page in range(2, int(max_page)):

            link = uri + str(page) + urn1 + search + urn2

            logic_zakupki(link, 'loader', '2')

def phase_3():

    uri = "https://zakupki.mos.ru/purchase/list?page="

    date = commun.get_time()

    load_keyword = commun.find_string(3)
    for search in load_keyword:


        urn1 = '&perPage=10&sortField=relevance&sortDesc=true&filter={"typeIn"%3A[3%2C2]%2C"nameLike"%3A"' + search + '"%2C"'
        urn2 = 'publishDateGreatEqual"%3A"' + date[0] + ' 00%3A00%3A00"%2C"publishDateLessEqual"%3A"' + date[1]+ '23%3A59%3A59"%2C"auctionSpecificFilter"%3A{}%2C"needSpecificFilter"%3A{"stateIdIn"%3A[20000002]}%2C"tenderSpecificFilter"%3A{"stateIdIn"%3A[5]}}&state={"currentTab"%3A1}'

        link = uri + str(1) + urn1 + urn2

#        print('#################################')
#        print('#################################')
#        print(search)
#        print(link)
#        print('#################################')
#        print('#################################')

        max_page = logic_zakupki(link, 'start', '3')

        for page in range(2, int(max_page)):

            link = uri + str(page) + urn1 + search + urn2

            logic_zakupki(link, 'loader', '3')
def phase_4():

    uri = "https://zakupki.mos.ru/purchase/list?page="

    date = commun.get_time()

    load_keyword = commun.find_string(4)
    for search in load_keyword:


        urn1 = '&perPage=10&sortField=relevance&sortDesc=true&filter={"typeIn"%3A[3%2C2]%2C"nameLike"%3A"' + search + '"%2C"'
        urn2 = 'regionPaths"%3A[".504."%2C".81809."]%2C"publishDateGreatEqual"%3A"' + date[0] + ' 00%3A00%3A00"%2C"publishDateLessEqual"%3A"'+ date[1] +'23%3A59%3A59"%2C"auctionSpecificFilter"%3A{}%2C"needSpecificFilter"%3A{"stateIdIn"%3A[20000002]}%2C"tenderSpecificFilter"%3A{"stateIdIn"%3A[5]}}&state={"currentTab"%3A1}'

        link = uri + str(1) + urn1 + urn2

#        print('#################################')
#        print('#################################')
#        print(search)
#        print(link)
#        print('#################################')
#        print('#################################')

        max_page = logic_zakupki(link, 'start', '4')

        for page in range(2, int(max_page)):

            link = uri + str(page) + urn1 + search + urn2

            logic_zakupki(link, 'loader', '4')



def main():
    pass


phase_1()
phase_2()
phase_3()
phase_4()
