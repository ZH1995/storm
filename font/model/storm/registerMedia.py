# Created by zh on 2016/4/3.
# -*- coding: UTF-8 -*-


import requests
import logging
import traceback
import json


class registerMedia(object):
    """
        注册媒体类，获得注册验证结果
    """
    def __init__(self):
        self.logger = logging.getLogger(name='registerMedia')

    def judge_register_result(self, user_name, user_pass, nick_name):
        """
            判断注册结果
        :param user_name: 用户名
        :param user_pass: 密码
        :param nick_name: 昵称
        :return: 成功返回user_id, nick_name   失败返回False
        """
        self.logger.info("进入judge_register_result")

        # 1.将参数封装成json对象
        jsons = json.dumps({
            'user_name': user_name,
            'user_pass': user_pass,
            'nick_name': nick_name
        }).encode('utf8')

        try:
            r = requests.get('http://localhost:8805%s' % '/media/register_media', data=jsons)
            json_obj = r.json()
            r.close()
            self.logger.info("远程调用register_media成功")
        except Exception:
            self.logger.error(traceback.format_exc())
            self.logger.error("远程调用register_media失败")
            raise Exception

        if json_obj['result'] == 'fail':
            self.logger.error(json_obj['fail_reason'])
            self.logger.info('退出judge_register_result')
            return False
        else:
            result = {}
            for key in json_obj['data']:
                result[key] = json_obj['data'][key]
            self.logger.info('退出judge_register_result')
            return result
