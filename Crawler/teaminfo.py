'''
File name：pachong.py
Explain：用来爬取球队排名信息
Create by：Li Junchao
Create Date：2020-12-13
Change by:Null
'''

import requests
from lxml import etree
import sqlite3

def main():
    url = 'https://nba.hupu.com/standings'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    team_list = tree.xpath('//tbody/tr[position()>2 and position()<18 or position()>19]/td//text()')
    print(team_list)
    # savemysql(team_list)
    

def initsqlite():
    # sql插入语句
    sql = """
        create table if not exists teamlist(
            Ran int,
            Tm char(6) not null primary key,
            Suc int,
            Neg int,
            SucAve char(6),
            Dif float,
            Hom char(6),
            Awa char(6),
            Di char(6),
            Tri char(6), 
            Sco float,
            Los float,
            Mar float, 
            SN char(6))"""
    # 连接数据库
    conn = sqlite3.connect('nba.db')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close

def savemysql(team_list):
    #创建数据库的球队排名表格
    initsqlite()
    sql = """
        insert into teamlist (Rank,Tm,Suc,Neg,SucAve,Dif,Hom,Awa,Div,Tri,Sco,Los,Mar,SN)
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
    
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


if __name__ == '__main__':
    main()