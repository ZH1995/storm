# Created by zh on 2016/4/3.
# -*- coding: UTF-8 -*-


import tornado.web
import logging
import traceback
import json
from model.storming.login_media import loginMedia
from model.mytools.json_encode import json_encode


class loginMediaHanlder(tornado.web.RequestHandler):
    """
        登录媒体接口
    """
    def initialize(self):
        self.logger = logging.getLogger(name='loginMediaHandler')
        self.add_header('Access-Control-Allow-Origin', '*')

    def get(self):
        """
            获取登录信息
        :return:
            {
                'result'： success/fail
                'fail_reason': ''
                'data': {
                    'user_id': message_id,
                    'nick_name': nick_name
                }
            }
        """
        self.logger.info("进入loginMediaHandler")

        # 1.获取参数
        try:
            argument = json.loads(self.request.body)
            self.logger.info("argument = %s", argument)
            user_name = argument['user_name']
            user_pass = argument['user_pass']
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("远程获取用户名、密码失败")
            self.write(json_encode('fail', u'获取参数失败'))
            return

        # 2.判断用户是否存在
        try:
            user_info = loginMedia().judge_exist_user(user_name, user_pass)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("判断用户是否存在失败")
            self.write(json_encode('fail', u'判断用户是否存在失败'))

        if user_info is False:
            self.write(json_encode('fail', u'用户不存在'))
        else:
            result_info = json.dumps({
                'result': 'success',
                'fail_reason': '',
                'data': user_info
            }).encode('utf8')
            self.write(result_info)

        self.logger.info("退出loginMediaHandler")