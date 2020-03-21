'''
@COVID-19 Crawler for North America
@Author: Jade Wang
@Time: March 2020
@Reference: DXY-2019-nCov-Crawler Project by Jiabao Lin
'''
from bs4 import BeautifulSoup
# from db import DB
# from userAgent import user_agent_list
from nameMap import state_name_map, new_york_county_map
import re
import json
import time
import random
import logging
import requests
from prettytable import PrettyTable
import csv
import sys
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


class Crawler:
    def __init__(self, csv_name=None):
        self.session = requests.session()
        # self.db = DB()
        self.crawl_timestamp = int()
        self.csv_name = csv_name

    def run(self):
        while True:
            self.crawler()
            time.sleep(6000)  # It's unnecessary to be a small interval

    def crawler(self):
        while True:
            # self.session.headers.update(
            #     {
            #         'user-agent': random.choice(user_agent_list)
            #     }
            # )
            self.crawl_timestamp = int(time.time() * 1000)
            try:
                r = self.session.get(url='https://coronavirus.health.ny.gov/county-county-breakdown-positive-cases')
            except requests.exceptions.ChunkedEncodingError:
                continue
            soup = BeautifulSoup(r.content, 'lxml')
            update_time = soup.find('div', attrs={'class': 'wysiwyg--field-webny-wysiwyg-title'})
            if update_time:
                self.update_time_parser(update_time=update_time)

            county_information = soup.find_all("td")
            if county_information:
                self.county_parser(county_information=county_information)

            if not update_time or not county_information:
                continue

            break

        logger.info('Successfully crawled.')

    def update_time_parser(self, update_time):
        print(
            "\nNew York State Government Official Website, Department of Health \n"
            "https://coronavirus.health.ny.gov/county-county-breakdown-positive-cases")
        print(update_time.string.extract())
        print()

    def county_parser(self, county_information):
        county_name = []
        county_number = []
        county_number_str = []
        flag = True
        for county in county_information:
            if flag:
                county_name.append(county.string.extract())
                flag = False
            else:
                county_str = county.string.extract()
                county_number_str.append(county_str)  # Easier to read with ,
                str_num = int(county_str.replace(',', ''))
                county_number.append(str_num)
                flag = True

        if self.csv_name:
            self.csv_output(county_name=county_name, county_number=county_number)

        self.console_output(county_name=county_name, county_number=county_number_str)

    def console_output(self, county_name, county_number):
        t = PrettyTable(['County', 'Positive Cases'])
        for i, j in zip(county_name, county_number):
            t.add_row([i, j])
        print(t)

    def csv_output(self, county_name, county_number):
        new_path = r'./Output'
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        csv_path = os.path.join(new_path, self.csv_name)
        with open(csv_path, 'w', newline='') as csvfile:
            fieldnames = ['County', 'Positive Cases']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i, j in zip(county_name, county_number):
                writer.writerow({'County': i, 'Positive Cases': j})
            csvfile.close()
        print("Successfully output as ", self.csv_name)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        crawler = Crawler(sys.argv[1])
    else:
        crawler = Crawler()

    crawler.run()
