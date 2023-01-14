# Created by zh on 2016/4/3.
# -*- coding: UTF-8 -*-


import logging
from model.sql import sql_statement
from model.mytools import sql_operations
import traceback


class loginMedia(object):
    """
        登录媒体平台类
    """
    def __init__(self):
        self.logger = logging.getLogger(name='loginMedia')

    def judge_exist_user(self, user_name, user_pass):
        """
            检查是否存在用户
        :param user_name: 用户名
        :param user_pass: 密码
        :return: 存在返回user_id、nick_name ，不存在返回False
        """
        self.logger.info("进入judge_exist_user方法")
        # 1.检查是否存在相同用户
        sql_sentence = sql_statement.info_user.search_user(user_name, user_pass)
        try:
            result_record = sql_operations.SQL().fetch_one(sql_sentence)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("数据库检查是否存在相同用户失败")
            raise e

        result = {}
        if result_record is None:
            return False
        else:
            result['user_id'] = result_record[0]
            result['nick_name'] = result_record[1]

        self.logger.info("退出judge_exist_user方法")
        return result

    def add_user(self, user_name, user_pass, nick_name):
        """
            添加新用户
        :param user_name: 用户名
        :param user_pass: 密码
        :param nick_name: 昵称
        :return:
        """
        self.logger.info("进入add_user方法")
        # 1.添加用户
        sql_sentence = sql_statement.info_user.add_user(user_name, user_pass, nick_name)
        try:
            sql_operations.SQL().excute_one(sql_sentence)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("数据库添加用户失败")
            raise e
        self.logger.info("退出add_user方法")


