import jieba
import jieba.analyse

from sqlalchemy import Column, Integer, DateTime, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from bs4 import BeautifulSoup


# 载入字典
jieba.set_dictionary('data/dict.txt.big.txt')


def getKeywords(txt, lenth):
    return jieba.analyse.extract_tags(txt, topK=lenth)

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
    keywords=Column(String)


engine = create_engine(
    'mysql+mysqlconnector://root:root@localhost:3306/test2?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session = DBSession()

count = session.query(Content).count()

print('Data count:', count)
index = 0
while index < count:
    print('current index:',index)
    ret = session.query(Content).order_by(
        Content.create_time.desc()).limit(1).offset(index).first()
    text = BeautifulSoup(ret.content,'lxml').get_text()
    keywords = ','.join(getKeywords(text,10))
    session.query(Content).filter_by(str_id=ret.str_id).update({'keywords':keywords})
    print(keywords)
    session.commit()
    index = index+1
    


# print(ret.str_id)




# text = u'''世界日报：负责修改宪法的咨询委员会，终于把联邦制的宪法草案交给杜特地总统;他将于明年举行公投，由人民决定是否接受新部宪法民调显示过半数的人民不明新宪法，反对者也多。但杜特地总统必籍他的民望，或用其他方法让它通过。
# 新宪法除了将国家“分裂”成十八个联邦行政区外，别无新意。旧瓶装旧酒，除了可让一些执政者乘机延长任期，只会增加国家机构，损害行政效率。要凭它解决南部回教徒叛乱问题，是痴人说梦;菲国早有“摩洛国”自治法，只欠认真执行。
# 新宪法草案没修改经济条文：如允许外国人或公司拥有土地菲国地产最近有过热现象，一旦开放，地价必定飙升，令欲置业者望地，望楼兴叹，沦为”无壳蜗牛”。有些经济学家盼望外国投资振兴经济，但外资只能占公司百分之四十的限制，没有取消，这让跨国公司失望，投资意愿低落。民族资本需耍一点一滴慢慢储蓄，一些大型投资，只能望洋兴叹。
# 草案也保留学校菲化条文：外侨生数不得超过学校生数三分之一华侨大多归化为公民，所以对华校来说影响不大但外国人不得担任学校首长，对一些欲聘请外国教育家以改善教学水准的学校是一项障碍。
# 新宪法草案出自一些政客的私心，劳民伤财，对整个国家的繁荣进步，可能全没贡献，也许在公投前，该周详考虑？
# '''

# print(getKeywords(text, 10))

# 全模式

# # text ="我来到北京清华大学"

# # seg_list = jieba.cut(text, cut_all=True)
# seg_list = jieba.cut(text, cut_all=True)

# print("[全模式]: ", "/ ".join(seg_list))

# # #精确模式
# seg_list = jieba.cut(text, cut_all=False)

# print("[精确模式]: ", "/ ".join(seg_list))

# # #默认是精确模式

# # seg_list = jieba.cut(text)

# # print("[默认模式]: ","/ ".join(seg_list))

# # #新词识别 “杭研”并没有在词典中,但是也被Viterbi算法识别出来了

# # seg_list = jieba.cut("他来到了网易杭研大厦")

# # print("[新词识别]: ","/ ".join(seg_list))

# # #搜索引擎模式
# seg_list = jieba.cut_for_search(text, )
# # seg_list = jieba.cut_for_search(text)

# print("[搜索引擎模式]: ", "/ ".join(seg_list))

# tags = jieba.analyse.extract_tags(text, topK=11)
# print(tags)
