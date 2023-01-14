# Created by zh on 2016/4/3.
# -*- coding: UTF-8 -*-


"""
    info_user相关sql语句
"""


def search_user(user_name, user_pass):
    """
        查找用户是否存在
    :param user_name: 用户名
    :param user_pass: 密码
    :return: 用户存在则返回1，不存在返回0
    """
    sql = """
        SELECT user_id, nick_name
         FROM info_user
         WHERE user_name = '%s' and user_pass = '%s'
    """ % (user_name, user_pass)
    return sql


def add_user(user_name, user_pass, nick_name):
    """
        添加新用户
    :param user_name: 用户名
    :param user_pass: 密码
    :param nick_name: 昵称
    :return:
    """
    sql = """
        INSERT INTO info_user
        (user_name, user_pass, nick_name)
        VALUES ('%s', '%s', '%s')
    """ % (user_name, user_pass, nick_name)
    return sql

