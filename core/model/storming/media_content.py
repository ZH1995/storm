# Created by zh on 2016/4/2.
# -*- coding: UTF-8 -*-


import logging
from model.sql import sql_statement
from model.mytools import sql_operations
import traceback


class mediaContent(object):
    """
        媒体具体信息
    """
    def __init__(self):
        self.logger = logging.getLogger(name="media_content")

    def get_media_content(self, media_id):
        """
            获取媒体具体信息
        :param media_id: 媒体ID
        :return:
                {
                'content': '',
                'source': '',
                'click_num':'',
                'gmt_created':''
                'download_addr': ''
            }
        """
        self.logger.info("进入get_media_content方法")

        # 1.获取媒体具体信息
        sql_sentence = sql_statement.info_message.select_media_content(media_id)
        try:
            result_record = sql_operations.SQL().fetch_one(sql_sentence)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("从数据库获取媒体具体信息失败")
            raise e

        # 2.将result_record封装成字典
        try:
            result = {}
            result['content'] = result_record[0]
            result['source'] = result_record[1]
            result['click_num'] = str(result_record[2])
            result['gmt_created'] = str(result_record[3])
            result['download_addr'] = result_record[4]
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("媒体具体信息封装失败")
            raise e

        self.logger.info("退出get_media_content方法")
        return result

    def increase_click_num(self, media_id):
        """
            点击量加1
        :param media_id: 媒体ID
        :return: null
        """
        self.logger.info("进入increase_click_num")

        sql_sentence = sql_statement.info_message.increase_click_num(media_id)
        try:
            sql_operations.SQL().excute_one(sql_sentence)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("数据库点击量字段加1失败")
            raise e

        self.logger.info("退出increase_click_num")
