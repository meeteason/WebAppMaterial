import scrapy


class PostItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    str_id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    creat_time = scrapy.Field()
    category = scrapy.Field()
    reply_count = scrapy.Field()
    watch_count = scrapy.Field()
    url = scrapy.Field()
    # pass
