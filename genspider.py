#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Package: genspider.py
Author: ^-^
-----
generate spider module
require scrapyenv
'''

from os import path
from jinja2 import Template, Environment
from xutil.xprint import iprint

PATH_HERE = path.dirname(path.abspath(__file__))
PROJECT = path.basename(PATH_HERE)

def fmt_platform(platform):
    "return format platform"
    tickouts = " -':,.@&"
    plt = platform
    for tk in tickouts:
        plt = plt.replace(tk, '')
    return plt.lower()

def fmt_country(country):
    return fmt_platform(country)

def fmt_cls_name(platform, country):
    return '%s%s' % (fmt_platform(platform).capitalize(),
                     fmt_country(country).capitalize())

def fmt_spider_name(platform, country):
    return '%s_%s' % (fmt_platform(platform), fmt_country(country))

def fmt_cls_platform(platform):
    return fmt_platform(platform).capitalize()

def fmt_cls_country(country):
    return fmt_country(country).capitalize()

def gen(tplt_file, save_file, spider_config):
    tplt = None
    env = Environment()
    # add cusmom filter
    env.filters['fmt_platform'] = fmt_platform
    env.filters['fmt_country'] = fmt_country
    env.filters['fmt_cls_name'] = fmt_cls_name

    with open(tplt_file, 'r') as r:
        tplt = env.from_string(r.read())

    res = tplt.render(config=spider_config)
    if not save_file:
        save_file = tplt_file.replace('.tplt','')
    g = True
    if path.exists(save_file):
        r = raw_input('WARNNING: %s existed, overrite?(y/N): ' % save_file)
        if r.upper() == 'N':
            g = False
            iprint('cancel genspider', color='y')
    if g:
        with open(save_file, 'w') as w:
            w.write(res)
        iprint('generate %s successfully!' % save_file, color='g')

def get_file_name(config):
    d = {}
    d['platform'] = fmt_platform(config['platform'])
    d['country'] = fmt_country(config['country'])
    return d

import argparse
def parse_arguments():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('platform',
                        help='platform name')
    parser.add_argument('country',
                        help='country name abbr. e.g. USA')
    return parser.parse_args()

def main():
    spider_dir = path.join(PATH_HERE, '%s/%s/spiders' % (PROJECT, PROJECT))
    tplt_file = path.join(PATH_HERE, 'spider.py.tplt')
    args = parse_arguments()
    plt = args.platform
    c = args.country
    if plt == '' or c =='':
        iprint('invalid platform or country', color='y')
    spider_config = {'platform' : plt,
                     'country' : c,
                     'spider_name': fmt_spider_name(plt, c),
                     'spider_class': fmt_cls_name(plt, c)}
    save_file = path.join(spider_dir, '%(platform)s%(country)sspider.py' \
                          % get_file_name(spider_config))
    gen(tplt_file, save_file, spider_config)

if __name__ == '__main__':
    main()
