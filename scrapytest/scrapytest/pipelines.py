# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from sqlalchemy import Column, Integer, DateTime, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()


class Content(Base):
    # 表的名字:
    __tablename__ = 'content1'
    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    str_id = Column(String)
    title = Column(String)
    content = Column(String)
    category = Column(String)
    create_time = Column(String)
    reply_count = Column(Integer)
    watch_count = Column(Integer)
    url = Column(String)


class ScrapytestPipeline(object):
    def process_item(self, item, spider):
        return item


class FLWDataPipeline(object):
    def process_item(self, item, spider):
        # print('==========================================\n')
        # print("mysql save >>>>"+item['str_id'])
        # print('\n')
        str_id = item['str_id']
        # engine = create_engine(
        #     'mysql+mysqlconnector://root:root@localhost:3306/test2?charset=utf8')
        
        # DBSession = sessionmaker(bind=engine)
        # session = DBSession()
        ret = self.session.query(Content).filter_by(str_id=str_id).first()
        if ret == None:
            self.session.add(Content(str_id=item["str_id"], title=item["title"], content=item["content"], category=item["category"],
                                     create_time=item["creat_time"], reply_count=item["reply_count"], watch_count=item["watch_count"], url=item["url"]))
        else:
            self.session.query(Content).filter_by(str_id=str_id).update({"title": item["title"], "content": item["content"], "category": item[
                "category"], "create_time": item["creat_time"], "reply_count": item["reply_count"], "watch_count": item["watch_count"], "url": item["url"]})
        self.session.commit()
        return item

    def __init__(self):
        # 初始化数据库连接:
        self.engine = create_engine(
            'mysql+mysqlconnector://root:root@localhost:3306/test2?charset=utf8')
        # 创建DBSession类型:
        self.DBSession = sessionmaker(bind=self.engine)

        self.session = self.DBSession()
