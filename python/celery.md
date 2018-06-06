# celery

celery 是一个简单，灵活且可靠的，处理大量消息的分布式系统，并且提供维护这样一个系统的必备工具。

## 任务队列

任务队列是一种在线程或机器间分发任务的机制

## 消息队列

消息队列的输入是工作的一个单元，称为任务，独立的工作进程(Worker)持续监视队列中是否有需要处理的任务。

celery 用消息通信，通常使用中间人(Broker)在客户端和工作进程之间斡旋。这个过程从向队列添加消息开始，之后中间人把消息派给工作进程，工作进程对消息进行处理。

## celery架构

celery 的架构由三部分组成，消息中间件(Message Broker)，任务执行单元(Worker), 任务执行结果存储(Task Result Store) 组成。

### 消息中间件

celery本身并不提供消息服务，但可以使用第三方提供的消息中间件集成，包括 RabbitMQ，Redis,MongoDB 等。

### 任务执行单元

Worker 是 Celery 的任务执行单元，Worker并发的运行在分布式的系统节点中

### 任务结果存储

Task Result Store 用来存储Worker执行任务的结果，Celery支持不同方式存储任务结果，包括 redis， Mongodb, Django ORM, AMQP等。

## 第一次测试代码

```python
import random
import time

import celery
import dandan
import requests

logger = dandan.logger.getLogger()

app = celery.Celery("tasks", broker="redis://:123456@localhost:6379/0")


@app.task
def test_task(url):
    start = time.time()
    response = requests.get(url)
    end = time.time()
    logger.debug("[%s] %s - %s", end - start, url, response)
    time.sleep(3)


def test():
    urls = [
        "http://www.baidu.com",
        "http://www.163.com",
        "http://www.qq.com",
        "http://www.taobao.com",
        "http://www.tmall.com",
    ]
    for _ in range(10):
        test_task.delay(random.choice(urls))


if __name__ == '__main__':
    test()
```

```sh
# 运行 celery tasks
celery -A tasks worker --loglevel=INFO

# 运行 flower
celery flower --broker="redis://:123456@localhost:6379/0" --address=0.0.0.0 --port=8080
```

## 参考资料

- [1] [Celery - Distributed Task Queue](http://docs.celeryproject.org/en/latest/index.html)
- [2] [Celery 框架学习笔记](https://www.cnblogs.com/forward-wang/p/5970806.html)