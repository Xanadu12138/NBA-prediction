# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

def sqlite3db():
    conn = sqlite3.connect('nba.db')
    return conn

class SpiderTestPipeline:
    def process_item(self, item, spider):
        dbobj = sqlite3db()
        cursor = dbobj.cursor()
        sql = """
        insert into playersinfo (Name,Tm,Num,Pos,Tall,Wei,Bri,Con,Img)
        values(?,?,?,?,?,?,?,?,?);
        """
        try:
            cursor.execute(sql,(item['Name'],item['Tm'],item['Num'],item['Pos'],
            item['Tall'],item['Wei'],item['Bri'],item['Con'],item['Img']))
            dbobj.commit()
        except BaseException as e:
            print("错误在这里>>>",e)
            dbobj.rollback()
        return item