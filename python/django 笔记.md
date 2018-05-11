# django 笔记


## 错误原因及解决方法

1. **django.db.utils.OperationalError: (2006, 'MySQL server has gone away')**

首先，出现 **MySQL server has gone away** 错误的根本原因，是由于MySQL服务器超时，并关闭了与客户端的连接导致的。

默认情况下，如果8小时内对mysql没有请求的话，服务器就会自动断开。可以通过修改全局变量 wait_time 和 interactive_timeout 两个变量的值来进行修改。

不过，这里解释的是django的错误，所以这里只说明从django端来解决这个错误。

django默认情况下对于连接是持续的。但是MySQL端默认只有8个小时，所以要想解决这个问题很简单，在配置文件中修改mysql的最长连接时间就可以了。

所以修改 `settings.py` 文件如下，加入 **CONN_MAX_AGE** 选项:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'CONN_MAX_AGE': 3600,
        # 其他配置信息
    }
}
```
其中 3600 是django对于MySQL连接的最长时间，之后就重新连接。默认情况下 MySQL 数据库的超时时间是 **28800**，小于这个值应该就可以。