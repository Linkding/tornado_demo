本demo是我学习tornado框架一个记录，我的目的是使用这个框架做一个RESTful的api。

项目架构：
* main.py  tornado实例化对象，主程序入口
* modle.py 数据库交互实例
* common目录 放置公用工具函数，比如解析url
* conf目录  存放配置文件，例如数据库连接信息，接口错误代码定义
* log目录 存放日志
* static目录  静态文件
* template目录 模板文件
* view 视图函数 业务处理逻辑代码目录

