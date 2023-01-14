# Created by zh on 2016/4/1.
# -*- coding: UTF-8 -*-


import MySQLdb
from DBUtils.PooledDB import PooledDB


# 数据库连接池
pool = PooledDB(MySQLdb, 3, host='127.0.0.1', user='root', passwd='123456', db='storming', port=3306, charset='utf8')