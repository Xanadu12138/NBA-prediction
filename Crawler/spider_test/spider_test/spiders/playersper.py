import scrapy
from spider_test.items import PlayersperItem

class PlayersperItemSpider(scrapy.Spider):
    name='playersper'
    custom_settings = {
        'ITEM_PIPELINES' : {'spider_test.pipelines.SpiderPlayersperPipeline': 300}
    }
    # 起始url，爬虫执行后第一批url，将从这个列表中获取
    start_urls = ['https://nba.hupu.com/players']
    # start_urls = ['https://nba.hupu.com/players/spurs','https://nba.hupu.com/players/pelicans']
    def parse(self,response):
        url_list = response.xpath("//div[@class='players_left']/ul/li//a/@href").extract()
        for url in url_list:
            yield scrapy.Request(url,callback = self.parse1)
        
    def parse1(self,response):
        playerurl_list = response.xpath("//div[@class='players_right']//td[@class='td_padding']/a/@href").extract()
        for url in playerurl_list:
            yield scrapy.Request(url,callback = self.parse2)

    def parse2(self,response):
        node_list = response.xpath('//div[@class="shengyasai_tables"]//table[2]//tr[position()>1]')
        for node in node_list:
            item = PlayersperItem()
            item['Name'] = node.xpath("//div[@class='gamecenter_livestart']//p[@class='bread-crumbs']//b/text()").extract_first()
            item['Season'] = node.xpath('.//td[1]//text()').extract()[0]
            item['Tm'] = node.xpath('.//td[2]//text()').extract()[0]
            item['G'] = node.xpath('.//td[3]//text()').extract()[0]
            item['GS'] = node.xpath('.//td[4]//text()').extract()[0]
            item['MP'] = node.xpath('.//td[5]//text()').extract()[0]
            item['FGA'] = node.xpath('.//td[6]//text()').extract()[0]
            item['FGAver'] = node.xpath('.//td[7]//text()').extract()[0]
            item['ThreePA'] = node.xpath('.//td[8]//text()').extract()[0]
            item['ThreePAver'] = node.xpath('.//td[9]//text()').extract()[0]
            item['FTA'] = node.xpath('.//td[10]//text()').extract()[0]
            item['FTAver'] = node.xpath('.//td[11]//text()').extract()[0]
            item['TRB'] = node.xpath('.//td[12]//text()').extract()[0]
            item['AST'] = node.xpath('.//td[13]//text()').extract()[0]
            item['STL'] = node.xpath('.//td[14]//text()').extract()[0]
            item['BLK'] = node.xpath('.//td[15]//text()').extract()[0]
            item['TOV'] = node.xpath('.//td[16]//text()').extract()[0]
            item['PF'] = node.xpath('.//td[17]//text()').extract()[0]
            item['PTS'] = node.xpath('.//td[18]//text()').extract()[0]
            yield(item)
        
        
        