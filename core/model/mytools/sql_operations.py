# Created by zh on 2016/4/1.
# -*- coding: UTF-8 -*-

import MySQLdb
import logging
import traceback
from db_pool import pool


class SQL(object):
    """
        sql基本操作
    """
    def __init__(self):
        self.logger = logging.getLogger(name='SQL')

    def fetch_all(self, sql):
        """
            执行sql语句获取所有数据，适用于select语句
        :param sql: sql语句
        :return: 成功：获取所有数据     失败：抛出异常
        """
        self.logger.info("进入fetch_all方法")
        self.logger.info("sql语句: sql=%s", sql)
        try:
            # 1.连接数据库
            conn = pool.connection()
            # 2.获取游标
            cur = conn.cursor()
            # 3.执行获取信息
            cur.execute(sql)
            result = cur.fetchall()
            # 4.关闭数据库
            conn.close()
            self.logger.info("退出fetch_all方法")
            return result
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("fetch_all方法执行失败")
            raise e

    def fetch_one(self, sql):
        """
            执行sql语句获取一条数据，适用于select语句
        :param sql: sql语句
        :return: 成功：获取一条数据    失败：抛出异常
        """
        self.logger.info("进入fetch_one方法")
        # self.logger.info("sql语句: sql=%s", sql)
        try:
            # 1.连接数据库
            conn = pool.connection()
            # 2.获取游标
            cur = conn.cursor()
            # 3.执行获取信息
            cur.execute(sql)
            result = cur.fetchone()
            # 4.关闭数据库
            conn.close()
            self.logger.info("退出fetch_one方法")
            return result
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("fetch_one方法执行失败")
            raise e

    def excute_one(self, sql):
        """
            执行sql语句并提交，适用于执行语句
        :param sql: sql语句
        :return:
        """
        self.logger.info("进入excute_one方法")
        try:
            # 1.连接数据库
            conn = pool.connection()
            # 2.获取游标
            cur = conn.cursor()
            # 3.执行提交
            cur.execute(sql)
            conn.commit()
            # 4.关闭数据库
            conn.close()
            self.logger.info("退出excute_one方法")
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("excute_one方法执行失败")
            raise e
