# -*- coding: utf-8 -*-
'''
Package: spiderbase.py
Author: ^-^
-----

'''

import sys
import logging
import scrapy
from scrapy import signals
from scrapy.exceptions import DontCloseSpider

from cmdlinebase import CmdlineBase
from redisbase import RedisBase
from boledate.utils.misc import attach_comm_meta

class SpiderBase(scrapy.Spider):
    name = ''
    project = 'boledate'

    timeout_times_limit = 3
    banned_times_limit = 3

    def __init__(self, *args, **kwargs):
        '''
        Initialize spider and get the url.
        '''
        super(SpiderBase, self).__init__()
        self.crawl_item = None
        # set source instance
        if kwargs.get('debug-item', None):
            self.src_ins = CmdlineBase(*args, **kwargs)
            print '***** entering debug-mode'
        else:
            self.src_ins = RedisBase(*args,
                                     spider_project=self.project,
                                     spider_name=self.name)

    def close(self, reason):
        if not reason == 'finished':
            logging.info('%s close, reason: %s' % (self.name, reason))
            self.push_back_item(self.crawl_item)

    def parse_failure(self, failure):
        url = failure.request.url
        logging.info('failed request url: %(url)s, type:%(type)s, value:%(value)s',
                     {'url':url, 'type': failure.type, 'value': failure.value})
        logging.error('parse_failure, request meta:%s' % failure.request.meta)
        if failure.type is scrapy.exceptions.IgnoreRequest:
            if failure.value == 'timeout':
                self.discard_item(self.crawl_item)
            elif failure.value == 'banned':
                self.push_back_item(self.crawl_item)

    def discard_item(self, crawl_item):
        # TODO: maybe log to somewhere
        if crawl_item:
            logging.info('discard crawl_item to redis: %s' % self.crawl_item)
            self.src_ins.discard_item(self.crawl_item)

    def push_back_item(self, crawl_item):
        # TODO: maybe log to somewhere
        if crawl_item:
            logging.info('push back crawl_item to redis: %s' % self.crawl_item)
            self.src_ins.pusl_back_item(self.crawl_item)

    def _set_crawler(self, crawler):
        '''
        This method overrite Spider's _set_crawler to setup redis.
        called after the __init__.
        '''
        super(SpiderBase, self)._set_crawler(crawler)
        self.crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)
        self.setup_log()
        self.src_ins.setup(self.crawler.settings)

    def setup_log(self):
        "when in debug-mode, log to file and print on screen"
        run_mode = self.crawler.settings.get('RUN_MODE', 'release')
        log_level = self.crawler.settings.get('LOG_LEVEL', 'INFO')
        if run_mode.find('debug') > -1 or run_mode.find('DEBUG') > -1:
            log_file = '/tmp/spider-%s.log' % self.name
            fh = logging.FileHandler(log_file, mode='w')
            fh.setLevel(getattr(logging, log_level))
            logging.root.addHandler(fh)
            logging.info('logging in log file: %s' % log_file)

    def spider_idle(self):
        self.schedule_next_request()
        raise DontCloseSpider

    def schedule_next_request(self):
        """Schedules a request if available"""
        req = self.next_request()
        if req:
            self.crawler.engine.crawl(req, spider=self)

    def next_request(self):
        '''
        get next request.
        overwrite super's method to support multiple parsers
        '''
        self.crawl_item = self.src_ins.next_crawl_item()
        if self.crawl_item:
            logging.info('read crawl_item: "%s"' % self.crawl_item)
            url, meta = self.src_ins.get_url_meta_from_crawl_item(self.crawl_item)
            return scrapy.Request(url=url,
                                  meta=attach_comm_meta(self, meta),
                                  dont_filter=True,
                                  callback=self.parse_items,
                                  errback=self.parse_failure)
        else:
            return None

    def parse_items(self, response):
        "overrite by child class."
        raise NotImplementedError