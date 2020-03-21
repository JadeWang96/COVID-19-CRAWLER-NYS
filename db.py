"""
@ProjectName: DXY-2019-nCov-Crawler
@FileName: db.py
@Author: Jiabao Lin
@Date: 2020/1/21
@Modifier: Jade Wang
@Data: 2020/3/20
"""
from pymongo import MongoClient


class DB:
    client = None
    db = None

    def __init__(self, host, port, db_name):
        self.client = MongoClient("mongodb://%s:%s/" % (host, port))
        self.db = self.client[db_name]

    def insert(self, collection, data):
        self.db[collection].insert(data)

    def find_one(self, collection, data=None):
        return self.db[collection].find_one(data)


Mongo = DB(host='172.17.0.2', port=27017, db_name='new_york_state')
