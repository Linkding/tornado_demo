#!/root/.pyenv/shims/python
# -*- coding:utf-8 -*-

import tornado.web
from tornado.escape import json_decode

# 从common中导入http_response方法
from common.commons import  (http_response,)

# 从配置文件导入错误码
from conf.base import (ERROR_CODE,)

class RegistHandle(tornado.web.RequestHandler):
  def post(self):
    try:
      #获取入参
      args = json_decode(self.request.body)
      phone = args['phone']
      password = args['password']
      verify_code = args['code']
    except:
      # 获取入参失败时，抛出错误码及错误信息
      http_response(self,ERROR_CODE['1001'],1001)
      return

    # 处理成功后，返回成功码"0"及成功信息"ok"
    http_response(self,ERROR_CODE['0'],0)
