# Created by zh on 2016/4/1.
# -*- coding: UTF-8 -*-


import tornado.web
import logging
import json
import traceback
from model.storming.media_list import mediaList
from model.mytools import json_encode


class mediaListHandler(tornado.web.RequestHandler):
    """
        获取媒体列表接口
    """
    def initialize(self):
        self.logger = logging.getLogger(name='mediaListHandler')
        self.add_header('Access-Control-Allow-Origin', '*')

    def get(self):
        """
            获取媒体列表信息
            参数包括init_offset, offset
        :return:
            {
                'result': success/fail,
                'fail_reason': '',
                'data': media_list
            }
        """
        self.logger.info("进入mediaListHandler")
        # 1.获取参数
        try:
            argument = json.loads(self.request.body)
            self.logger.info("arguments = %s", argument)
            init_offset = argument['init_offset']
            offset = argument['offset']
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("媒体列表远程获取参数失败")
            self.write(json_encode('fail', u'获取参数失败'))
            return
        # 2.获取媒体列表信息
        try:
            media_list = mediaList().get_media_list(init_offset, offset)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("获取媒体列表信息失败")
            self.write('fail', u'获取媒体列表信息失败')
            return

        result_info = {
            'result': 'success',
            'fail_reason': '',
            'data': media_list
        }
        self.write(json.dumps(result_info).encode('utf8'))
        self.logger.info("退出mediaListHandler")









