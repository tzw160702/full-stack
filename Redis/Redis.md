<center><font size=8><big>Redis</big></font></center>
* **Redis（Remote Dictionary Server ，远程字典服务） 是一个使用ANSI C编写的开源、支持网络、基于内存、可选持久性的键值对存储数据库，是NoSQL数据库。 **

* **Redis 特性: 速度快、持久化、多种数据结构、支持多种编程语言、功能丰富、简单：代码短小精悍、主从复制、高可用、分布式**

* **Redis 的应用场景包括：缓存系统（“热点”数据：高频读、低频写）、计数器、消息队列系统、排行榜、社交网络和实时系统。 **

* **Redis 的数据类型及主要特性： Redis提供的数据类型主要分为5种自有类型和一种自定义类型，5种自有类型是（String类型、哈希类型、列表类型、集合类型和顺序集合类型 ）**



## 1.Redis 安装

* 以下ubuntu(其它操作系统自行百度)安装步骤：

```redis
安装命令：sudo apt-get install -y redis-server
卸载命令：sudo apt-get purge --auto-remove redis-server 
关闭命令：sudo service redis-server stop 
开启命令：sudo service redis-server start 
重启命令：sudo service redis-server restart
配置文件：/etc/redis/redis.conf

进入redis服务: redis-cli --raw   # --raw中文正常显示
```

## 2.Redis 配置
* linux下redis默认配置文件路径：/etc/redis/redis.conf(启动时用的这个配置文件)
* redis 核心配置选项

```redis.conf
# 绑定ip：访问白名单，如果需要远程访问注释掉即可或绑定一个真实ip
bind 127.0.0.1   xx.xx.xx.xx

# 端⼝：默认为6379
port 6379

# 是否守护进程运行
# 如果以守护进程运行，则不会在命令阻塞，类似于服务
# 如果以守护进程运行，则当前终端被阻塞
# 设置为yes表示守护进程，设置为no表示⾮守护进程（推荐设置为yes）
daemonize yes

# RDB持久化的备份策略（RDB备份是默认开启的）
# save 时间 读写次数
save 900 1 当redis在900s内至少有1次读写操作，则触发一次数据库的备份操作
save 300 10 当redis在300s内至少有10次读写操作，则触发一次数据库的备份操作
save 60 10000 当redis在60s内至少有1000次读写操作，则触发一次数据库的备份操作
# 持久化如果出错是否还需要继续工作
stop-writes-on-bgsave-error yes     
# 是否压缩rdb文件, 需要消耗cpu资源 
rdbcompression yes
# 保存rdb文件的时候,进行错误的检查校验
rdbchecksum yes
# RDB 持久化备份文件
dbfilename dump.rdb
# RDB 持久化数据库数据文件的所在目录
# 手动设置
dir ./
 
# 日志文件目录
loglevel notice
logfile /var/log/redis/redis-server.log

# 进程ID
pidfile /var/run/redis/redis-server.pid

# 数据库默认有16个，数据库ID是不能自定义的，只能是0-15之间 
databases 16

# 是否显示logo
always-show-logo  

# redis的登录密码，生产阶段打开，开发阶段避免麻烦，一般都是注释的。
# redis在6.0版本以后新增了ACL访问控制机制，新增了用户管理，这个版本以后才有账号和密码，在此之前只有没有密码没有账号
# 注意：开启了以后，redis-cli终端下使用 auth 密码来认证登录。
# requirepass foobared

# redis客户端最大连接数
maxclients 10000
# redis 配置的最大内存容量
maxmemory <bytes>
# 内存达到上限之后的处理策略
maxmemory-policy noeviction

# AOF持久化的开启配置项(默认值是no，关闭状态, 大部分情况下rdb完全够用)
appendonly no
# AOF持久化的备份文件（AOF的备份数据文件与RDB的备份数据文件保存在同一个目录下，由dir配置项指定）
appendfilename "appendonly.aof"
AOF持久化备份策略（时间）
# appendfsync always    # 每次修改都会备份
appendfsync everysec    # 工作中最常用,每一秒备份一次
# appendfsync no        # 不执行, 操作系统自己备份, 速度最快

# 
```

## 3.Redis 数据类型

```redis
redis可以理解成一个全局的大字典，key就是数据的唯一标识符。根据key对应的值不同，可以划分成5个基本数据类型。
1. string类型:
    字符串类型，是 Redis 中最为基础的数据存储类型，它在 Redis 中是二进制安全的，也就是byte类型。
    单个数据的最大容量是512M。
        key: 值
    
2. hash类型:
    哈希类型，用于存储对象/字典，对象/字典的结构为键值对。key、域、值的类型都为string。域在同一个hash中是唯一的。
        key:{
            域（属性）: 值，
            域:值，            
            域:值，
            域:值，
            ...
        }
        
3. list类型:
    列表类型，它的子成员类型为string。
        key: [值1，值2, 值3.....]
        
4. set类型:
    无序集合，它的子成员类型为string类型，元素唯一不重复，没有修改操作。
        key: {值1, 值4, 值3, ...., 值5}

5. zset类型(sortedSet):
    有序集合，它的子成员值的类型为string类型，元素唯一不重复，没有修改操作。权重值(score,分数)从小到大排列。
        key: {
            值1 权重值1(数字);
            值2 权重值2;
            值3 权重值3;
            值4 权重值4;
        }
```

**选择数据库:** `select database_number`

### 3.0 Redis key操作

#### (1) 查找键

```redis
# 查看所有键(key)
keys * 

# 参数支持简单的正则匹配
# 查看名称中包含a的键
keys *a*
# 查看以a开头的键
keys a*
# 查看以a结尾的键
keys *a
```

