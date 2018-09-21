#!/root/.pyenv/shims/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from .user_view import (
  RegistHandle,
  TestHandle,
)

urls = [
  (r'regist',RegistHandle),
  (r'test',TestHandle),
]