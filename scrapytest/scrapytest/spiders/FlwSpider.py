import scrapy
import re
from scrapytest.PostItmes import PostItem
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import logging


class FlwSpider(scrapy.Spider):
    name = 'FlwSpider'
    allowed_domains = ['flw.ph']
    start_urls = [
        # 论坛
        'http://www.flw.ph/forum-170-1.html',
        'http://www.flw.ph/forum-47-1.html',
        'http://www.flw.ph/forum-75-1.html',
        'http://www.flw.ph/forum-76-1.html',
        'http://www.flw.ph/forum-94-1.html',
        'http://www.flw.ph/forum-37-1.html',
        'http://www.flw.ph/forum-177-1.html',
        'http://www.flw.ph/forum-36-1.html',
        # 分类
        'http://www.flw.ph/forum-69-1.html',
        'http://www.flw.ph/forum-70-1.html',
        'http://www.flw.ph/forum-67-1.html',
        'http://www.flw.ph/forum-86-1.html'
        'http://www.flw.ph/forum-172-1.html',
        'http://www.flw.ph/forum-84-1.html'
    ]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
        'Referer': 'http://www.flw.ph/',
        'Cookie': '_uab_collina=152906119174453922491716; pgv_pvi=3040741590; _ga=GA1.2.1367026788.1529061192; pgv_info=ssi=s7443033456; _gid=GA1.2.515803561.1531360590; z67S_2132_pc_size_c=0; z67S_2132_saltkey=ia88esNr; z67S_2132_lastvisit=1531372042; z67S_2132_atarget=1; z67S_2132_visitedfid=170; _umdata=BA335E4DD2FD504F96FA0DFC13257AC6A01ED8B83A0C60F7C778AACD7507A1D9AB98C444C566382ECD43AD3E795C914CA7D1E6874EE9B794B58EDF00684DD2FB; z67S_2132_ulastactivity=bb17qd4Db63fEISY5d1PgwUmkem1nI9nAqkrq9AAyOv%2B%2B1%2FE3H3Q; z67S_2132_auth=ebfafVpd5L4kDO5yWa6zb6Sfl10SOfHsGaSfO67DRiCqxiPJo5hde8NjlB5yzsvMNedOzRLCFT%2FDUj%2FWPk2wFQ4Atg; z67S_2132_lastcheckfeed=63111%7C1531375681; CURAD=10; z67S_2132_myrepeat_rr=R0; z67S_2132_connect_is_bind=0; z67S_2132_smile=1D1; z67S_2132_st_t=63111%7C1531381784%7C9959a8e714405dc906be93a8a87a0bbc; z67S_2132_forum_lastvisit=D_170_1531381784; z67S_2132_viewid=tid_390292; _gat_gtag_UA_41770192_1=1; z67S_2132_sendmail=1; z67S_2132_st_p=63111%7C1531383604%7C277dfecd74a9e1df6f0b658b2ffc18fc; z67S_2132_sid=f8I2zy; z67S_2132_lip=157.52.154.68%2C1531383609; z67S_2132_lastact=1531383613%09misc.php%09patch'
    }

    base_url = "http://www.flw.ph/"
    # rules = (
    #     Rule(LinkExtractor(allow=('forum-\d+-\d+\.html',)),callback='parse_list', follow=True),
    #     Rule(LinkExtractor(allow=('thread-\d+-1-1.html')), callback='parse_info'),
    # )

    # def start_requests(self):
    #     return [scrapy.FormRequest("http://www.flw.ph/member.php?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login", headers=self.headers, meta={"cookiejar": 1}, callback=self.parse_before_login)]

    # def parse_before_login(self, response):
    #     print(response)
    #     for url in self.start_urls:
    #         yield self.make_requests_from_url(url)

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')

        nextA = soup.select('#ct a.nxt')
        info_lists = soup.select('#threadlisttableid > tbody th > a.s.xst')

        for info_item in info_lists:
            info_url = self.base_url + info_item['href']
            self.log("go to info page>>"+info_url)
            req_info = scrapy.Request(
                info_url, callback=self.parse_info, headers=self.headers)
            yield req_info

        self.log(len(info_lists))

        if(len(nextA) > 0):
            next_url = self.base_url + nextA[0]["href"]
            self.log("go to next page>>"+next_url)
            yield scrapy.Request(next_url, callback=self.parse)
        # print(response.url)

    def parse_info(self, response):
        try:
            item = PostItem()
            soup = BeautifulSoup(response.body, 'lxml')
            _str_id = re.findall(
                r'http://www.flw.ph/thread-(.*)-1-\d+.html', response.url)
            _str_qid = re.findall(r'http://www.flw.ph/forum.php\?mod=viewthread&tid=(.*)', response.url)
            if(len(_str_id) > 0):
                item['str_id'] = _str_id[0]
            elif (len(_str_qid) > 0):
                item['str_id'] = _str_qid[0]
            else:
                self.log("url error>>"+response.url, level=logging.ERROR)
            item['title'] = soup.select('#thread_subject')[0].get_text()

            item['content'] = str(soup.select(
                '#postlist table.plhin div.thread_body div.pcb')[0])
            item['category'] = soup.select('#pt > div > a')[-2].get_text()
            # item['reply_count'] = soup.select(
            #     '#ct > div.display-z.cl > div > div.thread_all > div.post_t > div.mtn > div > span.notes-info-icon.reply-icon')[0].get_text()
            # item['reply_count'] = soup.select(
            #     '#ct > div.display-z.cl > div > div.thread_all > div.post_t > div.mtn > div > span.notes-info-icon.show-icon')[0].get_text()
            item['url'] = response.url

            time = soup.select(
                '#ct > div.display-z.cl > div > div.thread_all > div.post_t > div.mtn > div')
            reg_result = re.findall(
                r'<div class="xg1">时间：(.*) <span class="notes-info-icon reply-icon" title="回复">(.*)</span> <span class="notes-info-icon show-icon" title="查看">(.*)</span> <span class="pipe">(.*)', str(time))
            if len(reg_result) > 0:
                item['creat_time'] = reg_result[0][0]
                item['reply_count'] = reg_result[0][1]
                item['watch_count'] = reg_result[0][2]
            # re.findall(r'$<div class="xg1">'
            # self.log("parse infomation >>")
            self.log(item)

            yield item
        except Exception as e:
            self.log('catch error>>>',e, level=logging.ERROR)
