# -*- coding: utf-8 -*-

import logging
from twisted.internet import task
from xcrawlutil.sql import replace_sql

class BufferPipeline(object):
    '''
    batch insert pipeline.
    '''
    def __init__(self):
        self.itemkeys = ['iid', 'title', 'content', 'update_time']

        self.buffer_size = 0
        self.buffer_limit = 1000
        self.item_buffer = []    # use queue instead.
        self.flush_interval = 120    # second
        # TODO: initialize others

    def open_spider(self, spider):
        # TODO: initialize others
        self.buffer_limit = spider.settings.get('ITEM_BUFFER_LIMIT', self.buffer_limit)
        self.flush_interval = spider.settings.get('ITEM_BUFFER_FLUSH_INTERVAL', self.flush_interval)
        task.LoopingCall(self.commit_interval).start(self.flush_interval)    # flush interval

    def process_item(self, item, spider):
        item['title'] = self._tickout_out_sep(item['title'])
        try:
            self.maybe_commit(item)
        except Exception as e:
            logging.error('commit failed, error: %s' % e)
        return item

    def close_spider(self, spider):
        pass

    def _tickout_out_sep(self, s):
        return s.strip().replace('\n',' ').replace('\r\n', ' ').replace('\t', ' ')

    def commit_interval(self):
        "flush buffer interval if buffer not empty"
        if self.buffer_size > 0:
           logging.debug('bufferpipeline interval commit')
           self._commit_buffer()

    def maybe_commit(self, item):
        "commit if reach buffer limit."
        self.item_buffer.append(item)
        self.buffer_size +=1
        self.buffer_size = self.buffer_size % self.buffer_limit
        if self.buffer_size == 0:
            logging.debug('bufferpipeline limit commit')
            self._commit_buffer()

    def _commit_buffer(self):
        "commit buffer"
        try:
            logging.info('commit items, num: %s' % len(self.item_buffer))
            # TODO: add commit logic
            # commit self.item_buffer:
            pass
        except Exception as e:
            logging.error('commit buffer error: %s' % e)
        finally:
            self.item_buffer = []    # flush
            self.buffer_size = 0    # reset
