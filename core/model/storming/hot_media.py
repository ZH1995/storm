# Created by zh on 2016/4/1.
# -*- coding: UTF-8 -*-


import logging
from model.sql import sql_statement
from model.mytools import sql_operations
import traceback


class hotMedia(object):
    """
        热点媒体相关信息
    """
    def __init__(self):
        self.logger = logging.getLogger(name="hot_media")

    def get_hot_media(self):
        """
            获取当前热点媒体图片及相应message_id
        :return:
                [
                    {'pic': 'pic_url', 'message_id': 'message_id', 'headline': '', 'tags':''},...
                ]
        """
        self.logger.info("进入get_hot_media方法")
        # 1.获取图片路径及相应媒体ID
        sql_sentence = sql_statement.info_message.select_hot_media()
        try:
            result_record = sql_operations.SQL().fetch_all(sql_sentence)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("从数据库获取热点媒体失败")
            raise e

        # 2.将result_record封装成列表
        try:
            result = []
            for record in result_record:
                result_tp = {'pic': record[0], 'message_id': record[1], 'headline': record[2], 'tags': record[3]}
                result.append(result_tp)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("热点媒体封装失败")
            raise e

        self.logger.info("退出get_hot_media方法")
        return result
