# -*- coding: utf-8 -*-
import time
import pymysql
from xcrawlutil.sql import replace_sql

class MysqlPipeline(object):
    def __init__(self):
        self.itemkeys = ['iid', 'title', 'content' 'update_time']

    def open_spider(self, spider):
        self.host = spider.settings['MYSQL_HOST']
        self.user = spider.settings['MYSQL_USER']
        self.db = spider.settings['MYSQL_DB']
        self.password = spider.settings['MYSQL_PASSWORD']

        tb_name = '%s_%s' % (spider.settings['MYSQL_TB_NAME'], spider.name)
        self.item_sql = replace_sql(tb_name,
                                    '''`id`, `title`, `content`, `update_time`''')
        self.connection = self.connect_mysql(self.host, self.user, self.password, self.db)

    def process_item(self, item, spider):
        item['title'] = self._tickout_out_sep(item['title'])
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(self.item_sql, tuple([item[k].encode('utf8') for k in self.itemkeys]))
                self.connection.commit()
        except pymysql.err.OperationalError as e:
            if 2006 == e.args[0]:    # 'Broken pipe'
                self.connection = self.connect_mysql(self.host, self.user, self.password, self.db)
            if self.connection:    # reconnected succeed
                cursor.execute(self.item_sql, tuple([item[k].encode('utf8') for k in self.itemkeys]))
                self.connection.commit()
            else:    # failed
                raise e
        except Exception as e:
            logging.error('mysql process item error %s' %e)
            raise e

        return item

    def close_spider(self, spider):
        if self.connection:
            self.connection.close()

    def connect_mysql(self, host, user, password, db, times=10, interval=2):
        t = times
        connection = None
        while t > 0:
            try:
                connection = pymysql.connect(host, user, password, db,
                                             charset='utf8',
                                             cursorclass=pymysql.cursors.DictCursor)
            except pymysql.err.OperationalError as e:
                logging.error('mysql connection(%s time), error: %s' % (times-t, e))     # failed
                time.sleep(interval)
            else:
                break    # succeed
            t -= 1
        return connection

    def _tickout_out_sep(self, s):
        return s.strip().replace('\n',' ').replace('\r\n', ' ').replace('\t', ' ')