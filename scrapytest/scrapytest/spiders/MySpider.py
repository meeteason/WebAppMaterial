import scrapy
import re
from scrapytest.PostItmes import PostItem
from bs4 import BeautifulSoup


class MySpider(scrapy.Spider):
    name = 'MySpider'
    allowed_domains = ['flw.ph']
    start_urls = [
        'http://www.flw.ph/forum-40-1.html',
        # 'http://www.flw.ph/forum-170-1.html',
        # 'http://www.flw.ph/forum-37-1.html',
        # 'http://www.flw.ph/forum-177-1.html'
        # 'http://www.flw.ph/forum.php?mod=guide&view=hot'
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name',
               'Referer': 'http://www.flw.ph/forum.php?mod=guide&view=newthread',
               'Cookie': 'z67S_2132_saltkey=Ybo6d6B0; z67S_2132_lastvisit=1529057590; _uab_collina=152906119174453922491716; pgv_pvi=3040741590; _ga=GA1.2.1367026788.1529061192; z67S_2132_connect_is_bind=0; z67S_2132_smile=1D1; z67S_2132_atarget=1; pgv_info=ssi=s7443033456; _umdata=BA335E4DD2FD504F96FA0DFC13257AC6A01ED8B83A0C60F7C778AACD7507A1D9AB98C444C566382ECD43AD3E795C914C5C7C0EBCD9F9E69FB855BA2F93D1E78E; z67S_2132_auth=0541vaonJzK7Of4OWVlWJHaY5jxLSQ4jtO4Jdyf6InOMqndX9V5xvU194GrUSQ8gSL5Z3ZgXQqzK9eK4bi0Hcgqrnw; z67S_2132_creditnotice=0D0D2D0D0D0D0D0D0D63111; z67S_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; z67S_2132_lastcheckfeed=63111%7C1530778582; z67S_2132_home_diymode=1; z67S_2132_st_t=63111%7C1530860377%7Cdf662ef1af0c36ab88f265b6a7978aa7; z67S_2132_forum_lastvisit=D_70_1530860377; z67S_2132_ulastactivity=217dCmJEQtCj4cXwVoqjnRCrCfheVxnJao1oTidlR8EwXCjPkMD8; _gid=GA1.2.539459396.1531103374; z67S_2132_creditbase=0D0D83D0D0D0D0D0D0; z67S_2132_pc_size_c=0; CURAD=3; z67S_2132_myrepeat_rr=R0; z67S_2132_st_p=63111%7C1531199290%7C429e10e585c0f528695169817c966197; z67S_2132_visitedfid=76D70D69D170D86D36D172D2D75D40; z67S_2132_viewid=tid_412334; z67S_2132_sendmail=1; z67S_2132_sid=M5IzzN; z67S_2132_lip=157.52.154.68%2C1531200186; z67S_2132_lastact=1531200192%09misc.php%09patch'}

    def parse(self, response):

        soup = BeautifulSoup(response.body, "lxml")
        base_url = "http://www.flw.ph/"

        for box in soup.select('#threadlist tbody[id]'):
            # item['str_id'] = box["id"][-6:]
            item = {}
            aFlag = box.find('a', class_='s xst')
            detail_url = base_url + aFlag["href"]
            print(detail_url)
            item['url'] = detail_url
            item['title'] = aFlag.get_text()
            item['reply_count'] = box.find(
                "span", class_="ico_reply").get_text()
            item['watch_count'] = box.find("span", class_="ico_see").get_text()
            item['creat_time'] = box.select('i.z > span')[0].get_text()
            item['category'] = box.select('i.z > a')[1].get_text()
            req_detail = scrapy.Request(
                detail_url, self.parse_detail, headers=self.headers)
            req_detail.meta["item"] = item
            yield req_detail
            # yield item
        nexAflag = soup.select('#ct a.nxt')
        if len(nexAflag) >= 1:
            url = base_url+nexAflag[0]['href']
            print("next_url="+url)
            yield scrapy.Request(url, callback=self.parse, headers=self.headers)

    def parse_detail(self, response):
        print("get info>>")
        item = PostItem()
        _p_item = response.meta['item']
        item['str_id'] = re.findall(
            r'http://www.flw.ph/thread-(.*)-1-1.html', _p_item['url'])[0]

        item['url'] = _p_item['url']
        item['title'] = _p_item['title']
        item['reply_count'] = _p_item['reply_count']
        item['watch_count'] = _p_item['watch_count']
        item['creat_time'] = _p_item['creat_time']
        item['category'] = _p_item['category']

        soup = BeautifulSoup(response.body, "lxml")
        # print("=========")
        # print(soup.select('#postlist table.plhin div.thread_body div.pcb')[0])
        # print("=========")

        item['content'] = str(soup.select(
            '#postlist table.plhin div.thread_body div.pcb')[0])

        print("detail id >>>"+item['str_id'])
        print("detail url >>>"+item['url'])
        yield item
