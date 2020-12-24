# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

import scrapy
from spider_test.items import SpiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # 爬取域范围，允许爬虫在这个域名下爬取（可选）
    # allowed_domains = ['http://www.itcast.cn']

    # 起始url，爬虫执行后第一批url，将从这个列表中获取
    start_urls = ['https://nba.hupu.com/players']

    def parse(self, response):
        url_list = response.xpath("//div[@class='players_left']/ul/li//a/@href").extract()
        for i in range(0,30):
            url = url_list[i]
            yield scrapy.Request(url,callback = self.parse)

        # print(response.body)
        node_list = response.xpath('//tbody/tr[position()>1]')
        #将不在节点的单独解析
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item = SpiderItem()
            # .extract()将xpath对象转化为 Unicode对象
            item['Img'] = node.xpath(".//img/@src").extract()[0]
            item['Name'] = node.xpath('.//td[2]/b//text()').extract()[0]
            item['Num'] = node.xpath('.//td[3]//text()').extract()[0]
            item['Pos'] = node.xpath(".//td[4]/text()").extract()[0]
            item['Tall'] = node.xpath(".//td[5]/text()").extract()[0]
            item['Wei'] = node.xpath(".//td[6]/text()").extract()[0]
            item['Bri'] = node.xpath(".//td[7]/text()").extract()[0]
            item['Tm'] = node.xpath("//li[@class='on']//span//text()").extract()[0]
            item['Con'] = node.xpath(".//td[8]//text()").extract()[0]
            yield(item)
