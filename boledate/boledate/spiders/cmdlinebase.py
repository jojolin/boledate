# -*- coding: utf-8 -*-
'''
Package: debugbase.py
Author: ^-^
-----
command line source.
'''
import Queue

class CmdlineBase(object):

    def __init__(self, *args, **kwargs):
        self.debug_items = Queue.Queue()
        self.debug_items.put(kwargs.get('debug-item'))

    def next_crawl_item(self):
        try:
            return self.debug_items.get(False)
        except Queue.Empty:
            return None

    def get_url_meta_from_crawl_item(self, crawl_item):
        url, ct = crawl_item.split('@@')
        return url, {'category': ct}

    def discard_item(self, crawl_item):
        pass

    def push_back_item(self, crawl_item):
        pass

    def setup(self, settings):
        pass
