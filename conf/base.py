#!/root/.pyenv/shims/python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:mysql@168@6s.net579.com:21081/demo',echo=False)
BaseDB = declarative_base()

ERROR_CODE = {
  "0":"ok",
  "1001":"入参非法",
  "1002":"用户已注册，请直接登录",
  "1003":"test api requset fail"
}
