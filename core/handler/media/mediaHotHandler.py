# Created by zh on 2016/4/1.
# -*- coding: UTF-8 -*-


import tornado.web
import logging
import traceback
import json
from model.storming.hot_media import hotMedia
from model.mytools.json_encode import json_encode


class mediaHotHandler(tornado.web.RequestHandler):
    """
        获取热点媒体热点接口
    """
    def initialize(self):
        self.logger = logging.getLogger(name='mediaHotHandler')
        self.add_header('Access-Control-Allow-Origin', '*')

    def get(self):
        """
            获取热点媒体
        :return:
                {
                    'result': 'fail',
                    'fail_reason': '',
                    'data': [
                        {
                            'pic': '', 'message_id': '', 'headline': '', 'tags': ''
                        }
                    ]
                }
        """
        self.logger.info("进入mediaHotHandler")
        # 1.获取热点媒体信息
        try:
            hot_media = hotMedia().get_hot_media()
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("获取热点媒体信息失败")
            self.write(json_encode('fail',u'获取热点图片信息失败'))

        result_info = json.dumps({
            'result': 'success',
            'fail_reason': '',
            'data': hot_media
        }).encode('utf8')

        self.write(result_info)
        self.logger.info("退出mediaHotHandler")
