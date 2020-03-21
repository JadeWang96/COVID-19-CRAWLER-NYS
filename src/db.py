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

    def __init__(self, db_name):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]

