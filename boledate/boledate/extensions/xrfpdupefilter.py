# -*- coding: utf-8 -*-
'''
Package: xrfpdupefilter.py
Author: ^-^
-----
this package is used for overriting the behavior of default dupefilter
'''

import time
import logging

from scrapy.utils.job import job_dir
from scrapy.dupefilters import RFPDupeFilter

EXPIRE_TIME = 60 * 60 * 10   # seconds

class XRFPDupeFilter(RFPDupeFilter):
    '''
    extend the default RFPDupeFilter
    '''
    def __init__(self, expire_time, path=None, debug=False):
        super(XRFPDupeFilter, self).__init__(path, debug)
        self.last_cache_time = time.time()
        self.expire_time = expire_time
        logging.info('enabled extensions.xrfpdupefilter.XRFPDupeFilter, expire_time: %s' \
                     % self.expire_time)

    @classmethod
    def from_settings(cls, settings):
        debug = settings.getbool('DUPEFILTER_DEBUG')
        expire_time = settings.getint('DUPEFILTER_EXPIRE_TIME', EXPIRE_TIME)
        return cls(expire_time, job_dir(settings), debug)

    def request_fingerprint(self, request):
        "overrite super class to make requests not filtered by scrapy."
        if time.time() - self.last_cache_time > self.expire_time:
            self.fingerprints = set()
            self.last_cache_time = time.time()
            logging.info('update fingerprints')
        return super(XRFPDupeFilter, self).request_fingerprint(request)