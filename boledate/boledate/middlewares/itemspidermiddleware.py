# -*- coding: utf-8 -*-
'''
Package: itemspidermiddleware.py
Author: ^-^
-----

'''

from boledate.items import BoledateItem

class ItemSpiderMiddleware(object):
    '''
    item spider middleware for wrapping crawled item.
    '''

    def process_spider_output(self, response, result, spider):
        for item in result:
            if isinstance(item, BoledateItem):
                # TODO: set default item field
                # item.setdefault('iid', '')
                pass
            yield item
