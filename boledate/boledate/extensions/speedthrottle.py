# -*- coding: utf-8 -*-
import logging
from twisted.internet import task
from scrapy.exceptions import NotConfigured
from scrapy import signals

download_delay = 2

class SpeedThrottle(object):

    def __init__(self, crawler):
        self.crawler = crawler
        settings = crawler.settings

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler)
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(o.response_downloaded, signal=signals.response_downloaded)
        return o

    def spider_opened(self, spider):
        delay = self.read_download_delay() or download_delay
        spider.download_delay = int(delay)

    def throttle(self, request, spider):
        _, slot = self._get_slot(request, spider)
        delay = self.read_download_delay() or download_delay
        slot.delay = int(delay)

    def response_downloaded(self, response, request, spider):
        _, slot = self._get_slot(request, spider)
        latency = request.meta.get('download_latency')
        if latency is None or slot is None:
            return

        self.throttle(request, spider)

    def _get_slot(self, request, spider):
        key = request.meta.get('download_slot')
        return key, self.crawler.engine.downloader.slots.get(key)

    def read_download_delay(self):
        # TODO: add logci
        pass