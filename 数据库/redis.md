# redis

REmote DIctionary Server(Redis) 是一个由Salvatore Sanfilippo写的key-value存储系统。

Redis是一个开源的使用ANSI C语言编写、遵守BSD协议、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。

它通常被称为数据结构服务器，因为值（value）可以是 字符串(String), 哈希(Map), 列表(list), 集合(sets) 和 有序集合(sorted sets)等类型。

## 简介

Redis 是完全开源免费的，遵守BSD协议，是一个高性能的key-value数据库。

Redis 与其他 key - value 缓存产品有以下三个特点：

- Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
- Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
- Redis支持数据的备份，即master-slave模式的数据备份。 

## 优点

- 性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。
- 丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
- 原子 – Redis的所有操作都是原子性的，意思就是要么成功执行要么失败完全不执行。单个操作是原子性的。多个操作也支持事务，即原子性，通过MULTI和EXEC指令包起来。
- 丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。

## 配置

### 主从配置

    slaveof 192.168.211.129  6379

### 连接认证

    requirepass password

### 配置日志

```shell
mkdir -p /var/log/redis
chown redis redis
logfile "/var/log/redis/redis.log"
```

### 持久化

```shell
dbfilename "dump.rdb"
dir "/var/lib/redis"
```
## 链接数据库

    redis-cli -h host -p port -a password

## 数据类型

### String 字符串

string是redis最基本的类型，你可以理解成与Memcached一模一样的类型，一个key对应一个value。

string类型是二进制安全的。意思是redis的string可以包含任何数据。比如jpg图片或者序列化的对象 。

string类型是Redis最基本的数据类型，一个键最大能存储512MB。 

```redis
redis 127.0.0.1:6379> SET name "runoob"
OK
redis 127.0.0.1:6379> GET name
"runoob"
```
在以上实例中我们使用了 Redis 的 SET 和 GET 命令。键为 name，对应的值为 runoob。

注意：一个键最大能存储512MB。

### Hash 哈希

Redis hash 是一个键值(key=>value)对集合。

Redis hash 是一个string类型的field和value的映射表，hash特别适合用于存储对象。

```redis
redis> HMSET myhash field1 "Hello" field2 "World"
"OK"
redis> HGET myhash field1
"Hello"
redis> HGET myhash field2
"World"
```
以上实例中 hash 数据类型存储了包含用户脚本信息的用户对象。 实例中我们使用了 Redis HMSET, HGETALL 命令，user:1 为键值。每个 hash 可以存储 232 -1 键值对（40多亿）。

### List 列表

Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。

```redis
redis 127.0.0.1:6379> lpush runoob redis
(integer) 1
redis 127.0.0.1:6379> lpush runoob mongodb
(integer) 2
redis 127.0.0.1:6379> lpush runoob rabitmq
(integer) 3
redis 127.0.0.1:6379> lrange runoob 0 10
1) "rabitmq"
2) "mongodb"
3) "redis"
```
表最多可存储 2^32 - 1 元素 (4294967295, 每个列表可存储40多亿)。 

### Set 集合

Redis的Set是string类型的无序集合。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1)。

sadd 命令

添加一个 string 元素到 key 对应的 set 集合中，成功返回1，如果元素已经在集合中返回 0，如果 key 对应的 set 不存在则返回错误。

```redis
redis 127.0.0.1:6379> sadd runoob redis
(integer) 1
redis 127.0.0.1:6379> sadd runoob mongodb
(integer) 1
redis 127.0.0.1:6379> sadd runoob rabitmq
(integer) 1
redis 127.0.0.1:6379> sadd runoob rabitmq
(integer) 0
redis 127.0.0.1:6379> smembers runoob

1) "redis"
2) "rabitmq"
3) "mongodb"
```

以上实例中 rabitmq 添加了两次，但根据集合内元素的唯一性，第二次插入的元素将被忽略。
集合中最大的成员数为 2^32 - 1(4294967295, 每个集合可存储40多亿个成员)。 

### Zset (Sorted set) 有序集合

Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。

不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。

zset的成员是唯一的,但分数(score)却可以重复。

