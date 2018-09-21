#!/root/.pyenv/shims/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from importlib import import_module

#判断是否注册对应页面的路由，如果存在，获取到此页面所有路由
def include(module):
  res = import_module(module)
  print ('url_router :res = ' , res)
  urls = getattr(res,'urls',res)
  print ('urls: ',urls)
  return urls

def url_wrapper(urls):
  wrapper_list = []
  for url in urls:
    print('url: ',url)
    path,handles = url
    print ('path: ', path ,'handles: ', handles)
    if isinstance(handles,(tuple,list)):
      for handle in handles:
        # 分离获取字符串（如regist）和调用类（如views.users.users_views.RegistHandle）
        pattern, handle_class = handle
        # 拼接url,新的url调用模板
        wrap = ('{0}{1}'.format(path,pattern),handle_class)
        wrapper_list.append(wrap)
    else:
      wrapper_list.append(path,handles)

    print ('wrapper_list: ',wrapper_list)
    return wrapper_list