#### (2) 判断键是否存在

```redis
# 判断键是否存在<如果存在返回1, 不存在返回0>
exists key

# eg:判断name是否存在
127.0.0.1:6379> exists name
1
# name1不存在
127.0.0.1:6379> exists name1
0
```

#### (3) 查看键的值的数据类型

```redis
type key
# string   字符串
# hash     哈希类型(字典)
# list     数组类型(列表)
# set      无序集合
# zset     有序集合

# eg:
127.0.0.1:6379> set a1 a1    # 字符串
OK
127.0.0.1:6379> type a1
string
127.0.0.1:6379> lpush a2 1 2 3 4     # 列表
4
127.0.0.1:6379> type a2
list
127.0.0.1:6379> hset a3 name zy    # 对象
1
127.0.0.1:6379> type a3
hash
127.0.0.1:6379> sadd a4 1 2 3 3 4 5 5   # 集合
5
127.0.0.1:6379> type a4
set
127.0.0.1:6379> zadd a5 1 name 2 age 3 addr   # 有序集合
3
127.0.0.1:6379> type a5
zset
```

#### (4) 设置key的有效期

```redis
# 方式一
set 设置键值同时设置有效期
set key value EX 过期时间(s)      
# 如果想设置、访问毫秒级别的时间
set key value PX 过期时间(ms)   # 设置
pttl  key   #访问

# 方式二
setex 设置键值同时设置有效期
setex key 过期时间(s) value

# 给已有的键重新设置有效期,redis中所有的数据都可以通过expire来设置它的有效期。# 有效期到了，数据就会被删除。
expire key 过期时间(s)       # 秒
pexpire key 过期时间(ms)     # 毫秒

# 取消过期时间
persist key
# 返回值：
#	1 if the timeout was removed.
#	0 if key does not exist or does not have an associated timeout.
```

#### (5) 查看键的有效期

```redis
ttl key 
# 查询结果是秒作为单位的整数:
# 	-1 表示永不过期
# 	-2 表示当前数据已经过期, 查看一个不存在的数据的有效期就是-2
```

#### (5) 重命名键

```redis
rename oldkey newkey
```

#### (6) 删除键及键对应的值

```sql
# 删除指定key
del key1 key2 ...

# eg:
127.0.0.1:6379> keys *     # 查看所有key
a3
age
name
a2
addr
a1
a5
a4
127.0.0.1:6379> del age addr name    # 删除age、addr、name三个key
3
127.0.0.1:6379> keys *
a3
a2
a1
a5
a4

# 删除当前库所有key
flushdb

# 删除redis所有数据库0~15的全部key都会被清除
flushall
```

###  3.1 String(字符串)

*  字符串string: 用于保存项目中普通数据，只要是键值对都可以保存，
* 使用场景: 保存 session/jwt、定时记录状态、倒计时、验证码、防灌水答案 

#### (1)设置键值

```redis
# set 设置的数据没有额外操作时，是不会过期的。
set kye value   # 一个key可以设置多次
# 注意: redis 中所有的数据操作，如果设置的键不存在则添加，如果设置的键已经存在则修改。

# setnx 设置一个键, 当键不存在时才能设置成功, 用于一个变量只能被设置一次的情况 <0 表示不成功, 1表示成功>
setnx key value    # 一般用于给数据加锁(分布式锁)

# mset 设置多个键
mset key1 value1 key2 value2 ...
```

#### (2) 字符串拼接值

```
# append 常见于大文件上传
append key value  # 如果key不存在会自动创建
```

#### (3) 根据键取值

```redis
# get 取单个键的值
get key

# mget 取多个键的值
mget key1 key2 key3 ...

# getset 设置key的新值, 返回旧值
getset key new_vlaue    # 如果设置的key不存在返回nil, 因为没有旧值
```

#### (4) 自增自减

```redis
# 自增+1 increase
incr key   #  +1 

# 自减-1 decrease
decr key   # -1

# 自增自减大于小于1 incrby
incrby key 

# eg:
127.0.0.1:6379> set id 10
OK
127.0.0.1:6379> incr id
11
127.0.0.1:6379> decr id
10
127.0.0.1:6379> incrby id -2
8
127.0.0.1:6379> incrby id 2
10
```

#### (5) 获取字符串的长度

```redis
strlen key  
# unicode编码中一个汉字是占用三个字节
```

### 3.2 List(数组)

* 列表list: 用于保存项目中的列表/切片数据，但是也不能保存多维结构，
* 使用场景: 消息队列、秒杀系统、排队

#### (1) 添加成员

```redis
# 查看数组的key是否存在
exists key    # 返回值: <0表示不存在, 1表示存在>

# lpush在数组左侧(最前)添加一个元素
lpush key value1 value2 value3 ...

# rpush在数组右侧(最后)添加一个元素
rpush key value1 value2 value3 ...

# linsert 在数组的指定成员前/后添加一个元素
linsert key before exist_value new_value    # 在指定元素之前添加
linsert key after exist_value new_value     # 在指定元素之后添加
# 注意: 当列表如果存在多个成员值一致的情况下, 默认识别第一个元素。
```

#### (2) 获取数组成员

```redis
# 根据指定索引(下标)获取成员的值, 负数下标从右边-1开始,逐个递减 左边下标从0开始
lindex key index

# 移除并获取列表第一个或最后一个成员
# 移除第一个成员
lpop key   
# 移除最后一个成员 
rpop key

# 获取数组的切片
lrange key start stop      # 起始下标从0开始, 最后一个值下标为-1 
# eg: 获取全部成员
lrange key 0 -1
```

