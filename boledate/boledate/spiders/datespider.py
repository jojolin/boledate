# -*- coding: utf-8 -*-
'''
Package: xxsp.py
Author: ^-^
-----
xx spider
'''
import logging
import re

from .spiderbase import SpiderBase
from boledate.items import BoledateItem
from boledate.utils.misc import attach_comm_meta

class DateSpider(SpiderBase):
    name = 'date'
    proxy_domain = name
    url_domain = 'http://date.jobbole.com/'

    def __init__(self, *args, **kwargs):
        '''
        Initialize spider and get the url.
        '''
        SpiderBase.__init__(self, *args, **kwargs)

    def parse_items(self, response):
        logging.info('parse_items, url: %s' % response.url)
        meta = self.get_attach_meta(response)
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
        title = response.css('li.media > div.media-body > h1::text').extract()[0]
        if title.find(u'］') > -1:
            return []

        launch_time = response.css('li.media > div.media-body > p.p-meta > span::text').extract()[0]
        place = response.css('li.media > div.media-body > p.p-meta > span > a::text').extract()[0]
        content = response.css('div.p-entry > p::text').extract()
        picturls = response.css('div.p-entry > p > img::attr(src)').extract()
        like, collect = '0', '0'
        try:
            like = response.css('div#share-buttons > a')[0].css('h10::text').extract()[0]
        except IndexError:
            like = '0'
        try:
            collect = re.search('\d+', \
                    ''.join(response.css('div#share-buttons > a')[1].css('::text').extract())).group(0)
        except Exception:
            collect = '0'

        item['iid'] = title
        item['title'] = title
        item['content'] = content
        item['picturls'] = picturls
        item['like'] = like
        item['collect'] = collect
        item['launch_time'] = launch_time
        item['place'] = place
        items.append(item)
        return items
