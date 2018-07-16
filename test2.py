import requests
from bs4 import BeautifulSoup
import re
import pymysql.cursors

from sqlalchemy import Column, Integer, DateTime, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()


class Content(Base):
    # 表的名字:
    __tablename__ = 'content'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    str_id = Column(String)
    title = Column(String)
    content = Column(String)
    category = Column(String)
    create_time = Column(String)
    reply_count = Column(Integer)
    watch_count = Column(Integer)
    url=Column(String)


# 初始化数据库连接:
engine = create_engine(
    'mysql+mysqlconnector://root:root@localhost:3306/test2?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session = DBSession()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name',
           'Referer': 'http://www.flw.ph/forum.php?mod=guide&view=newthread',
           'Cookie': 'z67S_2132_saltkey=Ybo6d6B0; z67S_2132_lastvisit=1529057590; _uab_collina=152906119174453922491716; pgv_pvi=3040741590; _ga=GA1.2.1367026788.1529061192; z67S_2132_connect_is_bind=0; z67S_2132_smile=1D1; z67S_2132_atarget=1; pgv_info=ssi=s7443033456; _umdata=BA335E4DD2FD504F96FA0DFC13257AC6A01ED8B83A0C60F7C778AACD7507A1D9AB98C444C566382ECD43AD3E795C914C5C7C0EBCD9F9E69FB855BA2F93D1E78E; z67S_2132_auth=0541vaonJzK7Of4OWVlWJHaY5jxLSQ4jtO4Jdyf6InOMqndX9V5xvU194GrUSQ8gSL5Z3ZgXQqzK9eK4bi0Hcgqrnw; z67S_2132_creditnotice=0D0D2D0D0D0D0D0D0D63111; z67S_2132_creditbase=0D0D75D0D0D0D0D0D0; z67S_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; z67S_2132_lastcheckfeed=63111%7C1530778582; z67S_2132_home_diymode=1; z67S_2132_st_t=63111%7C1530860377%7Cdf662ef1af0c36ab88f265b6a7978aa7; z67S_2132_forum_lastvisit=D_70_1530860377; z67S_2132_ulastactivity=217dCmJEQtCj4cXwVoqjnRCrCfheVxnJao1oTidlR8EwXCjPkMD8; CURAD=2; z67S_2132_st_p=63111%7C1530962171%7Cd3d56bb883285ae217f15dbc09a6a20f; z67S_2132_visitedfid=69D36D76D86D70D172D2D75D40D38; z67S_2132_viewid=tid_411913; z67S_2132_lip=157.52.154.68%2C1530962180'}


def start(url):

    # id
    id = re.findall(r'http://www.flw.ph/thread-(.*)-1-1.html', url)[0]
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name', 'Referer': 'http://www.flw.ph/forum.php?mod=guide&view=newthread', 'Cookie': 'z67S_2132_saltkey=Ybo6d6B0; z67S_2132_lastvisit=1529057590; _uab_collina=152906119174453922491716; pgv_pvi=3040741590; _ga=GA1.2.1367026788.1529061192; z67S_2132_connect_is_bind=0; z67S_2132_smile=1D1; z67S_2132_atarget=1; z67S_2132_pc_size_c=0; CURAD=1; pgv_info=ssi=s7443033456; _gid=GA1.2.1338467510.1530778537; z67S_2132_visitedfid=69D172D2D86D75D70D76D40D38D41; z67S_2132_viewid=tid_410929; z67S_2132_sid=cAZDeP; _umdata=BA335E4DD2FD504F96FA0DFC13257AC6A01ED8B83A0C60F7C778AACD7507A1D9AB98C444C566382ECD43AD3E795C914C5C7C0EBCD9F9E69FB855BA2F93D1E78E; z67S_2132_ulastactivity=1903v6W%2FPZ1Cx%2FOLc%2B27pMh5g8%2FscPuB0%2Bk3OPLpjrEb%2BtYhyN%2FT; z67S_2132_auth=0541vaonJzK7Of4OWVlWJHaY5jxLSQ4jtO4Jdyf6InOMqndX9V5xvU194GrUSQ8gSL5Z3ZgXQqzK9eK4bi0Hcgqrnw; z67S_2132_creditnotice=0D0D2D0D0D0D0D0D0D63111; z67S_2132_creditbase=0D0D75D0D0D0D0D0D0; z67S_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; z67S_2132_lastcheckfeed=63111%7C1530778582; z67S_2132_myrepeat_rr=R0; z67S_2132_st_p=63111%7C1530778588%7Cdb7cc94cf239d23e52ab8af72c168359; z67S_2132_lastact=1530778590%09connect.php%09check; z67S_2132_nofocus_forum=1'}

    req = requests.get(url, headers=headers)

    page_soup = BeautifulSoup(req.content, "lxml")
    # title
    title = page_soup.find(id="thread_subject").get_text()
    # content
    content = page_soup.find_all("div", class_="pcb")[0]
    category_list = page_soup.find(id="pt").find_all("a")
    # category
    category = category_list[-2].get_text()
    # create_time
    create_time = ''
    # reply_count
    reply_count = 0
    # watch_count
    watch_count = 0

    content_info = page_soup.find(
        "div", class_="thread_all").find("div", class_="xg1")

    result = re.findall(r'<div class="xg1">时间：(.*) <span class="notes-info-icon reply-icon" title="回复">(.*)</span> <span class="notes-info-icon show-icon" title="查看">(.*)</span> <span class="pipe">(.*)', str(content_info))

    if len(result) > 0:
        result2 = result[0]
        create_time = result2[0]
        reply_count = result2[1]
        watch_count = result2[2]

    ret = session.query(Content).filter_by(str_id=id).first()

    if ret == None:
        session.add(Content(str_id=id, title=str(title), content=str(content), category=str(category),
                            create_time=create_time, reply_count=reply_count, watch_count=watch_count,url=url))
    else:
        session.query(Content).filter_by(str_id=id).update({"title": str(title), "content": str(content), "category": str(
            category), "create_time": create_time, "reply_count": reply_count, "watch_count": watch_count,"url":url})

    # print(insertContent.title)
    # session.add(insertContent)
    session.commit()