#### (3) 获取数组长度

```redis
llen key
```

#### (4) 按索引设置值

```redis
lset key index value
# redis的列表也有索引，从左往右，从0开始，逐一递增，第1个元素下标为0
# 索引可以是负数，表示末尾开始计数，如`-1`表示最后1个元素
```

#### (5) 删除指定成员

```redis
# lrem 删除指定成员
lrem key count value    # 该命令默认表示将从列表左侧前count个value的元素移除
# count 表示删除的数量, value表示要删除的成员. 
# count == 0, 表示删除列表所有值为value的元素
# count > 0, 表示删除列表左侧开始的前count个value的元素
# count < 0, 表示删除列表右侧开始的前count个value的元素

# 移除数组的最后一个元素, 并到一个新的数组中
rpoplpush old_key new_key

# 截取\截断, 截取的部分作为新的数组
ltrim key start_index stop_index
```

### 3.3 Hash(哈希)

* 哈希hash: 用于保存项目中的一些结构体/map类型数据，但是不能保存多维结构
* 使用场景: 商城的购物车、文章信息、json结构数据 

#### (1) 设置指定key的属性/域

```redis
hset key field value
# key 不存在会自动创建
# key 中不存在的field(属性)会自动创建
# key 中重复的field(属性)会被修改
# eg:
127.0.0.1:6379> hset info:1 age 18 addr 陕西   # info:1 会在redis界面操作中以:作为目录分隔符
2
127.0.0.1:6379> hset info:1 age 15 addr 山西
0
127.0.0.1:6379> hget info:1 addr 
山西
127.0.0.1:6379> hget info:1 age
15
```

#### (2) 获取指定key的属性/域的值

```redis
# 获取指定key的所有属性/域
hkeys key

# 获取指定key的指定属性/域的值
hget key field 

# 获取指定key的指定多个属性/域的值
hmget info field1 field2 field3 ...

# 获取指定key的所有属性/域的值
hvals key

# 获取指定key的所有hash属性/域值对
hgetall key 
```

#### (3) 获取hash 表中字段的数量

```redis
hlen key
```

#### (4) 删除指定key的属性/域 

```redis
hdel key field 
```

#### (5) 判断指定的属性/域是否存在于当前key对应的hash中

```redis
hexists key field    # 返回值: <0表示不存在, 1表示存在>
```

#### (6) 属性/域值的自增自减

```redis
hincrby key field number   # key不存在会自动创建 

# eg:
127.0.0.1:6379> hincrby info num 20      # 自增
20
127.0.0.1:6379> hincrby info num -10     # 自减
10
127.0.0.1:6379> hget info num
10
```

### 3.4 Set(集合)

*  set: 用于保存项目中的一些不能重复的数据，可以用于过滤
*   应用场景: 作者名单、有序集合 

#### (1) 添加集合的元素 

```redis
sadd key member1 member2 member3 ...
```

#### (2) 获取集合元素

```redis
# smembers 查看集合中所有元素
smembers key 

# simembers 查看集合中指定的元素
sismembers key value    # 返回值: <0表示不存在, 1表示存在>

# srandmember 随机抽取元素
srandmember key

# spop 随机抽取一个或多个元素, 抽取出来的元素会被删除
spop key [count=1]      # count 为可选参数, 不填默认取1个元素
```

#### (3) 获取集合长度

```redis
scard key
```

#### (4) 删除指定元素

```redis
# srem 删除指定成员
srem key value     # 返回值: <0表示不成功, 1表示成功>

# smove 将指定成员移除到另一个集合中
smove source(旧集合) destination(新集合) member(旧集合元素)
```

#### (5) 差集、交集、并集

*  推荐、（协同过滤、基于用户、基于物品） 

```redis
sinter  key1 key2 key3 ....    # 交集、比较多个集合中共同存在的成员
sdiff   key1 key2 key3 ....    # 差集、A={1,2,3,4,5} B={1,2,3,6} 差集B-A={6} 即把B中属于A的元素去掉
sunion  key1 key2 key3 ....    # 并集、合并所有集合的成员，并去重

# eg
127.0.0.1:6379> sadd number1 1 2 3 4
4
127.0.0.1:6379> sadd number2 1 3 4 5
4
127.0.0.1:6379> sadd number3 1 3 5 6
4
127.0.0.1:6379> sadd number4 2 3 4 
3
127.0.0.1:6379> sinter number1 number4     # 交集
2
3
4
127.0.0.1:6379> sdiff number2 number3     # 差集
4

127.0.0.1:6379> sunion number3 number4    # 并集
1
2
3
4
5
6
```

### 3.5 Zset(有序集合)

* 有序集合zset: 用于保存项目中一些不能重复，但是需要进行排序的数据,
* 使用场景: 分数排行榜、海选人排行榜、热搜排行

#### (1) 添加集合的元素 

```redis
# 有序集合，去重并且根据score权重值来进行排序的, score从小到大排列。
zadd key score1 member1 score2 member2 score3 member3 ...

# eg:
127.0.0.1:6379> zadd zset 1 name 2 age 3 sex
3
```

#### (2) 获取指定区间的成员

