# -*- coding: utf-8 -*-
'''
Package: redispipeline.py
Author: ^-^
-----

'''

import logging
from twisted.internet import task
import redis

redis_host = '127.0.0.1'
redis_port = 6379
redis_db = 0
redis_key_xx = ''

# write buffer to redis
class RedisBufferPipeline(object):
    '''
    batch insert pipeline.
    '''
    def __init__(self):
        self.itemkeys = ['iid', 'title', 'content', 'update_time']
        self.redis_cli = None

    def open_spider(self, spider):
        self.redis_host = spider.settings.get('REDIS_HOST', redis_host)
        self.redis_port = spider.settings.getint('REDIS_PORT', redis_port)
        self.redis_pwd =  spider.settings.get('REDIS_PASSWORD', None)
        self.redis_db = spider.settings.get('REDIS_DB', redis_db)
        self.redis_key = spider.settings.get('REDIS_KEY_XX', redis_key_xx)

        self.conn_redis()

    def conn_redis(self):
        if not self.redis_cli:
            self.redis_cli = redis.Redis(self.redis_host, self.redis_port, self.redis_db, self.redis_pwd)

    def maybe_commit(self, item):
        try:
            self.conn_redis()
            # TODO: do commit logic
            # self.redis_cli.lpush(self.rd_key_items, sql)
            # self.redis_cli.ltrim(self.rd_key_items, 0, self.maxnum_xx)
        except Exception as e:
            logging.error('commit buffer error: %s' % e)

    def process_item(self, item, spider):
        item['title'] = self._tickout_out_sep(item['title'])
        try:
            self.maybe_commit(item)
        except Exception as e:
            logging.error('commit failed, error: %s' % e)
        return item

    def close_spider(self, spider):
        pass
