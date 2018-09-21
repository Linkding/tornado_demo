#!/root/.pyenv/shims/python
# -*- coding:utf-8 -*-

import  json

def http_response(self,msg,code):
  self.write(json.dumps({'data':{"msg":msg},"code":code}))

# if __name__ == "__main__":
#   http_response()