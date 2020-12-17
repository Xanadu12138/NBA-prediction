'''
File name：pachong.py
Explain：用来爬取球队比赛赛程比分信息
Create by：Li Junchao
Create Date：2020-12-16
Change by:Null
'''
import os
import sys
import requests
from lxml import etree
import sqlite3

def main():
    # 将30支队伍的英文名存入表中，一边和前面球员信息表联系
    Chi_Eng = {'雄鹿':'MIL','猛龙':'TOR','凯尔特人':'BOS','热火':'MIA','步行者':'IND','76人':'PHI',
            '篮网':'BKN','魔术':'ORL','奇才':'WAS','黄蜂':'CHA','公牛':'CHI','尼克斯':'NYK',
            '活塞':'DET','老鹰':'ATL','骑士':'CLE','湖人':'LAL','快船':'LAC','掘金':'DEN',
            '爵士':'UTA','雷霆':'OKC','火箭':'HOU','独行侠':'DAL','灰熊':'MEM','开拓者':'POR',
            '鹈鹕':'NOP','国王':'SAC','马刺':'SAS','太阳':'PHX','森林狼':'MIN','勇士':'GSW'}
    url = 'https://nba.hupu.com/schedule/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57'
    }
    # 用来作为跳转页面的url，以爬取到所有的比赛信息
    for i in range(2020,2021):
        for j in range(11,12):
            for index in range(1,32,7):
                urls = url +str(i)+'-'+str(j)+'-'+str(index)
                print(urls)
                askdata(Chi_Eng,urls,headers)

#得到所有的比赛信息
def askdata(Chi_Eng,url,headers):
    info_list = list()
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    sc_list = tree.xpath('//tbody/tr/td[3]/a/@href')
    for item in sc_list:
        page_text = requests.get(url=item, headers=headers).text
        tree = etree.HTML(page_text)
        # 得到比赛球队的两个球队名字
        list_temp = tree.xpath('//div[@class="team_vs_box"]//p/a/text()')
        for item1 in list_temp:
            #如果不是三十队之一，直接存入中文名字
            if item1 in Chi_Eng:
                info_list.append(Chi_Eng[item1])
            else:
                info_list.append(item1)
        list_temp = tree.xpath('//div[@class="team_vs_box"]//div[@class="message"]/div/text()')
        for item1 in list_temp:
            # 如果长度小于8，证明该球队没有主场客场成绩
            if len(item1)<8:
                info_list.append('')
            else:
                item1 = item1[4:10]
                info_list.append(item1)
        # 得到比赛的比分信息
        list_temp = tree.xpath('//div[@class="team_vs_box"]//h2/text()')
        info_list.append(list_temp[0]+':'+list_temp[1])
    print(info_list)
    if info_list:
        savemysql(info_list)

def initsqlite():
    # 创建sqlite3的存储数据的表
    sql = """
        create table if not exists schlist(
            Tm1 char(6),
            Tm2 char(6),
            Sco1 char(10),
            Sco2 char(10),
            sco char(10));"""
    # 连接数据库
    conn = sqlite3.connect('nba.db')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close

def savemysql(team_list):
    # 初始化数据库的表
    initsqlite()
    # 用作存储一个比赛的信息
    list_temp = list()

    sql = """
        insert into schlist (Tm1,Tm2,Sco1,Sco2,sco)
        values(?,?,?,?,?);"""

    conn = sqlite3.connect('nba.db')
    cur = conn.cursor()
    # 用来存储一场比赛的信息，一场比赛的信息插入一次
    for index in range(len(team_list)):
        list_temp.append(team_list[index])
        if len(list_temp) == 5:
            cur.execute(sql,list_temp)
            conn.commit()
            list_temp.clear()
    conn.close
if __name__ == "__main__":
    main()       