# Created by zh on 2016/4/2.
# -*- coding: UTF-8 -*-


import tornado.web
import logging
import traceback
from model.storm.mediaContent import mediaContent


class contentHandler(tornado.web.RequestHandler):
    """
        获取媒体具体内容
        渲染具体内容页面
    """
    def initialize(self):
        self.logger = logging.getLogger(name='contentHandler')

    def get(self):
        """
            获取媒体具体内容
        :return: 渲染媒体具体内容页面
                  media_content字典
        """
        self.logger.info("进入contentHandler")

        try:
            # 1.获取媒体基本信息
            media_id = int(self.get_argument('message_id'))
            headline = self.get_argument('headline')
            tags = self.get_argument('tags')
            pic = self.get_argument('pic')

            # 2.获取媒体具体内容
            media_content = mediaContent().get_media_content(media_id)

            # 3.获取cookie
            user_id = self.get_cookie('user_id')
            nick_name = self.get_cookie('nick_name')

            self.logger.info("退出contentHandler,渲染media/content.html页面完成")
            self.render('media/content.html', media_content=media_content, media_id=media_id, headline=headline, pic=pic, tags=tags,
                        user_id=user_id, nick_name=nick_name)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error('contentHandler出现异常')
            self.render('media/error.html', e=e)

