#!/root/.pyenv/shims/python
# -*- coding:utf-8 -*-

import tornado.web
from tornado.escape import json_decode
import  logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

# 从common中导入http_response方法
from common.commons import  (http_response,)

# 从配置文件导入错误码
from conf.base import (ERROR_CODE,)

# 从model.py导入User类
from model import (Users)

###### configure logging #####
logFilePath = "log/user/user.log"
logger = logging.getLogger("User")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s \
%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',)
handler = TimedRotatingFileHandler(logFilePath,when="D",interval=1,backupCount=30)
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)


class RegistHandle(tornado.web.RequestHandler):

  @property
  def db(self):
    return self.application.db

  def post(self):
    try:
      #获取入参
      args = json_decode(self.request.body)
      print('args: ',args)
      header = self.request.headers
      print('yo ',header["Yo"])
      phone = args['phone']
      password = args['password']
      verify_code = args['code']
    except:
      # 获取入参失败时，抛出错误码及错误信息
      logger.info('RegistHandle: request argument incorrect')
      http_response(self,ERROR_CODE['1001'],1001)
      return

    #判断用户是否存在
    ex_user = self.db.query(Users).filter_by(phone=phone).first()
    if ex_user:
      #如果手机号已经存在，返回用户已注册
      http_response(self,ERROR_CODE['1002'],1002)
      self.db.close()
      return
    else:
      #如果用户不存在，数据库表中插入用户信息
      logger.debug("RegistHandle: insert db,user,: %s" %phone)
      create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      add_user = Users(phone,password,create_time)
      self.db.add(add_user)
      self.db.commit()
      self.db.close()
      # 处理成功后，返回成功码"0"及成功信息"ok"
      logger.debug("RegistHandle: request successfully")
      http_response(self,ERROR_CODE['0'],0)

class TestHandle(tornado.web.RequestHandler):
  def post(self):
    try:
      args = json_decode(self.request.body)
      test = args['test']
      http_response(self, ERROR_CODE['0'], 0)
    except:
      logger.info("test request is fail")
      http_response(self,ERROR_CODE["1003"],1003)

