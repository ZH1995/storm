# Created by zh on 2016/4/3.
# -*- coding: UTF-8 -*-


import tornado.web
import logging
import traceback
from model.storm.registerMedia import registerMedia


class registerHandler(tornado.web.RequestHandler):
    """
        接收注册信息，判断注册操作
    """
    def initialize(self):
        self.logger = logging.getLogger(name='registerHandler')

    def get(self):
        """
            获取注册信息
            渲染结果页面
        :return:
        """
        self.logger.info('进入registerHandler')
        try:
            # 1.获取用户名、密码
            user_name = self.get_argument('user_name')
            user_pass = self.get_argument('user_pass')
            nick_name = self.get_argument('nick_name')

            # 2.调用方法判断结果
            user_info = registerMedia().judge_register_result(user_name, user_pass, nick_name)

            # 3.根据结果渲染页面

            if user_info is False:
                self.logger.info('退出registerHandler')
                self.redirect('/')
            else:
                user_id = str(user_info['user_id'])
                self.set_cookie('user_id', user_id)
                self.set_cookie('nick_name', user_info['nick_name'])
                self.logger.info(user_info['user_id'])
                self.logger.info(user_info['nick_name'])
                self.logger.info('退出registerHandler')
                self.redirect('/')
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("registerHandler出现问题")
            self.render('media/error.html', e=e)