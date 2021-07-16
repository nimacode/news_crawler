# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class NewsPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb+srv://admin:admin@localhost/news_crawler?retryWrites=true&w=majority")
        db = self.conn['news_crawler']
        self.collection = db['news']
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
