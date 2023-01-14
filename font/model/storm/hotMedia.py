# Created by zh on 2016/4/2.
# -*- coding: UTF-8 -*-


import requests
import logging
import traceback


class hotMedia(object):
    """
        热点媒体类
        获取热点图片及相应ID
    """
    def __init__(self):
        self.logger = logging.getLogger(name='hotMedia')

    def get_hot_media(self):
        """
            获取热点媒体
        :return: hot_media列表
                [
                    {'pic': '', 'message_id': '', 'headline': '', 'tags': ''},
                    ...
                ]
        """
        self.logger.info("进入get_hot_media")

        # 1.获取并解析JSON对象
        try:
            r = requests.get('http://localhost:8805%s' % '/media/media_hot')
            json_obj = r.json()
            r.close()
            self.logger.info("远程调用get_hot_media成功")
        except Exception:
            self.logger.error(traceback.format_exc())
            self.logger.error("远程调用get_hot_media失败")
            raise Exception

        # 2.判断数据是否合法
        if json_obj['result'] == 'fail':
            self.logger.error(json_obj['fail_reason'])
            self.logger.info("退出get_hot_media")
            return []
        else:
            hot_media = []
            for dic in json_obj['data']:
                my_dic = {}
                for key in dic:
                    my_dic[key] = dic[key]
                hot_media.append(my_dic)
            self.logger.info("退出get_hot_media")
            return hot_media
