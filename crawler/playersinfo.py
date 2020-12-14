'''
File name：pachong.py
Explain：用来爬取球员信息
Create by：Li Junchao
Create Date：2020-12-10
Change by:Null
'''

from sqlite3.dbapi2 import SQLITE_CREATE_TABLE
import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
#import pymysql
import sqlite3


def main():
    geturl()


def geturl():
    # 战队总页面的url
    url = 'https://www.basketball-reference.com/players/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57'
    }
    # 爬取到总界面的所有队伍的链接
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    url_list = tree.xpath('//div[@id="site_menu"]/ul/li[2]/div/a/@href')
    for i in range(len(url_list)):
        url_list[i] = 'https://www.basketball-reference.com'+url_list[i]
    playnumber = 0
    for j in range(30):
        # urlteam = 'https://www.basketball-reference.com/teams/LAC/2020.html'
        page_text = requests.get(url=url_list[j], headers=headers).text
        print(url_list[j])
        tree = etree.HTML(page_text)
        # 在一只队伍的所有队员的详情链接爬取到
        url_list1 = tree.xpath('//table[@id="roster"]/tbody/tr/td[@data-stat="player"]/a/@href')
        # 前缀要加上 https://www.basketball-reference.com/ 才能访问该网站
        # for i in range(13,len(url_list)):
        for i in range(3,len(url_list1)):
            url2 = 'https://www.basketball-reference.com/'+url_list1[i]
            # 用来提醒第几个球员正在存储！！！
            playnumber = playnumber + 1
            print("第"+str(playnumber)+"位球员的信息正在存储！！！")
            getdata(url2, headers)