```redis
# 取区间成员
zrangebyscore key min max     # 按score进行从低到高排序获取指定score区间
zrevrangebyscore key max min  # 按score进行从高往低排序获取指定score区间
zrange key start stop         # 按scoer进行从低往高排序获取指定索引区间
zrevrange key start stop      # 按scoer进行从高往低排序获取指定索引区间
# eg:
127.0.0.1:6379> zadd zset 10 zy 23 zpc 18 tyl 26 tzw 27 jph
5
127.0.0.1:6379> zrangebyscore zset 9 25 withscores   # 按zset中的score从低到高排序, 取区间[左小右大]在9~25的score值 
zy
10
tyl
18
zpc
23
127.0.0.1:6379> zrevrangebyscore zset 30 25 withscores    # 按zset中的score从高到低排序, 取区间[左大右小]在30~25的score值
jph
27
tzw
26
127.0.0.1:6379> zrange zset 0 -1 withscores    # 取所有元素按zset中的score从低到高排序, 取在索引区间的元素
zy
10
tyl
18
zpc
23
tzw
26
jph
27
127.0.0.1:6379> zrevrange zset 0 -1 withscores    按zset中的score从高到低排序, 取在索引区间的元素
jph
27
tzw
26
zpc
23
tyl
18
zy
10


# Zinterstore 命令计算给定的一个或多个有序集的【交集】
# 计算numkeys个有序集合的交集, 并且把结果放到destination中
# 在给定要计算的 key 和其它参数之前，必须先给定 key 个数(numberkeys)
# 默认情况下，结果集中某个成员的分数值是所有给定集下该成员分数值之和。
ZINTERSTORE destination numkeys key1 key2 key3 ...
# eg:
127.0.0.1:6379> zadd zset1 1 name 2 age 3 sex
3
127.0.0.1:6379> zadd zset2 3 name 2 age1 3 sex
3
127.0.0.1:6379> zadd zset3 1 name2 2 age1 3 sex
3
127.0.0.1:6379> zinterstore zset 3 zset1 zset2 zset3
1
127.0.0.1:6379> zrange zset 0 -1 withscores
sex
9
```

#### (3) 获取有序集合的长度

```redis
zcard key 
```

#### (4) 获取指定成员的权重值

```redis
zscore key member
```

#### (5) 获取指定成员在有序集合中的排名

```redis
# 排名从0开始计算
zrank key member      # score从小到大的排名
zrevrank key member   # score从大到小的排名

# eg:
127.0.0.1:6379> zadd zset 33 zz 44 zpc 55 tzw 66 wjf
4
127.0.0.1:6379> zrank zset tzw
2
127.0.0.1:6379> zrevrank zset tzw
1
```

#### (6) 获取score在指定区间的所有成员数量

```redis
zcount key min max

# eg:
127.0.0.1:6379> zadd zset 33 zz 44 zpc 55 tzw 66 wjf
4
127.0.0.1:6379> zcount zset 0 60    # 获取zset score的值在0~60之间的member数
3
```

#### (7) 给有序集合中的指定成员(member)增加/减少权重值

```redis
zincrby key increment member     #在现有的member的score值上增加/或减少  -10 表示减少10个
```

#### (8) 删除元素

```redis
# zrem 删除有序结合中指定的member
zrem key member1 member2 member3 ...

# 删除指定数量的成员
# 删除指定数量的成员，从最低的score开始删除
zpopmin key [count=1]     # count 为可选参数, 不填默认取1个元素
# 删除指定数量的成员，从最高的score开始删除
zpopmax key [count=1]     # count 为可选参数, 不填默认取1个元素

# 移除有序集中score由低到高的指定排名(rank)区间内的所有成员
zremrangebyrank key start stop
```

## 4 . 事务

* redis单条命令的执行是原子性的，但是事务不保证原子性
* redis 事务本质:  一组(多行)命令的集合。一个事务中的所有命令都会被序列化, 执行过程中，事务会按顺序执行
*  事务执行中任意命令执行失败，其余的命令依然被执行 
* redis 事务没有隔离级别的概念

> 举个例子：事务可以理解为一个打包的批量执行脚本，但批量指令并非原子化的操作，中间某条指令的失败不会导致前面已做指令的回滚，也不会造成后续的指令不做。

### 4.1 执行事务

* 事务从开始到执行会经历三个阶段 ：

  * 开启事务(multi)
  * 命令入队(......)
  * 执行事务(exec)

```redis
# 正常执行事务
127.0.0.1:6379> multi              # 开启事务
OK
127.0.0.1:6379(TX)> set k1 v1      # command1 被放入队列缓存
QUEUED
127.0.0.1:6379(TX)> set k2 v2      # command2 被放入队列缓存
QUEUED
127.0.0.1:6379(TX)> get k1         # command3 被放入队列缓存
QUEUED
127.0.0.1:6379(TX)> exec           # 执行事务, 事务执行完表示当前事务就结束了
OK
OK
v1

# discard 取消事务，放弃执行事务块内的所有命令
127.0.0.1:6379> multi                  # 开启事务
OK
127.0.0.1:6379(TX)> hset info name zzz
QUEUED
127.0.0.1:6379(TX)> hget info name
QUEUED
127.0.0.1:6379(TX)> discard          # 取消事务, 命令队列都不会执行
OK

# 注意*: 
# 1. 如果命令有错, 事务中的所有命令都不会被执行
127.0.0.1:6379> multi
OK
127.0.0.1:6379(TX)> hset info name zzz
QUEUED
127.0.0.1:6379(TX)> hget info name
QUEUED
127.0.0.1:6379(TX)> hegt1 info name
ERR unknown command 'hegt1', with args beginning with: 'info' 'name' 

127.0.0.1:6379(TX)> exec
EXECABORT Transaction discarded because of previous errors.

# 2.如果事务中存在语法错误, 其它命令也是可以执行的
127.0.0.1:6379> set id ddd           # 设置一个key为id, sting为dddd的键值对
OK
127.0.0.1:6379> multi
OK
127.0.0.1:6379(TX)> incr id          # id的值为字符串,不能进行加减
QUEUED
127.0.0.1:6379(TX)> set name zy
QUEUED
127.0.0.1:6379(TX)> get name 
QUEUED
127.0.0.1:6379(TX)> exec
ERR value is not an integer or out of range
OK
zy
```

