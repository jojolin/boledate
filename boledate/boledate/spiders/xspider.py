# -*- coding: utf-8 -*-
'''
Package: xxsp.py
Author: ^-^
-----
xx spider
'''
import logging

from .spiderbase import SpiderBase
from boledate.items import BoledateItem
from boledate.utils.misc import attach_comm_meta

class XSpider(SpiderBase):
    name = 'x'
    proxy_domain = name
    url_domain = ''

    def __init__(self, *args, **kwargs):
        '''
        Initialize spider and get the url.
        '''
        SpiderBase.__init__(self, *args, **kwargs)

    def parse_items(self, response):
        logging.info('parse_items, url: %s' % response.url)
        meta = self.get_attach_meta(response)
        next_url = self.get_next_url(response)
        logging.info('next_url %s' % next_url)
        if next_url:
            yield scrapy.Request(url=next_url,
                                 meta=attach_comm_meta(self, meta),
                                 callback=self.parse_items)
        items = self.ex_items(response)
        logging.info('len of extract items: %s url: %s' % (len(items), response.url))
        for item in items:
            yield item

    def get_attach_meta(self, response):
        return {}

    def get_next_url(self, response):
        pass

    def ex_items(self, response):
        # TODO: extract items
        items = []
        item = BoledateItem()
        title = response.xpath('//title/text()').extract()[0]
        print title
        item['title'] = title
        items.append(item)
        return items