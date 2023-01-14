# Created by zh on 2016/4/1.
# -*- coding: UTF-8 -*-

"""
    info_message相关的sql语句
"""


def select_hot_media():
    """
        从info_message表选取点击数前四的媒体图片及ID
    :return: picture & message_id
    """
    sql = """
        SELECT picture, message_id, headline, tags
        FROM info_message
        ORDER BY click_num DESC
        LIMIT 0, 4
     """
    return sql


def select_media_list(init_offset, offset):
    """
        从info_message表选取从init_offset开始，偏移量为offset的数据
    :param init_offset: 起始数据
    :param offset: 偏移量
    :return:
    """
    sql = """
        SELECT message_id, headline, tags, picture
        FROM info_message
        ORDER BY message_id DESC
        LIMIT %d, %d
    """ % (init_offset, offset)
    return sql


def select_media_content(message_id):
    """
        从info_message表查找message_id的具体媒体信息
    :param message_id: 媒体ID
    :return:
    """
    sql = """
        SELECT content, source, click_num, gmt_created, download_addr
        FROM info_message
        WHERE message_id = %d
    """ % (message_id)
    return sql


def increase_click_num(message_id):
    """
        在info_message表中将click_num字段加1
    :param message_id:
    :return:
    """
    sql = """
        UPDATE info_message
        SET click_num = click_num + 1
        WHERE message_id = %d
    """ % (message_id)
    return sql
