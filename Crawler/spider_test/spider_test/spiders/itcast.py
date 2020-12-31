import scrapy
import sqlite3
from spider_test.items import SpiderItem,TeamItem,PlayerItem
# from spider_test.pipelines import deletedb
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # 爬取域范围，允许爬虫在这个域名下爬取（可选）
    # allowed_domains = ['http://www.itcast.cn']
    custom_settings = {
        'ITEM_PIPELINES' : {'spider_test.pipelines.SpiderTestPipeline': 300}
    }
    # 起始url，爬虫执行后第一批url，将从这个列表中获取
    start_urls = ['https://nba.hupu.com/players']

    def parse(self, response):
        url_list = response.xpath("//div[@class='players_left']/ul/li//a/@href").extract()
        for i in range(0,30):
            url = url_list[i]
            yield scrapy.Request(url,callback = self.parse)
        node_list = response.xpath('//tbody/tr[position()>1]')
        #将不在节点的单独解析
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item = SpiderItem()
            # .extract()将xpath对象转化为 Unicode对象
            item['Img'] = node.xpath(".//img/@src").extract()[0]
            item['Name'] = node.xpath('.//td[2]/b//text()').extract()[0]
            item['EName'] = node.xpath('.//td[2]//p//b//text()').extract()[0]
            item['Num'] = node.xpath('.//td[3]//text()').extract()[0]
            item['Pos'] = node.xpath(".//td[4]/text()").extract()[0]
            item['Tall'] = node.xpath(".//td[5]/text()").extract()[0]
            item['Wei'] = node.xpath(".//td[6]/text()").extract()[0]
            item['Bri'] = node.xpath(".//td[7]/text()").extract()[0]
            item['Tm'] = node.xpath("//li[@class='on']//span//text()").extract()[0]
            item['Con'] = node.xpath(".//td[8]//text()").extract()[0]
            yield(item)
            # print(item)

class TeamSpider(scrapy.Spider):
    name = 'Team'
    # 爬取域范围，允许爬虫在这个域名下爬取（可选）
    allowed_domains = ['https://nba.hupu.com/']
    # 起始爬取的地址
    start_urls = ['https://nba.hupu.com/standings']
    custom_settings = {
        'ITEM_PIPELINES' : {'spider_test.pipelines.SpiderTeamPipeline': 300}
    }
    # 清空数据库
    # deletedb("teamlist")
    def parse(self,response):
        node_list = response.xpath('//tbody/tr[position()>2 and position()<18 or position()>19]')
        i = 1
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item = TeamItem()
            # 判断并且用来记录战区
            if i < 16:
                di_str = '东部'
            else:
                di_str = '西部'
            i = i + 1

            item['Ran'] = node.xpath('.//td[1]//text()').extract()[0]
            item['Tm'] = node.xpath('.//td[2]//text()').extract()[0]
            item['Suc'] = node.xpath('.//td[3]/text()').extract()[0]
            item['Neg'] = node.xpath('.//td[4]/text()').extract()[0]
            item['SucAve'] = node.xpath('.//td[5]/text()').extract()[0]
            item['Dif'] = node.xpath('.//td[6]/text()').extract()[0]
            item['Hom'] = node.xpath('.//td[7]/text()').extract()[0]
            item['Awa'] = node.xpath('.//td[8]/text()').extract()[0]
            item['Di'] = di_str
            item['Sco'] = node.xpath('.//td[11]/text()').extract()[0]
            item['Los'] = node.xpath('.//td[12]//text()').extract()[0]
            item['Mar'] = node.xpath('.//td[13]//text()').extract()[0]
            item['Sn'] = node.xpath('.//td[14]//text()').extract()[0]
            yield(item)

class PlayerSpider(scrapy.Spider):
    name = 'Player'
    # 爬取域范围，允许爬虫在这个域名下爬取（可选）
    allowed_domains = ['https://nba.hupu.com/']
    # 起始爬取的地址
    start_urls = ['https://nba.hupu.com/stats/players/pts']
    # 指定管道文件
    custom_settings = {
        'ITEM_PIPELINES' : {'spider_test.pipelines.SpiderPlayerPipeline': 300}
    }
    # 清空数据库
    # deletedb("playerlist")
    def parse(self,response):
        item = PlayerItem()
        node_list = response.xpath('//tbody/tr[position()>1]')
        for node in node_list:
            item['Ran'] = node.xpath('.//td[1]//text()').extract()[0]
            item['Name'] = node.xpath('.//td[2]//text()').extract()[0]
            item['Tm'] = node.xpath('.//td[3]//text()').extract()[0]
            item['Sco'] = node.xpath('.//td[4]/text()').extract()[0]
            item['FGA'] = node.xpath('.//td[5]/text()').extract()[0]
            item['FGAver'] = node.xpath('.//td[6]/text()').extract()[0]
            item['TPA'] = node.xpath('.//td[7]/text()').extract()[0]
            item['TPAver'] = node.xpath('.//td[8]/text()').extract()[0]
            item['FTA'] = node.xpath('.//td[9]/text()').extract()[0]
            item['FTAver'] = node.xpath('.//td[10]/text()').extract()[0]
            item['G'] = node.xpath('.//td[11]/text()').extract()[0]
            item['Time'] = node.xpath('.//td[12]//text()').extract()[0]
            yield(item)
