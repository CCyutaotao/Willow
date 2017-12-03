# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy_splash import SplashRequest
from items import WillowItem

class AcademySpider(scrapy.Spider):
    name = 'academy'
    allowed_domains = ['uestc.edu.cn']
    start_urls = [
        'http://www.scie.uestc.edu.cn/',
        'http://www.ee.uestc.edu.cn/',
        'http://www.pe.uestc.edu.cn/',
        'http://www.ccse.uestc.edu.cn/',
        'http://www.auto.uestc.edu.cn/',
        'http://www.life.uestc.edu.cn/',
        'http://www.mgmt.uestc.edu.cn/',
        'http://www.fl.uestc.edu.cn/',
        'http://www.energy.uestc.edu.cn/',
        'http://www.iaa.uestc.edu.cn/index.asp',
        'http://www.med.uestc.edu.cn/',
        'http://www.yingcai.uestc.edu.cn/',
        'http://www.iffs.uestc.edu.cn/',
        'http://www.ncl.uestc.edu.cn/main/index/',
        'http://www.me.uestc.edu.cn/',
        'http://www.soei.uestc.edu.cn/',
        'http://www.is.uestc.edu.cn/',
        'http://sport.uestc.edu.cn/home',
        'http://www.gla.uestc.edu.cn/chinese/',
        'http://www.sre.uestc.edu.cn/',
        'http://www.rw.uestc.edu.cn/',
        'http://www.math.uestc.edu.cn/',
        'http://www.jxdz.uestc.edu.cn/',
        'http://121.41.25.203:8080/xsht/',
        'http://www.news.uestc.edu.cn/',
    ]
    URL = []

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait':0.5})


    def parse(self, response):
        html = response.body
        title = response.css('title').extract_first()
        urls = response.xpath('//a/@href').re('.*[0-9]+.+')
        for url in urls:
            if url in self.URL:
                continue
            else:
                self.URL.append(url)
            if url.startswith('/'):
                url = '/'.join(response.url.split('/')[0:3]) + url
            elif url.startswith('http') or url.startswith('www'):
                url = url
            else:
                if response.url.endswith('/'):
                    url = response.url + url
                else:
                    url = '/'.join(response.url.split('/')[0:-1]) + '/' + url
            yield SplashRequest(url, self.parse_content, args={'wait':0.5})

    def parse_content(self, response):
        html = response.body
        title = response.css('title').extract_first()
        now = datetime
        item = WillowItem()
        item['title'] = title
        item['url'] = response.url
        item['content'] = response.body
        item['now'] = datetime.datetime.now().strftime('%Y-%m-%d')