```redis
redis 127.0.0.1:6379> zadd runoob 0 redis
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 mongodb
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 rabitmq
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 rabitmq
(integer) 0
redis 127.0.0.1:6379> > ZRANGEBYSCORE runoob 0 1000
1) "mongodb"
2) "rabitmq"
3) "redis"
```

## 命令

| 命令 | 描述 |
| - | - |
| select 0 | 选择数据库 0|
| dbsize | 当前数据库的 key 的数量 |
| flushall | 删除所有数据库的所有Key |
| flushdb | 删除当前数据库的所有key |
| DEL key | 删除 key |
| DUMP key | 序列化 key |
| EXISTS key | 检查给定 key 是否存在 |
| EXPIRE key seconds | 为给定 key 设置过期时间 |
| EXPIREAT key timestamp | 设置 key 的过期时间是 UNIX 时间戳(unix timestamp) |
| PEXPIRE key milliseconds | 设置 key 的过期时间以毫秒计 |
| KEYS pattern | 查找所有符合给定模式( pattern)的 key  |
| MOVE key db | 将当前数据库的 key 移动到给定的数据库 db 当中 |
| PERSIST key | 移除 key 的过期时间，key 将持久保持 |
| PTTL key | 以毫秒为单位返回 key 的剩余的过期时间 |
| TTL key | 以秒为单位，返回给定 key 的剩余生存时间(TTL, time to live) |
| RANDOMKEY | 从当前数据库中随机返回一个 key |
| RENAME key newkey | 修改 key 的名称 |
| RENAMENX key newkey | 仅当 newkey 不存在时，将 key 改名为 newkey |
| TYPE key | 返回 key 所储存的值的类型 |

## 发布订阅

首先做简单的引入。

MQ主要是用来：

- 解耦
- 异步化消息
- 流量削峰填谷

目前使用的较多的有ActiveMQ、RabbitMQ、ZeroMQ、Kafka、MetaMQ、RocketMQ等。

Redis 发布订阅(pub/sub)是一种消息通信模式：发送者(pub)发送消息，订阅者(sub)接收消息。

Redis 客户端可以订阅任意数量的频道。

**redis-py** 包含一个 PubSub 对象可以订阅通道，监听通道来获得新消息。创建pubsub对象很简单。

```python
r = redis.StrictRedis(...)
p = r.pubsub()
```

一旦PubSub对象创建，通道和模式就可以被订阅了。

```python
p.subscribe('my-first-channel', 'my-second-channel', ...)
p.psubscribe('my-*', ...)
p.get_message()
```

然后就可获取消息了。

```python
{'pattern': None, 'type': 'psubscribe', 'channel': 'my-*', 'data': 3L}
```

消息是一个字典，包括了以下几个键：

- type 下面的其中之一: 'subscribe', 'unsubscribe', 'psubscribe', 'punsubscribe', 'message', 'pmessage'
- channel 通道信息
- pattern 除了pmessage 以外，其他的都为空
- data 消息数据

```python
#!/usr/bin/python3
# coding=utf-8

'''
Description: publisher
Author: Steven Kang
Datetime: 2018-05-31 11:41:31
'''

import time
import dandan
from redis import StrictRedis

logger = dandan.logger.getLogger()

redis = StrictRedis(password=123456, db=0)
channel = "test"

for _ in range(100):
    message = "message {}".format(time.time())
    logger.info("send %s", message)
    redis.publish(channel, message)
    time.sleep(0.5)
```

```python
import time
import dandan
from redis import StrictRedis

logger = dandan.logger.getLogger()

redis = StrictRedis(password=123456)
channel = "test"

pub = redis.pubsub(ignore_subscribe_messages=True)
pub.subscribe(channel)
message = pub.parse_response()

logger.info(message)

while True:
    message = pub.parse_response(timeout=5)
    if not message:
        break
    logger.info("receive %s", message)
    time.sleep(0.5)

```




## 参考资料

- [1] [Redis 教程 ](http://www.runoob.com/redis/redis-tutorial.html)
- [2] [redis实现消息队列（实时消费+ack机制）](https://segmentfault.com/a/1190000012244418)
- [3] [redis-py](https://github.com/andymccurdy/redis-py)