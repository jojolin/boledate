# -*- coding=utf8 -*-
import time
import redis
import requests
from lxml import etree

REDIS_HOST = 'your.redis.host'
REDIS_PORT = your.redis.port
REDIS_PWD = 'your.reids.password'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'}
TIMEOUT = 20
CRAWL_INTERVAL = 1
REDIS_KEY = 'boledate:date:crawl-items'

def get_page_tree(url):
    res = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    tree = etree.fromstring(res.text, parser=etree.HTMLParser())
    return tree

def get_nxt_pg_url(tree):
    nxt_url = tree.xpath('//li[@id="pagination-next-page"]/a/@href')
    return nxt_url[0] if nxt_url else None

def parse_items(tree):
    items = tree.xpath('//li[@class="media"]//h3[@class="p-tit"]/a')
    for u in items:
        tit = u.xpath('text()')[0]
        url = u.xpath('@href')[0]
        yield (url,  tit)
        # print tit, url
    nxt_pg_url = get_nxt_pg_url(tree)
    if nxt_pg_url:
        time.sleep(CRAWL_INTERVAL)
        for i in parse_items(get_page_tree(nxt_pg_url)):
            yield i

def parse(st_url):
    tree = get_page_tree(st_url)
    items = parse_items(tree)
    server = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PWD)
    for url, tit in items:
        server.lpush(REDIS_KEY, '@@'.join([url, tit]))
        print 'push item to redis: %s' % tit

def main():
    st_url = 'http://date.jobbole.com/'
    parse(st_url)

if __name__ == '__main__':
    main()
