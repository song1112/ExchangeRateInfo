# !/usr/bin/python
# coding: utf-8

import pkey
import MySQLdb

db = MySQLdb.connect(pkey.DB_LOCALHOST, pkey.DB_USER, pkey.DB_PASSWORD, pkey.DB_DATABASE)
cursor = db.cursor()

create_fx_rate_day_sql = "create table fx_rate_day ( \
    id int not null auto_increment, \
    createtime datetime default current_timestamp, \
    currenttime int, \
    currency varchar(3), \
    type enum('in', 'out'), \
    cash double, \
    spot double, \
    primary key(id));" \

create_fx_rate_raw_sql = "create table fx_rate_raw ( \
    id int not null auto_increment, \
    createtime datetime default current_timestamp, \
    currenttime int, \
    currency varchar(3), \
    type enum('in', 'out'), \
    cash double, \
    spot double, \
    primary key(id));" \

select_sql = 'select * from fx_rate_day;'

drop_sql = 'drop table fx_rate_day;'

index_sql = 'create index q_currenttime on fx_rate_day(currenttime);'

try:
    cursor.execute(create_fx_rate_day_sql)
    cursor.execute(create_fx_rate_raw_sql)
    cursor.execute(index_sql)
    db.commit()
except Exception,ex:
    print ex.message
finally:
    db.close()