### 4.2 乐观锁 

> 	乐观锁：乐观锁在操作数据时非常乐观，认为别人不会同时修改数据。. 因此乐观锁不会上锁，只是在执行更新的时候判断一下在此期间别人是否修改了数据：如果别人修改了数据则放弃操作，否则执行操作。 	
>
>悲观锁：悲观锁在操作数据时比较悲观，认为别人会同时修改数据。. 因此操作数据时直接把数据锁住，直到操作完成后才会释放锁；上锁期间其他人不能修改数据 。

* watch 命令用于监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断 
* unwatch 命令用于取消 watch 命令对所有 key 的监视。 
```redis
# 一个终端操作一个数据，事务不会中断
127.0.0.1:6379> hset info:1 money 100
1
127.0.0.1:6379> watch info:1
OK
127.0.0.1:6379> multi
OK
127.0.0.1:6379(TX)> hincrby info:1 money -10
QUEUED
127.0.0.1:6379(TX)> exec
90

# 多个终端同时操作操作同一个数据，事务会中断
# terminal-1
127.0.0.1:6379> hset info:1 money 100
1
127.0.0.1:6379> watch info:1      # 监控 info:1 这个key
OK
127.0.0.1:6379> multi         # 开启事务  
OK
127.0.0.1:6379(TX)> hincrby info:1 money -10   # 此时另一个终端也修改这个key值  
QUEUED
127.0.0.1:6379(TX)> exec     # 执行事务, 此时事务被中断

# -------------------------------------------------
# terminal-2
127.0.0.1:6379> hincrby info:1 money 10
110

# 如果事务执行失败, 就先解锁
# 获取最新的值，再次监控，执行事务
127.0.0.1:6379> unwatch
OK
127.0.0.1:6379> watch info:1
OK
127.0.0.1:6379> multi
OK
127.0.0.1:6379(TX)> hincrby info:1 money -10
QUEUED
127.0.0.1:6379(TX)> exec
100
```
## 5.Redis持久化
* redis是内存数据库, 如果不将内存中的数据库保存到磁盘，某天服务器宕机了服务器中的数据库状态也会消失；所以redis提供了持久化功能。

### 5.1 持久化之RDB
* redis 会单独创建(fork)一个子进程来进行持久化，会先将数据写入到一个临时文件中，待持久化过程都结束了，再用这个临时文件替换上次持久化好的文件，整个过程中主进程是不进行IO操作的

**触发机制:**

  1. save的规则满足的情况下，会自动触发rdb规则
  2. 执行flushall命令，也会触发rdb规则
  3. 退出redis，也会生成rdb文件 (备份就自动生成一个dump.rdb文件，生产环境需要备份这个文件)

**如何恢复reb文件:**
只需要讲rdb文件放在redis.conf文件的dir配置目录(查看命令:`config get dir`)就可以了，redis启动的时候会自动检查dump.rdb恢复其中的数据

**优点:** 1. 适合大规模的数据恢复, 对数据的完整性要求不高
**缺点:** 1. 需要一定的时间间隔进行操作，如果redis意外宕机了，最后一次修改的数据就没有了 2. fork进程的时候，会占用一定的内存空间

### 5.2 持久化之AOF
* 将所有命令全部记录下来， history ,  恢复的时候就把这个文件礼里边的命令全部执行一遍
* 以日志的形式来记录每个写操作, 将redis执行过的所有命令记录下来, 只许追加文件但不可以修改文件，redis启动时会读取文件重新构建数据

AOF默认是不开启的, 配置项`appendonly no` 改为 yes 即可

**触发机制和恢复aof文件一样**

注意: 如果aof文件有错误或者被破坏， 这时候redis 是无法正常启动的. 

redis提供了一个工具`redis-check-aof --fix aof文件 ` 如果文件正常，重启redis就可以直接恢复了

**优点:** 1.每一次修改都会同步, 文件的完整会更加好 2. 每秒同步一次，可能会丢失一秒的数据，从不同步，效率最高的

**缺点:** 1. 相对于数据文件来说, aof 远远大于rdb, 修复的速度也比rdb慢 2. aof 运行效率要比rdb慢，所以redis 默认的配置就是rdb持久化###

## 6. Redis发布订阅

 Redis 发布订阅 (pub/sub) 是一种消息通信模式：发送者 (pub) 发送消息，订阅者 (sub) 接收消息 

**发布订阅命令:**

		1.   `Psubscribe` 命令订阅一个或多个符合给定模式的频道 
  		2.   `Pubsub` 命令用于查看订阅与发布系统状态，它由数个不同格式的子命令组成 
                		3.   `Publish` 命令用于将信息发送到指定的频道 
            		4.    `Punsubscribe` 命令用于退订所有给定模式的频道。 这个命令在不同的客户端中有不同的表现。  
                      		5.   `Subscribe` 命令用于订阅给定的一个或多个频道的信息 
                              		6.    `Unsubscribe` 命令用于退订给定的一个或多个频道的信息 

```redis
# terminal1-订阅端
127.0.0.1:6379> subscribe channel1      # 订阅一个 channel 频道
subscribe
channel1
1
# 等待推送消息
message       # 消息 
channel1      # 哪个频道的消息
I dont`t care!     # 消息的具体内容

