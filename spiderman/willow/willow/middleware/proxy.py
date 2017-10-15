# -*- coding: utf-8 -*-

import random
from scrapy.conf import settings
import logging

logger = logging.getLogger("crawler.middleware.proxy")

class StaticProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = settings.get("PROXY")
        logger.info("process request %s using proxy %s" %(request, proxy)
        request.meta['proxy'] = proxy


class RandomProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = random.choice(settings.get('PROXY_LIST'))
        logger.info("process request %s using proxy %s" % (request, proxy))
        request.meta['proxy'] = proxy



