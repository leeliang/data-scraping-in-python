# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ErshoufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    floor_plan = scrapy.Field()
    decoration_description = scrapy.Field()
    orientation = scrapy.Field()
    floor_description = scrapy.Field()
    area = scrapy.Field()
    built = scrapy.Field()
    community = scrapy.Field()
    district = scrapy.Field()
    plate = scrapy.Field()
    address = scrapy.Field()
    code = scrapy.Field()
    elevator_description = scrapy.Field()
    last_transaction_date = scrapy.Field()
    fengbennianxian = scrapy.Field()
    reason_for_sale = scrapy.Field()
    property = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    subway = scrapy.Field()
    open_date = scrapy.Field()