# terminal2-订阅端
127.0.0.1:6379> publish channel1 'I dont`t care!' # 发布者发布消息到channel1 频道
1
```

## 7. 主从复制

> 主从复制是指将一台redis 服务器的数据复制到其它的redis 服务器；前者称为主节点(master/leader), 后者称为从节点(slave/fllower)。
>
> **数据的复制是单向的, 只能由主节点到从节点。master以写为主，slave以读为主。**
>
> 默认情况下，每台redis服务器都是主节点，一个主节点可以有多个从节点(或没有从节点), 但是一个从节点只能由一个主节点

**主从复制的作用主要包括:**

1. 数据冗余：主从复制实现了数据的热备份，是持久化之外的一种数据冗余方式。
2. 故障恢复：当主节点出现问题时，可以由从节点提供服务，实现快速的故障恢复；实际上是一种服务的冗余。
3. 负载均衡：在主从复制的基础上，配合读写分离，可以由主节点提供写服务，由从节点提供读服务（即写Rdis数据时应用连接
   主节点，读Rdis数据时应用连接从节点），分担服务器负载；尤其是在写少读多的场景下，通过多个从节点分担读负载，可以大
   大提高Redis服务器的并发量。
4. 高可用(集群)基石：除了上述作用以外，主从复制还是哨兵和集群能够实施的基础，因此说主从复制是Rds高可用的基础。

一般来说，要将Redis运用于工程项目中，只使用一台Redis是万万不能的（宕机），原因如下：

1. 从结构上，单个Redis服务器会发生单点故障，并且一台服务器需要处理所有的请求负载，压力较大
2. 从容量上，单个Redis服务器内存容量有限，就算一台Redis服务器内存容量为256G,也不能将所有内存用作Redis存储内存，
   一般单台Redisi最大使用内存不应该超过20G(电商网站上的商品，一般都是一次上传，无数次浏览的，说专业点也就是"多读少写”)

### 环境配置

* 只需要配置从节点

```redis
# 端口号
port 6379

# pid 程件文件名称
pidfile /var/run/redis/redis-server.pid

# log文件名称
logfile /var/log/redis/redis-server.log

# dump.rdb 文件名称
dbfilename dump.rdb


# eg:+++++++++++++++++++++++++++++++++++++
#redis-6379.conf
port 6379
daemonize yes
logfile "6379.log"
dbfilename "dump-6379.rdb"

#redis-6380.conf
port 6380
daemonize yes
logfile "6380.log"
dbfilename "dump-6380.rdb"
slaveof 192.168.92.128 6379

#redis-6381.conf
port 6381
daemonize yes
logfile "6381.log"
dbfilename "dump-6381.rdb"
slaveof 192.168.92.128 6379
```

### 7.1 一主二从

* 默认情况下每个节点都是主机

```redis
# 临时配置(命令行配置)
# 主节点查看配置
127.0.0.1:6379> info replication
# 从节点配置
127.0.0.1:6379> slaveof 主节点ip 主节点端口

# 永久配置修改redis.conf配置文件
# replicaof <masterip> <masterport>
# masterauth <master-password>
```

**主机可以写，从机不能写只能读取主机的数据！主机中的所有信息和数据都会被从机保存**

1. 主机宕机了，从机依旧是连接到主机的但是没有写操作，如果主机重新启动了, 从机依旧可以直接获取到主机写的数据
2. 如果是使用命令行配置的主从设备，这个时候重启了就会变成主机。只要变为从机，立马就会从主机中获取到值

**同步原理:**

Slave启动成功连接到master后会发送一个sync同步命令
Master接到命令，启动后台的存盘进程，同时收集所有接收到的用于修改数据集命令，在后台进程执行完毕之后，master将传送
整个数据文件到slave,并完成一次完全同步。
全量复制：而slve服务在接收到数据库文件数据后，将其存盘并加载到内存中。
增量复制：Master继续将新的所有收集到的修改命令依次传给slave,完成同步
但是只要是重新连接master,一次完全同步（全量复制）将被自动执行！我们的数据一定可以在从机中看到！

### 7.2 层层链路

* 主机下面挂了一台从机1，从机1下面挂了一台从机2（master --> salve1 --> slave2）

如果主机断开了连接，我们可以使用手动使用命令`slaveof no  one`让自己变成主机

### 7.3 哨兵模式(重点)

一主二从三哨兵集群，当master节点宕机时，通过哨兵(sentinel)重新推选出新的master节点，保证集群的可用性。

**原理:** 哨兵是一个独立的进程，独立运行； 哨兵通过发送命令，等待redis服务器响应从而监控运行多个redis实例

**哨兵的主要功能:**
1.集群监控：负责监控 Redis master 和 slave 进程是否正常工作。
2.消息通知：如果某个 Redis 实例有故障，那么哨兵负责发送消息作为报警通知给管理员。
3.故障转移：如果 master node 挂掉了，会自动转移到 slave node 上。
4.配置中心：如果故障转移发生了，通知 client 客户端新的 master 地址。
根据推举机制，集群中哨兵数量最好为奇数(3、5…)

哨兵用于实现 redis 集群的高可用，本身也是分布式的，作为一个哨兵集群去运行，互相协同工作。
故障转移时，判断一个 master node 是否宕机了，需要大部分的哨兵都同意才行，涉及到了分布式选举的问题。
即使部分哨兵节点挂掉了，哨兵集群还是能正常工作的，因为如果一个作为高可用机制重要组成部分的故障转移系统本身是单点的，那就很坑爹了。

**哨兵配置文件:**

```redis
# 配置文件sentinel.conf

