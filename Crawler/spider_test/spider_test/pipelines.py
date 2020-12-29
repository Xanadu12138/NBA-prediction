# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

# 链接数据库
def sqlite3db():
    conn = sqlite3.connect('nba.db')
    return conn

# 清空数据库中一个表的内容
def deletedb(name):
    dbobj = sqlite3db()
    cursor = dbobj.cursor()
    sql = """
        delete from %s;
        """%(name)
    cursor.execute(sql)
    dbobj.commit()
    dbobj.close

class SpiderTestPipeline:
    def process_item(self, item, spider):
        dbobj = sqlite3db()
        cursor = dbobj.cursor()
        sql = """
        insert into playersinfo (Name,Tm,Num,Pos,Tall,Wei,Bri,Con,Img)
        # values(?,?,?,?,?,?,?,?,?);
        """
        try:
            cursor.execute(sql,(item['Name'],item['Tm'],item['Num'],item['Pos'],
            item['Tall'],item['Wei'],item['Bri'],item['Con'],item['Img']))
            dbobj.commit()
            dbobj.close
        except BaseException as e:
            print("错误在这里>>>",e)
            dbobj.rollback()
        return item

class SpiderTeamPipeline:
    def process_item(self, item, spider):
        dbobj = sqlite3db()
        cursor = dbobj.cursor()
        sql = """
        insert into teamlist (Ran,Tm,Suc,Neg,SucAve,Dif,Hom,Awa,Di,Sco,Los,Mar,SN)
        values(?,?,?,?,?,?,?,?,?,?,?,?,?);
        """
        try:
            cursor.execute(sql,(item['Ran'],item['Tm'],item['Suc'],item['Neg'],
            item['SucAve'],item['Dif'],item['Hom'],item['Awa'],item['Di'],item['Sco'],
            item['Los'],item['Mar'],item['Sn']))
            dbobj.commit()
            dbobj.close()
        except BaseException as e:
            print("错误在这里>>>",e)
            dbobj.rollback()
        return item

class SpiderPlayerPipeline:
    def process_item(self, item, spider):
        dbobj = sqlite3db()
        cursor = dbobj.cursor()
        sql = """
        insert into playerlist (Ran,Name,Tm,Sco,FGA,FGAver,TPA,TPAver,FTA,FTAver,G,Time)
        values(?,?,?,?,?,?,?,?,?,?,?,?);
        """
        try:
            cursor.execute(sql,(item['Ran'],item['Name'],item['Tm'],item['Sco'],item['FGA'],
            item['FGAver'],item['TPA'],item['TPAver'],item['FTA'],item['FTAver'],item['G'],
            item['Time']))
            dbobj.commit()
            dbobj.close
        except BaseException as e:
            print("错误在这里>>>",e)
            dbobj.rollback()
        return item