# print(str(content).replace('\n',''))
# insertData(id,title,str(content).replace('\n',''),category,create_time,reply_count,watch_count)
# print(title, content, category, create_time, reply_count, watch_count)


# 通过cursor创建游标
# cursor = connection.cursor()

# # 创建sql 语句，并执行
# sql = "UPDATE `content` SET `title`='aa\
# abbss' WHERE `id`=1"
# cursor.execute(sql)

# # 提交SQL
# connection.commit()


# def insertData(id, title, content, category, create_time, reply_count, watch_count):
#     _is_exist_sql = "SELECT count(*) as count from `content` WHERE `str_id`='"+id+"'"
#     _insert_sql = "INSERT INTO `content` (`str_id`,`title`,`content`,`category`,`create_time`,`reply_count`,`watch_count`) VALUES ('" + \
#         id+"','"+title+"','{content}','"+category + \
#         "','"+create_time+"',"+reply_count+","+watch_count+")"
#     _update_sql = "UPDATE `content` SET `title`='"+title+"',`content`='{content}',`category`='"+category + \
#         "',`create_time`='"+create_time+"',`reply_count`=" + \
#         reply_count+",`watch_count`=" + \
#         watch_count+"  WHERE `str_id`='"+id+"'"
#     _insert_sql = _insert_sql.format(content=content)
#     _update_sql = _update_sql.format(content=content)
#     cursor = connection.cursor()
#     cursor.execute(_is_exist_sql)
#     run_sql = _insert_sql
#     if cursor.fetchone()['count'] >= 1:
#         run_sql = _update_sql
#     cursor.execute(_update_sql)
#     cursor.commit()
#     print(run_sql)
    # print(_insert_sql)
    # print(_update_sql)


# insertData('test1', '222', '222333', '4444', '4444', '1', '2')
def entry():
    base_url = 'http://www.flw.ph/'
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name', 'Referer': 'http://www.flw.ph/forum.php?mod=guide&view=newthread', 'Cookie': 'z67S_2132_saltkey=Ybo6d6B0; z67S_2132_lastvisit=1529057590; _uab_collina=152906119174453922491716; pgv_pvi=3040741590; _ga=GA1.2.1367026788.1529061192; z67S_2132_connect_is_bind=0; z67S_2132_smile=1D1; z67S_2132_atarget=1; z67S_2132_pc_size_c=0; CURAD=1; pgv_info=ssi=s7443033456; _gid=GA1.2.1338467510.1530778537; z67S_2132_visitedfid=69D172D2D86D75D70D76D40D38D41; z67S_2132_viewid=tid_410929; z67S_2132_sid=cAZDeP; _umdata=BA335E4DD2FD504F96FA0DFC13257AC6A01ED8B83A0C60F7C778AACD7507A1D9AB98C444C566382ECD43AD3E795C914C5C7C0EBCD9F9E69FB855BA2F93D1E78E; z67S_2132_ulastactivity=1903v6W%2FPZ1Cx%2FOLc%2B27pMh5g8%2FscPuB0%2Bk3OPLpjrEb%2BtYhyN%2FT; z67S_2132_auth=0541vaonJzK7Of4OWVlWJHaY5jxLSQ4jtO4Jdyf6InOMqndX9V5xvU194GrUSQ8gSL5Z3ZgXQqzK9eK4bi0Hcgqrnw; z67S_2132_creditnotice=0D0D2D0D0D0D0D0D0D63111; z67S_2132_creditbase=0D0D75D0D0D0D0D0D0; z67S_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; z67S_2132_lastcheckfeed=63111%7C1530778582; z67S_2132_myrepeat_rr=R0; z67S_2132_st_p=63111%7C1530778588%7Cdb7cc94cf239d23e52ab8af72c168359; z67S_2132_lastact=1530778590%09connect.php%09check; z67S_2132_nofocus_forum=1'}
    page = 1
    while page<=9:
        print("page>>>"+str(page))
        list_url = base_url + 'forum.php?mod=guide&view=hot&page='+str(page)
        req = requests.get(list_url, headers=headers)
        page_soup = BeautifulSoup(req.content, "lxml") 
        ret =  page_soup.select("table tbody[id]")
        for item in ret:
            path = item.find('a',class_="s xst")['href']
            print("get>>"+base_url + path)
            start(base_url + path)
        # print(len(ret))
        page=page+1
entry()
# start('http://www.flw.ph/thread-411463-1-1.html')
