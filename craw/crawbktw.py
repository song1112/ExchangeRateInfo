# coding: utf-8
from datetime import datetime
import requests
import telepot
import time
import MySQLdb
import csv
import pkey
import os

class Crawbktw:

    filename = ''
    uxin_now = 0
    def main(self):
        header = {'User-Agent': \
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'}
        r = requests.get('http://rate.bot.com.tw/xrt/flcsv/0/day', headers=header)
        r.encoding = 'utf-8'
        self.uxin_now = int(time.mktime(datetime.now().timetuple()))
        now = datetime.now()
        self.filename = 'bktw_'+datetime.strftime(now, '%Y%m%dT%H%M%S')+'.csv'
        try:
            # tel
            bot = telepot.Bot(pkey.TELEGRAM_TOKEN)

            # db
            db = MySQLdb.connect(pkey.DB_LOCALHOST, pkey.DB_USER, pkey.DB_PASSWORD, pkey.DB_DATABASE)
            cursor = db.cursor()

            # file
            file = open('./raw_data/'+self.filename, 'w')
            data = r.text.encode('utf-8')
            file.writelines(data)
            file = open('./raw_data/'+self.filename, 'r')
            raw_data = csv.reader(file)
            insert_sql = ''
            for i, r in enumerate(raw_data):
                if i==0: continue
                insert_sql = "insert into fx_rate_raw (currenttime, currency, type, cash, spot) \
                    values(%d, '%s', 'in', %f, %f);" % (self.uxin_now, r[0], float(r[2]), float(r[3]))
                cursor.execute(insert_sql)
                insert_sql = "insert into fx_rate_raw (currenttime, currency, type, cash, spot) \
                    values(%d, '%s', 'out', %f, %f);" % (self.uxin_now, r[0], float(r[12]), float(r[13]))
                cursor.execute(insert_sql)
                db.commit()

                
        except Exception, ex:
            bot.sendMessage(pkey.TELEGRAM_ID, '[%s] craw error! %s at %d' % \
                (str(now), str(ex.message), self.uxin_now))
        finally:
            db.close()
            bot.sendMessage(pkey.TELEGRAM_ID, '[%s] craw finally! at %d' % \
                (str(now), self.uxin_now))
            os.remove('raw_data/'+self.filename)
            file.close()

        # writmee database
        # db = MySQLdb.connect(pkey.DB_LOCALHOST, pkey.DB_USER, pkey.DB_PASSWORD, pkey.DB_DATABASE)
        # cursor = db.cursor()

if __name__ == '__main__':
    c = Crawbktw()
    c.main()
