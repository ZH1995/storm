# Created by zh on 2016/4/3.
# -*- coding: UTF-8 -*-

import tornado.web
import logging
import traceback
from model.storm.loginMmedia import loginMedia


class loginHandler(tornado.web.RequestHandler):
    """
        接收登录信息，判断登录操作
    """
    def initialize(self):
        self.logger = logging.getLogger(name='loginHandler')

    def get(self):
        """
            获取登录信息
            渲染结果页面
        :return:
        """
        self.logger.info('进入loginHandler')
        try:
            # 1.获取用户名、密码
            user_name = self.get_argument('user_name')
            user_pass = self.get_argument('user_pass')

            # 2.调用方法判断结果
            user_info = loginMedia().judge_login_result(user_name, user_pass)

            # 3.根据结果渲染页面

            if user_info is False:
                self.logger.info('退出loginHandler')
                self.redirect('/')
            else:
                user_id = str(user_info['user_id'])
                self.set_cookie('user_id', user_id)
                self.set_cookie('nick_name', user_info['nick_name'])
                self.logger.info(user_info['user_id'])
                self.logger.info(user_info['nick_name'])
                self.logger.info('退出loginHandler')
                self.redirect('/')
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("loginHandler出现问题")
            self.render('media/error.html', e=e)