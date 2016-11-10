# -*- coding: utf-8 -*-
import logging
from twisted.internet.error import TimeoutError
import scrapy

class TimeoutMiddleware(object):
    def __init__(self):
        pass

    def inc_meta_value(self, request, meta_key):
        if meta_key in request.meta:
            request.meta[meta_key] += 1
        else:
            request.meta[meta_key] = 1

    def process_exception(self, request, exception, spider):
        timeout_times_limit = request.meta['timeout_times_limit']
        logging.error('TimeoutMiddleware catch exception: %s' % exception)
        if isinstance(exception, TimeoutError):
            logging.error('timeout, url: %s' % request.url)
            self.inc_meta_value(request, 'timeout-times')
            if request.meta['timeout-times'] > timeout_times_limit:
                raise scrapy.exceptions.IgnoreRequest('timeout')
            return request    # re scheduled
        return None