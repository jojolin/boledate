# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BoledateItem(scrapy.Item):
    iid = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    picturls = scrapy.Field()
    like = scrapy.Field()
    collect = scrapy.Field()
    launch_time = scrapy.Field()
    place = scrapy.Field()

