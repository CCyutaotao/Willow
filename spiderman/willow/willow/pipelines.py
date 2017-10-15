# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from pymongo import IndexModel, ASCENDING
from items import WillowItem


class WillowPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient("localhost", 27017)
        db = client["willow"]
        self.academy = db["academy"]
        idx = IndexModel([('title',ASCENDING)], unique=True)
        self.academy.create_indexes([idx])

    def process_item(self, item, spider):
        if isinstance(item, WillowItem):
            print 'academy  True'
        try:
            self.academy.insert_one({'title':item['title']})
        except Exception:
            pass

        return item
