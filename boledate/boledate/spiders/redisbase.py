# -*- coding: utf-8 -*-
'''
redis source.
'''
import logging
import redis

class RedisBase(object):

    def __init__(self, *args, **kwargs):
        '''
        Initialize spider and get the url.
        '''
        super(RedisBase, self).__init__()

        self.sp_project = kwargs.pop('spider_project', '')
        self.sp_name = kwargs.pop('spider_name', '')
        self.redis_host = 'localhost'
        self.redis_port = 6379
        self.redis_pwd =''
        self.redis_key = ''
        self.url_seprator = '@@'
        self.server = None

    def push_back_item(self, crawl_item):
        self.server.lpush(self.redis_key, self.crawl_item)

    def discard_item(self, crawl_item):
        # TODO: maybe log to somewhere
        pass

    def push_back_item(self, crawl_item):
        # TODO: maybe log to somewhere
        pass

    def setup(self, settings):
        self.url_seprator = settings.get('URL_SEPRATOR', self.url_seprator)
        self.redis_host  = settings.get('REDIS_HOST', self.redis_host)
        self.redis_port  = settings.get('REDIS_PORT', self.redis_port)
        self.redis_pwd =  settings.get('REDIS_PASSWORD', None)
        self.server = redis.Redis(host=self.redis_host,
                                  port=self.redis_port,
                                  password=self.redis_pwd)
        self.redis_key = self.get_redis_key(self.sp_project, self.sp_name)
        logging.info('Read crawl item from redis "(%s:%s)%s"' \
                     % (self.redis_host, self.redis_port, self.redis_key))

    def next_crawl_item(self):
        '''
        get next request from redis.
        '''
        return self.server.rpop(self.redis_key)

    def get_url_meta_from_crawl_item(self, crawl_item):
        url, ct = crawl_item.split(self.url_seprator)
        return url, {'category': ct}

    def get_redis_key(self, project, name):
        return '%s:%s:crawl-items' % (project, name)