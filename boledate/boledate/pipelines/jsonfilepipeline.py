# -*- coding: utf-8 -*-
'''
Package: jsonfilepipeline.py
Author: ^-^
-----

'''
import logging
import json

class JsonfilePipeline(object):

    def __init__(self):
        self.f = open('/tmp/boledate-data.json', 'w')

    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item), encoding='utf-8')+'\n')
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        if self.f:
            self.f.close()
