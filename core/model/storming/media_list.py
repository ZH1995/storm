# Created by zh on 2016/4/1.
# -*- coding: UTF-8 -*-


import logging
from model.sql import sql_statement
from model.mytools import sql_operations
import traceback


class mediaList(object):
    """
        媒体列表相关信息
    """
    def __init__(self):
        self.logger = logging.getLogger(name='media_list')

    def get_media_list(self, init_offset, offset):
        """
            获取当前媒体列表
        :param init_offset: 初始偏移量
        :param offset: 偏移量
        :return:
                [
                    {'media_is': '', 'headline': '', 'type': '', 'pic': ''},
                    ...
                ]
        """
        self.logger.info("进入get_media_list方法")
        # 1.获取媒体列表信息
        sql_sentence = sql_statement.info_message.select_media_list(init_offset, offset)
        try:
            result_record = sql_operations.SQL().fetch_all(sql_sentence)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("从数据库获取媒体列表失败")
            raise e

        # 2.将result_record封装成列表
        try:
            result = []
            for record in result_record:
                result_tp = {'message_id': record[0], 'headline': record[1], 'tags': record[2], 'pic': record[3]}
                result.append(result_tp)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("媒体列表封装失败")
            raise e
        self.logger.info("退出get_media_list方法")
        return result
