# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient
from itemadapter import ItemAdapter


class NewsPipeline:
    def __init__(self):
        self.conn = MongoClient("127.0.0.1", 27017, username = "admin", password = "956659")
        db = self.conn['donyaye_tahlil']
        self.collection = db['news']
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
