#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Author: linkding
# Email: 619216759@qq.com
# Version: demo

import tornado.ioloop
import tornado.web
from tornado.options import options,define



class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("hello world")

application = tornado.web.Application([
	(r"/",MainHandler),
])

define('yo',default="yo",help="define var yo")

if __name__ == "__main__":
	# options.parse_config_file("./hello.conf")
	options.parse_command_line()
	print(options.yo)
	application.listen(8888)
	tornado.ioloop.IOLoop.current().start()
