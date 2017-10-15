# -*- coding: utf-8 -*-
import scrapy

from scrapy_splash import SplashRequest
from willow.items import WillowItem

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

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait':0.5})


    def parse(self, response):
        html = response.body
        title = response.css('title').extract_first()
        item = WillowItem()
        item['title'] = title
        yield item

        pass