# sentinel monitor 被监控的名称  主机  端口 数字2代表,主节点挂了slave投票看谁接替为主节点，票数最多的就称为主节点
sentinel monitor mymaster 127.0.0.1 6379 2   # 核心配置，还有其它的配置     
```

如果原来宕机的redis主机正常启动了，只能归并到新的主机下当做从机，这就是哨兵模式的规则！

**优点:**

1. 哨兵集群基于主从复制模式，所有的主从配置优点它都有
2. 主从节点可以切换，故障可以转移系统的可用性更好
3. 哨兵模式就是主从模式的升级，手动到自动更加健壮

**缺点:**

1. redis 不好在线扩容，集群容量一旦到达上限，在线扩容十分麻烦
2. 实现哨兵模式的配置很麻烦

**哨兵模式全部配置:**

```redis
# 哨兵sentinel实例运行的端口，默认26379  
port 26379

# 哨兵sentinel的工作目录
dir /tmp

# 是否开启保护模式，默认开启。
protected-mode no

# 是否设置为后台启动。
daemonize yes

# 哨兵sentinel的日志文件
logfile ./sentinel.log

# 哨兵sentinel监控的redis主节点的 
# ip: 主机ip地址
# port: 哨兵端口号
# master-name: 可以自己命名的主节点名字
# quorum: 当这些quorum个数sentinel哨兵认为master主节点失联 那么这时客观上认为主节点失联了  
# sentinel monitor <master-name> <ip> <redis-port> <quorum>  
sentinel monitor mymaster 127.0.0.1 6379 2

# 当在Redis实例中开启了requirepass，所有连接Redis实例的客户端都要提供密码。
# sentinel auth-pass <master-name> <password>  
sentinel auth-pass mymaster 123456  

# 指定主节点应答哨兵sentinel的最大时间间隔，超过这个时间，哨兵主观上认为主节点下线，默认30秒  
# sentinel down-after-milliseconds <master-name> <milliseconds>
sentinel down-after-milliseconds mymaster 30000  

# 指定了在发生failover主备切换时，最多可以有多少个slave同时对新的master进行同步。
# 这个数字越小，完成failover所需的时间就越长；反之，但是如果这个数字越大，就意味着
# 越多的slave因为replication而不可用。可以通过将这个值设为1，来保证每次只有一个slave 处于不能处理命令请求的状态。
# sentinel parallel-syncs <master-name> <numslaves>
sentinel parallel-syncs mymaster 1  

# 故障转移的超时时间failover-timeout，默认三分钟，可以用在以下这些方面：
# 1. 同一个sentinel对同一个master两次failover之间的间隔时间。  
# 2. 当一个slave从一个错误的master那里同步数据时开始，直到slave被纠正为从正确的master那里同步数据时结束。  
# 3. 当想要取消一个正在进行的failover时所需要的时间。
# 4. 当进行failover时，配置所有slaves指向新的master所需的最大时间。不过，即使过了这个超时,
# slaves依然会被正确配置为指向master，但是就不按parallel-syncs所配置的规则来同步数据了
# sentinel failover-timeout <master-name> <milliseconds>  
sentinel failover-timeout mymaster 180000

# 当sentinel有任何警告级别的事件发生时（比如说redis实例的主观失效和客观失效等等），
# 将会去调用这个脚本。一个脚本的最大执行时间为60s，如果超过这个时间，脚本将会被一个SIGKILL信号终止，之后重新执行。
# 对于脚本的运行结果有以下规则：  
# 	1. 若脚本执行后返回1，那么该脚本稍后将会被再次执行，重复次数目前默认为10。
#	2. 若脚本执行后返回2，或者比2更高的一个返回值，脚本将不会重复执行。  
#	3. 如果脚本在执行过程中由于收到系统中断信号被终止了，则同返回值为1时的行为相同。
# sentinel notification-script <master-name> <script-path>  
sentinel notification-script mymaster /var/redis/notify.sh

