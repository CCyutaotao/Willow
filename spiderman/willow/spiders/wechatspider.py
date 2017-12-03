# -*- coding: utf-8 -*-
import scrapy


class WechatspiderSpider(scrapy.Spider):
    name = 'wechatspider'
    allowed_domains = ['sougou.com']
    start_urls = ['http://weixin.sogou.com/']

    def parse(self, response):
        pass
