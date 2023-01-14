# Created by zh on 2016/4/2.
# -*- coding: UTF-8 -*-


import tornado.web
import logging
import traceback
from model.storm.hotMedia import hotMedia
from model.storm.mediaList import mediaList


class homeHandler(tornado.web.RequestHandler):
    """
        获取热点媒体、媒体列表
        渲染平台首页
    """
    def initialize(self):
        self.logger = logging.getLogger(name='homeHandler')

    def get(self, init_offset=0):
        """
            获取热点媒体、媒体列表
        :param init_offset: 媒体列表的起始条数
        :return: 渲染media/home.html
                  hot_media列表
                  media_list列表
        """
        try:
            # 1.获取热点媒体
            hot_media = hotMedia().get_hot_media()

            # 2.获取媒体列表
            media_list = mediaList().get_media_list(init_offset, offset=10)

            # 3.获取cookie
            user_id = self.get_cookie('user_id')
            nick_name = self.get_cookie('nick_name')

            self.logger.info( user_id)
            self.logger.info("退出homeHandler,渲染hone.html完成")
            self.render('media/home.html', hot_media=hot_media, media_list=media_list, user_id=user_id, nick_name=nick_name)
        except Exception, e:
            self.logger.error(traceback.format_exc())
            self.logger.error("homeHandler出现问题")
            self.render('media/error.html', e=e)

