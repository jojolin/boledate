# -*- coding: utf-8 -*-
'''
misc.
'''

def attach_comm_meta(spider, meta):
    m = {
        'banned_times_limit': spider.banned_times_limit,
        'timeout_times_limit': spider.timeout_times_limit
    }
    m.update(meta)
    return m
