# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import os
import time
import multiprocessing


class SimpleSpider:
    # def __init__(self,url,callback):
    #     self.a = 'a'
    #     self.url = url

    def crawl(self, url, options={}, callable=None):
        return requests.get(url, options)


def save_item():
    time.sleep(3)
    while True:
        print('saveitem')


def crawl():
    time.sleep(3)
    while True:
        print('crawl')


if(__name__ == '__main__'):
    pool = multiprocessing.Pool(processes=2)
    # for i in xrange(3):
    #     msg = "hello %d" %(i)
    #     pool.apply_async(func, (msg, ))
    pool.apply_async(save_item)
    pool.apply_async(crawl)
    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()    # behind close() or terminate()
    print("Sub-process(es) done.")
