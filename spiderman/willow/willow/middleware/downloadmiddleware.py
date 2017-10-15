# -*- coding: utf-8 -*-
import random
import json
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from static_useragents import agents
from static_cookies import cookie
import logging

class RandomUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent=''):
        self.logger = logging.getLogger("crawler.middleware.randomua")
        self.user_agent = user_agent


    def process_request(self, request, spider):
        ua = random.choice(agents)
        if request.headers.get('User-Agent') is not None:
            return
        request.headers.setdefault('User-Agent', ua)
        self.logger.info("process request %s using random ua: %s" % (request, ua))




class CookiesMiddleware(object):

    def process_request(self, request, spider):
        bs = ''
        for i in range(32):
            bs += chr(random.randint(97, 122))
        _cookie = json.dumps(cookie) % bs
        request.cookies = json.loads(_cookie)


