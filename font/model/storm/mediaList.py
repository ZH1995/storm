# Created by zh on 2016/4/2.
# -*- coding: UTF-8 -*-


import json
import requests
import logging
import traceback


class mediaList(object):
    """
        媒体列表类
        获取媒体ID、列表，包括标题、类型、图片
    """
    def __init__(self):
        self.logger = logging.getLogger(name='mediaList')

    def get_media_list(self, init_offset, offset):
        """
            获取媒体列表
        :return: media_list列表
                [
                    {'message_id': '', 'headline': '', 'tags': '', 'pic': ''},
                    ...
                ]
        """
        self.logger.info("进入get_media_list")

        # 1.将参数转换成json格式
        jsons = json.dumps(
            {
                'init_offset': init_offset,
                'offset': offset
            }
        ).encode('utf8')

        # 1.获取并解析JSON对象
        try:
            r = requests.get('http://localhost:8805%s' % '/media/media_list', data=jsons)
            json_obj = r.json()
            r.close()
            self.logger.info("远程调用get_media_list成功")
        except Exception:
            self.logger.error(traceback.format_exc())
            self.logger.error("远程调用get_media_list失败")
            raise Exception

        # 2.判断数据是否合法
        if json_obj['result'] == 'fail':
            self.logger.error(json_obj['fail_reason'])
            self.logger.info("退出get_media_list")
            return []
        else:
            media_list = []
            for dic in json_obj['data']:
                my_dic = {}
                for key in dic:
                    my_dic[key] = dic[key]
                media_list.append(my_dic)
            self.logger.info("退出get_media_list")
            return media_list