def getdata(url, headers):
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    play_name = tree.xpath('//div[@id="meta"]//h1/span/text()') # 存放球员的名字
    season_list = tree.xpath('//table[@id="per_game"]/tbody/tr/th//text()')  # 将赛季存入一个列表中
    player_list = list()
    # 存放一个球员有多少条记录
    listtemp = tree.xpath('//table[@id="per_game"]/tbody/tr')
    for i in range(1,len(listtemp)+1):

        # 用来判断该球员当赛季是否进行比赛，如果否，不存入当赛季的记录
        judge_list = tree.xpath('//table[@id="per_game"]/tbody/tr[{}]/td'.format(i))
        if(len(judge_list)<20):
            season = tree.xpath('//table[@id="per_game"]/tbody/tr[{}]/td[1]//text()'.format(i))
            season_list.insert(i-1,season[0]) 
            # 将没有参加的赛季补空
            player_list.extend([play_name[0],season_list[i-1],'0','0','0','0','0','0','0','0','0','0','0','0','0'
            ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'])
            # 跳过本次循环，进行下次记录的处理
            continue
        else:
            
            # 将百分数前面的存入列表(因为部分命中率为空)
            player_list.extend(tree.xpath('//table[@id="per_game"]/tbody/tr[{}]/td[position()<10]//text()'.format(i)))
            player_list_temp = tree.xpath('//table[@id="per_game"]/tbody/tr[{}]/td[position()=10]//text()'.format(i))
            if(player_list_temp):
                player_list.extend(player_list_temp)
            else:
                player_list.append('')
            # 将百分数前面的存入列表
            player_list.extend(tree.xpath('//table[@id="per_game"]/tbody/tr[{}]/td[position()<13 and position()>10]//text()'.format(i)))

            #将球员的名字和赛季插入到列表中
            player_list.insert((i-1)*31, play_name[0])
            player_list.insert((i-1)*31+1, season_list[i-1])
            # 用来判断三分球得命中率是否为空
            player_list_temp = tree.xpath('//table[@id="per_game"]/tbody/tr[{}]/td[position()=13]//text()'.format(i))
            if(player_list_temp):
                player_list.extend(player_list_temp)
            else:
                player_list.append('')

            player_list.extend(tree.xpath('//table[@id="per_game"]/tbody/tr[{}]/td[position()>13 and position()<16]//text()'.format(i)))

            # 用来判断二分球得命中率是否为空
            player_list_temp = tree.xpath('//table[@id="per_game"]/tbody/tr[{}]/td[position()=16]//text()'.format(i))
            if(player_list_temp):
                player_list.extend(player_list_temp)
            else:
                player_list.append('')

            # 用来判断命中率是否为空
            player_list_temp = tree.xpath('//table[@id="per_game"]/tbody/tr[{}]/td[position()=17]//text()'.format(i))
            if(player_list_temp):
                player_list.extend(player_list_temp)
            else:
                player_list.append('')
            # 将正常的数据存入列表
            player_list.extend(tree.xpath('//table[@id="per_game"]/tbody/tr[{}]/td[position()>17 and position()<20]//text()'.format(i)))

            # 用来判断罚球得命中率是否为空
            player_list_temp = tree.xpath('//table[@id="per_game"]/tbody/tr[{}]/td[position()=20]//text()'.format(i))
            if(player_list_temp):
                player_list.extend(player_list_temp)
            else:
                player_list.append('')

            player_list.extend(tree.xpath('//table[@id="per_game"]/tbody/tr[{}]/td[position()>20]//text()'.format(i)))

    # 将列表经过处理放入数据库中
    getplayers(player_list)


# 处理得到的球员数据，将球员数据修改以便存入数据库
def getplayers(player_list):
    le = int(len(player_list)/31)
    # 将列表的每个数据的格式化为和数据库相同的格式
    for index in range(le):
        player_list_temp = [player_list[0+index*31], player_list[1+index*31], int(player_list[2+index*31]),
                            player_list[3+index*31], player_list[4 +index*31], player_list[5+index*31],
                            int(player_list[6+index*31]), int(player_list[7 +index*31]), float(player_list[8+index*31]),
                            float(player_list[9+index*31]), float(player_list[10+index*31]), float('0'+player_list[11+index*31]),
                            float(player_list[12+index*31]), float(player_list[13+index*31]),float('0' + player_list[14+index*31]), 
                            float(player_list[15+index*31]),float(player_list[16+index*31]),float('0'+player_list[17+index*31]), 
                            float('0'+player_list[18+index*31]), float(player_list[19+index*31]), float(player_list[20+index*31]), 
                            float('0' + player_list[21+index*31]),float(player_list[22+index*31]), float(player_list[23+index*31]), 
                            float(player_list[24+index*31]), float(player_list[25+index*31]), float(player_list[26+index*31]), 
                            float(player_list[27+index*31]),float(player_list[28+index*31]), float(player_list[29+index*31]),
                            float(player_list[30+index*31])]
        #将处理过的数据存入数据库的表中
        # savemysql(player_list_temp)
        savesqlite(player_list_temp)


def savemysql(player_list_temp):
    # 链接本地数据库
    conn = pymysql.connect(host='localhost', user='root',passwd='ljc677521', database='nba', port=3306, charset='utf8')
    # 获取光标
    cur = conn.cursor()
    # sql插入语句
    sql = """
        insert into gsw (PlayerName,Season,Age,Tm,Lg,Pos,G,GS,MP,FG,FGA,
        FGAver,3P,3PA,3PAver,2P,2PA,2PAver,eFGAver,FT,FTA,FTAver,ORB,DRB,TRB,AST,
        STL,BLK,TOV,PF,PTS)
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
    # 经处理的数据经过sql语句加入表中
    cur.execute(sql, player_list_temp)
    conn.commit()
    conn.close

# Modified By Dai Yucong
def savesqlite(player_list_temp):
    conn = sqlite3.connect('../backend/db.sqlite3')
    cur = conn.cursor()
    sql = """
        insert into gsw (PlayerName,Season,Age,Tm,Lg,Pos,G,GS,MP,FG,FGA,
        FGAver,ThreeP,ThreePA,ThreePAver,TwoP,TwoPA,TwoPAver,eFGAver,FT,FTA,FTAver,ORB,DRB,TRB,AST,
        STL,BLK,TOV,PF,PTS)
        values(?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s,?%s);"""
    # 经处理的数据经过sql语句加入表中
    cur.execute(sql, player_list_temp)
    conn.commit()
    cur.close()
    conn.close


if __name__ == "__main__":
    main()