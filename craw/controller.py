# !/usr/bin/python
# coding: utf-8
from datetime import datetime
import time
import MySQLdb
import telepot
import pkey
from crawbktw import Crawbktw

if __name__ == '__main__':

    db = MySQLdb.connect(pkey.DB_LOCALHOST, pkey.DB_USER, pkey.DB_PASSWORD, pkey.DB_DATABASE)
    cursor = db.cursor()
    bot = telepot.Bot(pkey.TELEGRAM_TOKEN)

    # 取得今日日期
    now = datetime.now()

    # 執行最後一次爬蟲取得收盤資料
    c = Crawbktw()
    c.main()

    # 找出今日最後一筆收盤資料
    select_sql = "insert into fx_rate_day (currenttime, currency, type, cash, spot) \
        select distinct currenttime, currency, type, cash, spot from fx_rate_raw \
        where currenttime=%d;" % c.uxin_now
    print select_sql
    try:
        cursor.execute(select_sql)
        db.commit()
    except Exception, ex:
        bot.sendMessage(pkey.TELEGRAM_ID, '[%s] controller error: %s! at %d' % \
            (str(now), str(ex.message), c.uxin_now))
    finally:
        bot.sendMessage(pkey.TELEGRAM_ID, '[%s] controller finally! at %d' % \
            (str(now), c.uxin_now))
        db.close()


