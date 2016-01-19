## mysql架构
### mysql逻辑架构
第一层：连接服务，授权认证，安全
第二层：查询解析，分析优化，缓存，内建函数，存储过程，触发器，视图。
第三层：存储和提取所有存放在mysql中的数据。

1. 连接管理与安全性
2. 优化与执行（第四章）

### 并发控制
1. 读锁与写锁
写锁会阻塞其它的读锁和写锁，而读锁是共享资源的。
2. 锁粒度
所策略，载锁开销和安全性能之间寻找一个平衡。
	+ 行级锁
	+ 表锁
3. 事务
ACID特性，Atomicity,Consistency,Isolation,Durability。
	1. 隔离级
		+ READ UNCOMMITTED
		Dirty Read
		+ READ COMMITTED
		用户运行同一语句两次，看到的结果是不同的。
		+ REPEATBLE READ
		+ SERIALIZABLE
	2. 死锁
	多个事务以不同的顺序加锁统一资源。
4. 多版本并发控制(MVVC, Multiversion Concurrency Control)
5. 存储引擎
```
SHOW TABLE STATUS LIKE 'user' \G
```
Row Format: 
	Dynamic, Compact, Fixed。
Rows:
	表中的行数。
	1. InnoDB　引擎
	InnoDB适合处理大量短期事务，把所有数据文件存储载表空间内，基于聚簇索引建立。实现所有四个标准隔离级，默认隔离级为REPEATABLE READ，并使用间隙锁防止幻读。
	2. Memory　引擎
	系统重启后不需要保留，快速数据访问性能。用途，查找表和映射表。支持哈希索引。
6. 考虑因素
	+ 事务
	+ 并发
	+ 备份
	+ 崩溃后恢复
	+ 特有特性
7. 表转换
把表从一种存储引擎转换到另一种存储引擎。
	+ Alter Table
	耗费大量时间，原表要加锁，进行逐行复制，不适合对繁忙的表进行操作。
	+ Dump　和 Import
	先转储为一个文本文件，再从文本文件进行编辑导入
	+ Create 和 Select
	
