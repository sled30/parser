import sqlite3

def conn():
    connect = sqlite3.connect('data/storageDB') # 'data/mydb'
    return connect
def create_db_agregator():
    """ create structure db """


    create_source = "CREATE TABLE IF NOT EXISTS `agregator` ( \
	           `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , \
                  `number_advert` varchar(20) NOT NULL, \
            	  `advert_text` varchar(20) NOT NULL,  \
                  `status` varchar(20) NOT NULL,\
                  `short_text_advert` varchar(50) NOT NULL, \
                  `name_organisation` varchar(50) NOT NULL, \
                  `long_text_advert` varchar(50) NOT NULL,  \
                  `advert_type` varchar(20) NOT NULL, \
                  `createtion_date` varchar(50) NOT NULL, \
                  `end_advert_date` varchar(50) NOT NULL, \
                  `region` varchar(50) NOT NULL, \
                  `date_of_conclusion` varchar(50) NOT NULL, \
                  `url` varchar(50) NOT NULL, `actual` varchar(50) NOT NULL) "


    create_source_index = "CREATE INDEX `number_advert` ON `agregator` (`number_advert`)"

    connect = conn()
    with connect:
        connect.execute(create_source)
        connect.execute(create_source_index)
        connect.close
        return True

def create_db_b2b():
    """ create structure db """


    create_source = "CREATE TABLE IF NOT EXISTS `b2b` ( \
	           `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , \
                  `number_advert` varchar(20) NOT NULL, \
            	  `advert_text` varchar(20) NULL,  \
                  `short_text_advert` varchar(50), \
                  `name_organisation` varchar(50) NOT NULL, \
                  `long_text_advert` varchar(50) NULL,  \
                  `advert_type` varchar(20), \
                  `createtion_date` varchar(50) NOT NULL, \
                  `end_advert_date` varchar(50) NOT NULL, \
                  `region` varchar(50) NOT NULL, \
                  `status` varchar(2), \
                  `date_of_conclusion` varchar(50), \
                  `url` varchar(50) NOT NULL, `actual` varchar(50)) "


    create_source_index = "CREATE INDEX `number_b2b` ON `b2b` (`number_advert`)"

    connect = conn()
    with connect:
        connect.execute(create_source)

        connect.execute(create_source_index)

        connect.close
        return True
def create_db_zakupki():
    create_source = "CREATE TABLE IF NOT EXISTS `zakupki` ( \
	           `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , \
                  `number_advert` varchar(20) NOT NULL, \
            	  `advert_text` varchar(20) NULL,  \
                  `short_text_advert` varchar(50), \
                  `name_organisation` varchar(50) NOT NULL, \
                  `long_text_advert` varchar(50) NULL,  \
                  `advert_type` varchar(20), \
                  `createtion_date` varchar(50) NOT NULL, \
                  `end_advert_date` varchar(50) NOT NULL, \
                  `region` varchar(50) NOT NULL, \
                  `status` varchar(2), \
                  `date_of_conclusion` varchar(50), \
                  `url` varchar(50) NOT NULL, `actual` varchar(50)) "


    create_source_index = "CREATE INDEX `number_zakupki` ON `zakupki` (`number_advert`)"

    connect = conn()
    with connect:
        connect.execute(create_source)

        connect.execute(create_source_index)

        connect.close
        return True
def save_b2b(date):
    try:

        sql = "INSERT INTO b2b (number_advert, \
                                      advert_text, \
                                      name_organisation, \
                                      createtion_date, \
                                      end_advert_date, \
                                      actual, \
                                      region, \
                                      url) \
                                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

        connect = conn()
        cur = connect.cursor()
        with connect:
            cur.execute(sql, (date[0], date[1], date[2], date[3], date[4], '1', date[5], date[6]))
        connect.close
    except Exception as e:
        print(e)

def save_zakupki(date):
    status = check_save_zakupki(number_advert)
    if status == True:
        try:
            sql = "INSERT INTO zakupki (number_advert, \
                                          advert_text, \
                                          name_organisation, \
                                          createtion_date, \
                                          end_advert_date, \
                                          actual, \
                                          region, \
                                          url, \
                                          status) \
                                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

            connect = conn()
            cur = connect.cursor()
            with connect:
                cur.execute(sql, ( date[0], date[1], date[2], date[4], date[5], '1', date[3], date[0], date[6]))
            connect.close
        except Exception as e:
            print(e)



def get_agregator():
    """   """

    try:
        sql = "SELECT `number_advert`, \
                      `advert_text`, \
                      `status`, \
                      `short_text_advert`, \
                      `name_organisation`, \
                      `advert_type`, \
                      `createtion_date`, \
                      `end_advert_date`, \
                      `date_of_conclusion`, \
                      `region`, \
                      `url` from agregator"


    #    sql = "select `number_advert` from agregator where number_advert='{}'".format(number_advert)
        connect = conn()
        cur = connect.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
        connect.close

    except Exception as e:
        print(e)

def get_b2b():
    """   """

    try:
        sql = "SELECT `number_advert`, \
                      `advert_text`, \
                      `name_organisation`, \
                      `createtion_date`, \
                      `end_advert_date`, \
                      `region`, \
                      `url`, \
                      `actual` \
                      from b2b"

        connect = conn()
        cur = connect.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
        connect.close

    except Exception as e:
        print(e)

def check_save_b2b(number_advert):

    try:
        sql = "select `number_advert` from b2b where number_advert='{}'".format(number_advert)
        connect = conn()
        cur = connect.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        len_rows = len(rows)
        if len_rows == 0:
            return True
        else:
             return False

        connect.close

    except Exception as e:
        print(e)

def check_save_zakupki(number_advert):

    try:
        sql = "select `number_advert` from zakupki where number_advert='{}'".format(number_advert)
        connect = conn()
        cur = connect.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        len_rows = len(rows)
        if len_rows == 0:
            return True
        else:
             return False

        connect.close

    except Exception as e:
        print(e)
def main():
    pass
