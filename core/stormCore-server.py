# Created by zh on 2016/4/1.
# -*- coding: UTF-8 -*-


import os
import sys
import logging.config
import tornado.ioloop
import tornado.web
import handler
import base64
import uuid

# 设置当前目录为根目录
sys.path.append(os.getcwd())

# 载入日志模板
logging.config.fileConfig(r'config/logging.conf')

settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
    'debug': True
}

media_handlers = [
    (r'/media/media_list', handler.media.mediaListHandler),
    (r'/media/media_hot', handler.media.mediaHotHandler),
    (r'/media/media_content', handler.media.mediaContentHandler),
    (r'/media/login_media', handler.media.loginMediaHanlder),
    (r'/media/register_media', handler.media.registerMediaHanlder)
]

handlers = []
handlers.extend(media_handlers)

if __name__ == '__main__':
    app = tornado.web.Application(handlers=handlers, **settings)
    app.listen(8805)
    tornado.ioloop.IOLoop.instance().start()
