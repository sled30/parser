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
                  `url` varchar(50) NOT NULL) "


    create_source_index = "CREATE INDEX `number_advert` ON `agregator` (`number_advert`)"
#    create_ids_index = "CREATE INDEX `phone` ON `ids` (`phone`, `date`)"
    connect = conn()
    with connect:
        connect.execute(create_source)
    #    connect.execute(create_ids)
        connect.execute(create_source_index)
    #    connect.execute(create_ids_index)
        connect.close
        return True

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
#        if len_rows == 0:
#            return True
#        else:
#             return False

        connect.close

    except Exception as e:
        print(e)
