# -*- coding: UTF-8 -*-
import MySQLdb
import time
from datetime import datetime
import constant
import pkey

class handle:

    def __init__(self):
        self.db = MySQLdb.connect(pkey.DB_LOCALHOST, pkey.DB_USER, pkey.DB_PASSWORD, pkey.DB_DATABASE)
        self.cursor = self.db.cursor()
        self.data = {}
        self.usdci, self.usdsi, self.usdco, self.usdso = [], [], [], []
        self.gbpci, self.gbpsi, self.gbpco, self.gbpso = [], [], [], []
        self.hkdci, self.hkdsi, self.hkdco, self.hkdso = [], [], [], []
        self.audci, self.audsi, self.audco, self.audso = [], [], [], []
        self.cadci, self.cadsi, self.cadco, self.cadso = [], [], [], []
        self.sgdci, self.sgdsi, self.sgdco, self.sgdso = [], [], [], []
        self.jpyci, self.jpysi, self.jpyco, self.jpyso = [], [], [], []
        self.eurci, self.eursi, self.eurco, self.eurso = [], [], [], []
        self.cnyci, self.cnysi, self.cnyco, self.cnyso = [], [], [], []


        """
        for c in constant.CURRENCY:
            tmp = {}
            tmp['in'] = []
            tmp['out'] = []
            self.data[c] = tmp
        """

    """ 取得今天資料 """
    def getToday(self):
        now = int(time.time())
        start = int(time.mktime(datetime.now().date().timetuple()))
        sql = 'select * from fx_rate_raw where currenttime >= %d and currenttime <= %d;' % (start, now)
        sql = 'select * from fx_rate_raw limit 76;'
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        for row in results:
            if row[3] == 'USD':
                if row[4] == 'in':
                    self.usdci.append(row[5]) # cash
                    self.usdsi.append(row[6]) # spot
                else:
                    self.usdco.append(row[5]) # cash
                    self.usdso.append(row[6]) # spot
            elif row[3] == 'HKD':
                if row[4] == 'in':
                    self.hkdci.append(row[5]) # cash
                    self.hkdsi.append(row[6]) # spot
                else:
                    self.hkdco.append(row[5]) # cash
                    self.hkdso.append(row[6]) # spot
            elif row[3] == 'GBP':
                if row[4] == 'in':
                    self.gbpci.append(row[5]) # cash
                    self.gbpsi.append(row[6]) # spot
                else:
                    self.gbpco.append(row[5]) # cash
                    self.gbpso.append(row[6]) # spot
            elif row[3] == 'AUD':
                if row[4] == 'in':
                    self.audci.append(row[5]) # cash
                    self.audsi.append(row[6]) # spot
                else:
                    self.audco.append(row[5]) # cash
                    self.audso.append(row[6]) # spot
            elif row[3] == 'CAD':
                if row[4] == 'in':
                    self.cadci.append(row[5]) # cash
                    self.cadsi.append(row[6]) # spot
                else:
                    self.cadco.append(row[5]) # cash
                    self.cadso.append(row[6]) # spot
            elif row[3] == 'SGD':
                if row[4] == 'in':
                    self.sgdci.append(row[5]) # cash
                    self.sgdsi.append(row[6]) # spot
                else:
                    self.sgdco.append(row[5]) # cash
                    self.sgdso.append(row[6]) # spot
            elif row[3] == 'JPY':
                if row[4] == 'in':
                    self.jpyci.append(row[5]) # cash
                    self.jpysi.append(row[6]) # spot
                else:
                    self.jpyco.append(row[5]) # cash
                    self.jpyso.append(row[6]) # spot
            elif row[3] == 'EUR':
                if row[4] == 'in':
                    self.eurci.append(row[5]) # cash
                    self.eursi.append(row[6]) # spot
                else:
                    self.eurco.append(row[5]) # cash
                    self.eurso.append(row[6]) # spot
            elif row[3] == 'CNY':
                if row[4] == 'in':
                    self.cnyci.append(row[5]) # cash
                    self.cnysi.append(row[6]) # spot
                else:
                    self.cnyco.append(row[5]) # cash
                    self.cnyso.append(row[6]) # spot
            """        
            # currency
            if self.data.get(row[3]):
                # sellbuy
                info = {}
                info['time'] = str(row[1])
                info['cash'] = row[5]
                info['spot'] = row[6]
                self.data[row[3]][row[4]].append(info)
            """

    """ 取得某一天 """
    def getSomeday(self, date):
        sql = 'select * from fx_rate_raw where date=%s' % date
        pass

    def getMonth(self, month=0):
        sql = 'select * from fx_rate_day'
        pass

    def getInterval(self, start, end):
        sql = 'select * from fx_rate_day'
        pass

if __name__ == '__main__':
    h = handle()
    h.getToday()
    print h.data
    h.db.close()

