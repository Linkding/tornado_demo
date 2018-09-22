options是一个定义全局变量的模块

文件hello.py
```
from tornado.options import options,define

define('yo',default="yo",help="define var yo")

if __name__ == "__main__":
	print(options.yo)
```
输出：
```
(tornado) [root@VM_0_12_centos demo]# python hello.py
yo
```

## parse_command_line
这个模块允许在执行命令行的时候，重新定义变量
文件hello.py
```
from tornado.options import options,define

define('port',default="80",help="define var port")

if __name__ == "__main__":
    options.parse_command_line()
	print(options.port)
```

执行：
```
(tornado) [root@VM_0_12_centos demo]# python hello.py --port=8080
8080
```

这样的场景使用就非常清晰了，可以在执行命令行中去改变已有的变量

## parse_config_file
这个方法，允许通过独立文件来定义options。

文件hello.conf
```
yo="yo"
```

文件hello.py
```
from tornado.options import options,define

if __name__ == "__main__":
	options.parse_config_file("./hello.conf")
	print(options.yo)
```

执行hello.py
```
(tornado) [root@VM_0_12_centos demo]# python hello.py
Traceback (most recent call last):
  File "hello.py", line 25, in <module>
    print(options.yo)
  File "/root/.pyenv/versions/tornado/lib/python3.6/site-packages/tornado/options.py", line 136, in __getattr__
    raise AttributeError("Unrecognized option %r" % name)
AttributeError: Unrecognized option 'yo'
```

**注意：** 在解析变量前，你必须先`define`定义它

```[hello.py]
from tornado.options import options,define

yo="test"
if __name__ == "__main__":
	options.parse_config_file("./hello.conf")
	print(options.yo)
```
输出：
```
(tornado) [root@VM_0_12_centos demo]# python hello.py
yo
```

这样的好处和使用场景，就是允许在不改变原来配置的情况下，独立重新定义options变量，用于测试等，非常方便

[参考1](https://stackoverflow.com/questions/26801231/tornado-parse-config-file-not-working#)