#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Author: linkding
# Email: 619216759@qq.com
# Version: demo

import tornado.ioloop
import tornado.web
import os
import sys
from tornado.options import define, options
from model import initdb
from common.url_router import include,url_wrapper
from sqlalchemy.orm import scoped_session,sessionmaker
from conf.base import BaseDB,engine

class Application(tornado.web.Application):
  def __init__(self):
    initdb(); #创建表结构，如果已有则忽视

    #定义路由
    handles = url_wrapper([
      (r"/user/",include('view.user.user_url')),
    ])

    #定义tornado服务器的配置项，如static/template目录位置，debug级别
    settings = dict(
      debug=True,
      static_path=os.path.join(os.path.dirname(__file__),"static"),
      template_path=os.path.join(os.path.dirname(__file__),"template"),
    )
    tornado.web.Application.__init__(self,handles,**settings)
    self.db = scoped_session(sessionmaker(bind=engine,
                                          autocommit=False,
                                          autoflush=True,
                                          expire_on_commit=False))

if __name__ == "__main__":
  print("Tornado server is ready for service")
  tornado.options.parse_command_line()
  Application().listen(8888,xheaders=True)
  tornado.ioloop.IOLoop.instance().start()