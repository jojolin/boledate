# -*- coding: utf-8 -*-
'''
Package: monitormiddleware.py
Author: ^-^
-----

'''
import logging

class InspectMiddleware(object):
    def __init__(self):
        pass

    def process_response(self, request, response, spider):
        msg = 'REQUEST INFO: request.proxy: %s, request.url: %s, response.url: %s, response.body length: %s ' \
              % (request.meta.get('proxy', 'NO PROXY'), request.url, response.url, len(response.body))
        logging.info(msg)
        return response
