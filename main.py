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

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


class Crawler:
    def __init__(self):
        self.session = requests.session()
        # self.db = DB()
        self.crawl_timestamp = int()

    def run(self):
        while True:
            self.crawler()
            time.sleep(600)

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
                county_name = []
                county_number = []
                flag = True
                for county in county_information:
                    if flag:
                        county_name.append(county.string.extract())
                        flag = False
                    else:
                        county_number.append(county.string.extract())
                        flag = True

                t = PrettyTable(['County', 'Positive Cases'])
                for i, j in zip(county_name, county_number):
                    t.add_row([i, j])
                print(t)

            if not update_time or not county_information:
                continue

            break

        logger.info('Successfully crawled.')

    def update_time_parser(self, update_time):
        print(update_time.string.extract())
        print()

    # def state_parser(self, state_information, soup):
    # county_name = soup.find_all('td', attrs={'data-th': 'County'})
    # count_number = soup.find_all('td', attrs={'data-th': 'Positive Cases'})
    # county_name = state_information.find
    # count_number = soup.find_all('td', attrs={'data-th': 'Positive Cases'})
    # print("Display table content:\n")
    # print(county_name)
    # print()
    # print(count_number)
    # print()


if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
