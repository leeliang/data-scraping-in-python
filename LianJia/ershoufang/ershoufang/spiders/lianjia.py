# -*- coding: utf-8 -*-
import scrapy
import re
from lxml import etree
from ershoufang.items import ErshoufangItem

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    #allowed_domains = ['lianjia.com']
    start_urls = ['https://sh.lianjia.com/ershoufang/']

    def parse(self, response):
        # 区
        selector = etree.HTML(response.text)
        district_href = selector.xpath("//div[@class='position']/dl[2]/dd/div[1]/div/a/@href")
        #
        base_url = 'https://sh.lianjia.com'
        #
        for href in district_href:
            url = base_url + href
            yield scrapy.Request(url=url, callback=self.parse_district)


    def parse_district(self,response):
        selector = etree.HTML(response.text)
        # 地块链接
        plate_href = selector.xpath("//div[@class='position']/dl[2]/dd/div[1]/div[2]/a/@href")
        #
        base_url = 'https://sh.lianjia.com'
        for href in plate_href:
            url = base_url + href
            #print url
            yield scrapy.Request(url=url, callback=self.parse_plate,meta={'plate_url':url})

    def parse_plate(self,response):
        selector = etree.HTML(response.text)
        # 某地块链接
        plate_url = response.meta['plate_url']
        #
        base_url = 'https://sh.lianjia.com'
        # 某地块房源总套数
        result_count = int(selector.xpath("//h2[@class='total fl']/span/text()")[0])
        # 该地块页面数
        page_num = result_count/30 + 1
        #
        for page in range(page_num):
            url = plate_url + '/pg' +str(page+1)
            yield scrapy.Request(url=url,callback=self.parse_page)
    # #
    # # #
    def parse_page(self,response):
        selector = etree.HTML(response.text)
        house_href = selector.xpath("//div[@class='info clear']/div[@class='title']/a/@href")
        #base_url = 'https://sh.lianjia.com'
        for href in house_href:
            #url = base_url + href

            yield scrapy.Request(url=href,callback=self.parse_house)
            #
    def parse_house(self,response):
        item = ErshoufangItem()
        selector = etree.HTML(response.text)
        # 总价格
        total_price = selector.xpath("//div[@class='price ']/span[@class='total']/text()")
        item['total_price'] = total_price
        print total_price
        # 单位价格
        unit_price = selector.xpath("//div[@class='unitPrice']/span[@class='unitPriceValue']/text()")
        item['unit_price'] = unit_price
        # 房型，朝向，装修水平，楼层，面积，建造年费
        main_info = selector.xpath("//div[@class='houseInfo']/div/div/text()")
        item['floor_plan'] = main_info[0].strip()
        item['decoration_description'] = main_info[3].strip()
        item['orientation'] = main_info[2].strip()
        item['floor_description'] = main_info[1].strip()
        item['area'] = main_info[4].strip()
        item['built'] = main_info[5].strip()
        # 小区名字、地区名字、地块名字
        name_info = selector.xpath("//div[@class='aroundInfo']//a/text()")
        item['community'] = name_info[0].strip()
        item['district'] = name_info[2].strip()
        item['plate'] = name_info[3].strip()
        # 地址
        #item['address'] = selector.xpath("//span[@class='item-cell maininfo-estate-address']/text()")[0].strip()
        # 房屋编号
        item['code'] = selector.xpath("//div[@class='houseRecord']/span[@class='info']/text()")[0]
        # 电梯
        content = selector.xpath("//div[@class='base']/div[@class='content']/ul/li/text()")
        item['elevator_description'] = content[10] + '('+ content[9] +')'
        # 交易信息
        sale_info = selector.xpath("//div[@class='transaction']/div[@class='content']/ul/li/span[2]/text()")
        item['open_date'] = sale_info[0].strip()
        item['last_transaction_date'] = sale_info[2].strip()
        item['fengbennianxian'] = sale_info[4].strip()
        #item['reason_for_sale'] = sale_info[].strip()
        item['property'] = sale_info[3].strip()
        # 经纬度
        item['latitude'] = re.findall(r"resblockPosition:\'(.*?),(.*?)\'", response.text)[0][1]
        item['longitude'] = re.findall(r"resblockPosition:\'(.*?),(.*?)\'", response.text)[0][0]
        # # 地铁信息
        # subway_info = selector.xpath("//script//text()")[1]
        # subway = subway_info.splitlines()[-5].split(':')[1].replace("'", '')
        # if len(subway):
        #     item['subway'] = subway
        # else:
        #     item['subway'] = None
        #
        # #print item
        yield item



