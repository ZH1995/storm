# Created by zh on 2016/4/2.
# -*- coding: UTF-8 -*-


import tornado.web
import logging
import traceback
import json
from model.storming.media_content import mediaContent
from model.mytools.json_encode import json_encode


class mediaContentHandler(tornado.web.RequestHandler):
    """
        获取媒体具体信息接口
    """
    def initialize(self):
        self.logger = logging.getLogger(name='mediaContentHandler')
        self.add_header('Access-Control-Allow-Origin', '*')

    def get(self):
        """
            获取媒体具体信息
        :return:
                {
                    'result': 'fail',
                    'fail_reason': '',
                    'data': {
                        'content': '',
                        'source': '',
                        'click_num': '',
                        'gmt_created': ''
                        'download_addr': ''
                    }
                }
        """
        self.logger.info("进入mediaContentHandler")
        # 1.获取媒体ID
        try:
            argument = json.loads(self.request.body)
            self.logger.info("argument = %s", argument)
            media_id = argument['media_id']
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("远程获取媒体ID失败")
            self.write(json_encode('fail', u'获取参数失败'))
            return

        # 2.点击量加1
        try:
            mediaContent().increase_click_num(media_id)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("点击量加1失败")

        # 3.获取媒体具体信息
        try:
            media_content = mediaContent().get_media_content(media_id)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("获取媒体具体信息失败")
            self.write(json_encode('fail', u'获取媒体具体失败'))

        self.logger.info(media_content['download_addr'])

        result_info = json.dumps({
            'result': 'success',
            'fail_reason': '',
            'data': media_content
        }).encode('utf8')

        self.write(result_info)
        self.logger.info("退出mediaContentHandler")
