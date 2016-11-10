# -*- coding: utf-8 -*-
import logging
from twisted.internet.error import TimeoutError
from scrapy.spidermiddlewares.httperror import HttpError
import scrapy

class XMiddleware(object):
    def __init__(self):
        pass

    def process_request(self, request, spider):
        pass
        # raise scrapy.exceptions.IgnoreRequest('test exception')

    def process_response(self, request, response, spider):
        raise HttpError(response, 'test exception')
        # raise scrapy.exceptions.IgnoreRequest('test exception')

    def process_exception(self, request, exception, spider):
        pass