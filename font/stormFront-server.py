# Created by zh on 2016/4/2.
# -*- coding: UTF-8 -*-


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
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'debug': True
}

media_handlers = [
    (r'/', handler.media.homeHandler),
    (r'/content', handler.media.contentHandler),
    (r'/personal', handler.media.personalHandler),
    (r'/login', handler.media.loginHandler),
    (r'/register', handler.media.registerHandler),
]

static_file_handlers = [
    (r'/template/(.*)', tornado.web.StaticFileHandler, {'path': settings['template_path']})
]

handlers = []
handlers.extend(media_handlers)
handlers.extend(static_file_handlers)

if __name__ == '__main__':
    app = tornado.web.Application(handlers=handlers, **settings)
    app.listen(8804)
    tornado.ioloop.IOLoop.instance().start()
