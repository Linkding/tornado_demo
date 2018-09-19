#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Author: linkding
# Email: 619216759@qq.com
# Version: demo

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("hello world")

application = tornado.web.Application([
	(r"/",MainHandler),
])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.current().start()
