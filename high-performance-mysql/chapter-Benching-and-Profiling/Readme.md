## 性能分析

### MySQL 分析

+ 一般在mysql分析中需要获取以下数据
  + 访问最多的数据
  + 执行时间最长的查询种类
  + 停留时间最长的状态
  + 执行查询的使用最频繁的子系统
  + 查询过程中访问的数据种类
  + 执行了多少种不同类型的活动

+ 记录查询

`mysql` 有两种查询日志，普通日志(general log)和慢速日志(slow log)。慢速日志记录了执行时间比较长或者没有使用索引的查询。

log-slow-queries = :file
long_query_time = 2
log-queries-not-using-indexes

+ 精细控制日志

mysql5.0 中，long_query_time 的最小值是1s。在mysql5.7中可以是ms级。

https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html

### show status

可以结合使用 `flush status` 和 `show session status` 优化查询。

在查询上添加 `sql_no_cache`，mysql不会从查询缓存中获取结果。

> 需要 root 权限

### show profile

开启分析

```
set profiling = 1;
```
