# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from chengjiao.items import ChengjiaoItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    #allowed_domains = ['lianjia.com']
    start_urls = ['http://sh.lianjia.com/chengjiao/']

    def parse(self, response):
        # 区
        selector = etree.HTML(response.text)
        district_href = selector.xpath("//div[@class='level1']/a[@class='level1-item ']/@href")
        #
        base_url = 'http://sh.lianjia.com'
        #
        for href in district_href:
            url = base_url + href
            yield scrapy.Request(url=url, callback=self.parse_district)

    #
    def parse_district(self,response):
        selector = etree.HTML(response.text)
        # 地块链接
        plate_href = selector.xpath("//div[@class='level2-item']/a/@href")[1:]
        #
        base_url = 'http://sh.lianjia.com'
        for href in plate_href:
            url = base_url + href
            yield scrapy.Request(url=url, callback=self.parse_plate,meta={'plate_url':url})
    #
    def parse_plate(self,response):
        selector = etree.HTML(response.text)
        # 某地块链接
        plate_url = response.meta['plate_url']
        #
        base_url = 'http://sh.lianjia.com'
        # 某地块房源总套数
        result_count = int(selector.xpath("//span[@class='result-count strong-num']/text()")[0])
        # 该地块页面数
        page_num = result_count/20 + 1
        #
        for page in range(page_num):
            url = plate_url + 'd' +str(page+1)
            print url
            yield scrapy.Request(url=url,callback=self.parse_page)
    #
    # #
    def parse_page(self,response):
        selector = etree.HTML(response.text)
        house_href = selector.xpath("//div[@class='info-table']/div[@class='info-row']/a/@href")
        for i,href in enumerate(house_href):
            item = ChengjiaoItem()
            item['code']  = href.split("/")[-1].split(".")[0]
            item['sold_date'] = selector.xpath("//div[@class='info-col deal-item main strong-num']/text()")[i]
            yield item



