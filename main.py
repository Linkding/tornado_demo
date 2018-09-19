#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Author: linkding
# Email: 619216759@qq.com
# Version: demo

import tornado.ioloop
import tornado.web
import os
import sys
from tornado.options import define,options
from common.url_router import include,url_wrapper

class Application(tornado.web.Application):
  def __init__(self):
    handles = url_wrapper(
      [
        (r"/user/",include('view.user.user_url'))
      ]
    )
    print ('handles: ' , handles)

    # 定义 Tornado 服务器的配置项，如 static/templates 目录位置、debug 级别等
    settings = dict(
      debug=True,
      static_path=os.path.join(os.path.dirname(__file__), "static"),
      template_path=os.path.join(os.path.dirname(__file__), "template")
    )
    # 
    tornado.web.Application.__init__(self, handles, **settings)


if __name__ == "__main__":
  print ("tornado server is ready for service")
  tornado.options.parse_command_line()
  Application().listen(8888, xheaders=True)
  tornado.ioloop.IOLoop.instance().start()