# 这个脚本应该是通用的，能被多次调用，不是针对性的。
# sentinel client-reconfig-script <master-name> <script-path>
sentinel client-reconfig-script mymaster /var/redis/reconfig.sh
```

## 8. 缓存穿透/雪崩

### 缓存穿透

>缓存穿透的概念很简单，用户想要查询一个数据，发现dis内存数据库没有，也就是缓存没有命中，于是向持久层数据库查询。发
>现也没有，于是本次查询失败。当用户很多的时候，缓存都没有命中(秒杀！)，于是都去请求了持久层数据库。这会给持久层数
>据库造成很大的压力，这时候就相当于出现了缓存穿透

**解决方案:**

1. 【布隆过滤器】：布隆过滤器是一种数据结构，对所有可能查询的参数以hsh形式存储，在控制层先进行校验，不符合则丢弃，从而避免了对底层存
   储系统的查询压力；

   但是这种方法会存在两个问题：
   1）如果空值能够被缓存起来，这就意味着缓存需要更多的空间存储更多的键，因为这当中可能会有很多的空值的键；
   2）即使对空值设置了过期时间，还是会存在缓存层和存储层的数据会有一段时间窗口的不一致，这对于需要保持一致性的业务会
   有影响。

### 缓存击穿

>这里需要注意和缓存击穿的区别，缓存击穿，是指一个ky非常热点，在不停的扛着大并发，大并发集中对这一个点进行访问，当
>这个ky在失效的瞬间，持续的大并发就穿破缓存，直接请求数据库，就像在一个屏障上凿开了一个洞。
>当某个ky在过期的瞬间，有大量的请求并发访问，这类数据一般是热点数据，由于缓存过期，会同时访问数据库来查询最新数
>据，并且回写缓存，会导使数据库瞬间压力过大。

**解决方案:**

1. 【设置热点数据永不过期】： 从缓存层面来看，没有设置过期时间，所以不会出现热点ky过期后产生的问题。
2. 【加互斥锁分布式锁】：使用分布式锁，保证对于每个ky同时只有一个线程去查询后端服务，其他线程没有获得分布式锁的权限，因此只需要
   等待即可。这种方式将高并发的压力转移窄到了分布式锁，因此对分布式锁的考验很大。

### 缓存雪崩

>缓存雪崩，是指在某一个时间段，缓存集中过期失效。 
>产生雪崩的原因之一，比如在写本文的时候，马上就要到双十二零点，很快就会迎来一波抢购，这波商品时间比较集中的放入了缓
>存，假设缓存一个小时。那么到了凌晨一点钟的时候，这批商品的缓存就都过期了。而对这批商品的访问查询，都落到了数据库
>上，对于数据库而言，就会产生周期性的压力波峰。于是所有的请求都会达到存储层，存储层的调用量会暴增，造成存储层也会挂
>掉的情况。其实集中过期，倒不是非常致命，比较致命的缓存雪崩，是缓存服务器某个节点宕机或断网。因为自然形成的缓存雪崩，
>一定是在某个时间段集中创建缓存，这个时候，数据库也是可以顶住压力的。无非就是对数据库产生周期性的压力而已。而缓存服务节点的
>宕机，对数据库服务器造成的压力是不可预知的，很有可能瞬间就把数据库压垮。

**解决方案:**

1. 【redisi高可用】：这个思想的含义是，既然redis有可能挂掉，那我多增设几台res,这样一台挂掉之后其他的还可以继续工作，其实就是搭建的集
   群。
2. 【限流降级】：这个解决方案的思想是，在缓存失效后，通过加锁或者队列来控制读数据库写缓存的线程数量。比如对某个ky只允许一个线程查
   询数据和写缓存，其他线程等待
3. 【数据预热】：数据加热的含义就是在正式部署之前，我先把可能的数据先预先访问一遍，这样部分可能大量访问的数据就会加载到缓存中。在即
   将发生大并发访问前手动触发加载缓存不同的ky,设置不同的过期时间，让缓存失效的时间点尽量均匀。

## 9. Python 操作redis

```python
# 方式1
import redis

r = redis.Redis(host='127.0.0.1', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))


# 方式2
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('bar', 'Foo')
print(r.get('bar'))

# 通常情况下, 当我们需要做redis操作时会创建一个连接, 并基于这个连接进行redis操作, 操作完成后释放连接,一般情况下这是没问题的, 
# 但当并发量比较高的时候, 频繁的连接创建和释放对性能会有较高的影响。于是, 连接池就发挥作用了。
# 连接池的原理是, 通过预先创建多个连接, 当进行redis操作时直接获取已经创建的连接进行操作, 而且操作完成后不会释放, 用于后续的其他redis操作。
# 这样就达到了避免频繁的redis连接创建和释放的目的, 从而提高性能。


# ==============================================================================================
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# （1）字符串操作：不允许对已经存在的键设置值
ret = r.setnx("name", "yuan")
print(ret)  # False
# （2）字符串操作：设置键有效期
r.setex("good_1001", 10, "2")
# （3）字符串操作：自增自减
r.set("age", 20)
r.incrby("age", 2)
print(r.get("age"))  # b'22'

# （4）hash操作：设置hash
r.hset("info", "name", "rain")
print(r.hget("info", "name"))  # b'rain'
r.hset("info", "gender", "male", {"age": 22})
print(r.hgetall("info"))  # {b'name': b'rain', b'gender': b'male', b'age': b'22'}

# （5）list操作：设置list
r.rpush("scores", "100", "90", "80")
r.rpush("scores", "70")
r.lpush("scores", "120")
print(r.lrange("scores", 0, -1))  # ['120', '100', '90', '80', '70']
r.linsert("scores", "AFTER", "100", 95)
print(r.lrange("scores", 0, -1))  # ['120', '100', '95', '90', '80', '70']
print(r.lpop("scores"))  # 120
print(r.rpop("scores"))  # 70
print(r.lindex("scores", 1)) # '95'

# （6）集合操作
# key对应的集合中添加元素
r.sadd("name_set", "zhangsan", "lisi", "wangwu")
# 获取key对应的集合的所有成员
print(r.smembers("name_set"))  # {'lisi', 'zhangsan', 'wangwu'}
# 从key对应的集合中随机获取 numbers 个元素
print(r.srandmember("name_set", 2))
r.srem("name_set", "lisi")
print(r.smembers("name_set"))  # {'wangwu', 'zhangsan'}

# （7）有序集合操作
# 在key对应的有序集合中添加元素
r.zadd("jifenbang", {"yuan": 78, "rain": 20, "alvin": 89, "eric": 45})
# 按照索引范围获取key对应的有序集合的元素
# zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)
print(r.zrange("jifenbang", 0, -1))  # ['rain', 'eric', 'yuan', 'alvin']
print(r.zrange("jifenbang", 0, -1, withscores=True))  # ['rain', 'eric', 'yuan', 'alvin']
print(r.zrevrange("jifenbang", 0, -1, withscores=True))  # ['rain', 'eric', 'yuan', 'alvin']

print(r.zrangebyscore("jifenbang", 0, 100))
print(r.zrangebyscore("jifenbang", 0, 100, start=0, num=1))

# 删除key对应的有序集合中值是values的成员
print(r.zrem("jifenbang", "yuan"))  # 删除成功返回1
print(r.zrange("jifenbang", 0, -1))  # ['rain', 'eric', 'alvin']

# （8）键操作
r.delete("scores")
print(r.exists("scores"))
print(r.keys("*"))
r.expire("name",10)
```

