# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 球员的个人信息的存储格式
class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 姓名
    Name = scrapy.Field()
    # 号码
    Num = scrapy.Field()
    # 位置
    Pos = scrapy.Field()
    # 身高
    Tall = scrapy.Field()
    # 体重
    Wei = scrapy.Field()
    # 生日
    Bri = scrapy.Field()
    # 球队
    Tm = scrapy.Field()
    # 合同
    Con = scrapy.Field()
    # 头像照片的地址
    Img =scrapy.Field()

# 球队排行榜的存储格式
class TeamItem(scrapy.Item):
    # 排名
    Ran = scrapy.Field()
    # 队名
    Tm = scrapy.Field()
    # 胜场数
    Suc = scrapy.Field()
    # 败场数
    Neg = scrapy.Field()
    # 胜率
    SucAve = scrapy.Field()
    # 胜场差
    Dif = scrapy.Field()
    # 主场胜负
    Hom = scrapy.Field()
    # 客场胜负
    Awa = scrapy.Field()
    # 赛区
    Di = scrapy.Field()
    # 得分
    Sco = scrapy.Field()
    # 失分
    Los = scrapy.Field()
    # 净胜
    Mar = scrapy.Field()
    #连胜/负
    Sn = scrapy.Field()

class PlayerItem(scrapy.Item):
    Ran = scrapy.Field()
    Name = scrapy.Field()
    Tm = scrapy.Field()
    Sco = scrapy.Field()
    FGA = scrapy.Field()
    FGAver = scrapy.Field()
    TPA = scrapy.Field()
    TPAver = scrapy.Field()
    FTA = scrapy.Field()
    FTAver = scrapy.Field()
    G = scrapy.Field()
    Time = scrapy.Field()