# Created by zh on 2016/4/2.
# -*- coding: UTF-8 -*-


import json
import requests
import logging
import traceback


class mediaContent(object):
    """
        媒体具体内容类
        获取媒体内容、来源、点击量、发布时间
    """
    def __init__(self):
        self.logger = logging.getLogger(name='mediaContent')

    def get_media_content(self, message_id):
        """
            获取媒体具体内容
        :param message_id: 媒体ID
        :return: media_content列表
                {
                    'content': '',
                    'source': '',
                    'click_num': '',
                    'gmt_created': ''
                    'download_addr': ''
                }
        """
        self.logger.info("进入get_media_content")

        # 1.将参数转化成json格式
        jsons = json.dumps({
            'media_id': message_id
        }).encode('utf8')

        # 2.获取并解析JSON对象
        try:
            r = requests.get('http://localhost:8805%s' % '/media/media_content', data=jsons)
            json_obj = r.json()
            r.close()
            self.logger.info("远程调用get_media_content成功")
        except Exception:
            self.logger.error(traceback.format_exc())
            self.logger.error("远程调用get_media_content失败")
            raise Exception

        # 3.判断数据是否合法
        if json_obj['result'] == 'fail':
            self.logger.error(json_obj['fail_reason'])
            self.logger.info("退出get_media_content")
            return []
        else:
            media_content = {}
            for key in json_obj['data']:
                media_content[key] = json_obj['data'][key]
            self.logger.info("退出get_media_content")
            return media_content
