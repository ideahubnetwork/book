# 架构优化和索引

优化需要权衡取舍。比如，添加索引会加快读取速度，却会减慢跟新速度。

## 优化数据类型

+ 根据粒度和需要设置合适大小的数据类型
+ 使用内置的日期和时间类型存储日期时间，使用整数存储IP地址
+ 尽量避免NULL，NULL需要更大的存储空间

### 整数

根据实际情况选择有符号和无符号的类型。

int(1) 和 int(11) 是一样的，只不过在交互工具上显示字符的个数不同。

### 实数

`float` 和 `decimal`

### 字符串

+ varchar 和 char

`varchar` 会使用额外的1到2字节去存储值的长度，如 varchar(10) 占用了11个字节，而 varchar(1000) 占用1002个字节。
当最大长度远大于平均长度，并且很少更新的时候，适合使用 `varchar`。

mysql 会保留字符串末尾的空格，但其他 DBMS 不一定。

`char`。长度大致相似且比较短的时候，适合使用 `char` 。

mysql 不会保留字符串末尾的空格，但其他 DBMS 不一定。

+ blob 和 text

`blob` 保存二进制数据，且没有字符集和排序规则。

+ 使用enum代替字符串

使用enum代替字符串具有更好的可读性，并且存储空间较小，而且容易知道允许存储的值有哪些。但正由于此，每当添加字符串时，都需要 alter table。
另外，由于实际存储的是整数，所以不要使用enum来代替整数，另外，也不能按照字符串的顺序来排序。

### 日期和时间类型

`datetime` 占用8字节的存储空间，从1001年到9999年，精度为秒，与时区无关。

`timestamp` 占用4字节的存储空间，保存了自1970年1月1日的秒数。

如果需要保存毫秒数，可以使用 `bigint` 或者 `double`。

## 索引基础知识

### 索引类型

有很多类型的索引，在存储引擎层实现。

+ B-Tree 索引

很多时候，叫 `B-Tree` 索引不一定是 `B-Tree` 索引，有可能是 `B+Tree`，也有可能是 `T-Tree`。

B-Tree 意味着数据存储是有序的，且每个叶子节点到根的距离大致一样（平衡因子较小）。

+ Hash
+ R-Tree
+ Full Text

## 高性能索引策略

### 隔离列

对于查找的列，不能成为表达式的一部分也不能位于函数中，更好地利用缓存。

``` sql
# 位于表达式中
select id from student where id + 1 = 5;
```

### 前缀索引

创建索引会耗费空间，当索引的字符串特别长的时候，为了空间上性能的提高，可以只索引前缀。

Index Selecitivity (索引选择性) 指不重复的索引值与行数的比，索引选择性越高，性能越好。

### 聚集索引

### 覆盖索引

直接在索引中获取检索数据，而不用去读数据库，减少IO。

当发起 `Index-covered Query` 时，解释器的 Extra 字段为 `Using Index`。

``` sql
explain select id from student;
```

> type 和 extra 列的 index 毫无关系

### 为排序使用索引扫描

mysql 有两种排序的方式，文件排序(Filesort)和扫描索引。

### 压缩索引

### 多余和重复索引

> 如果类型要求不同，则忽略。如 kye 和 fulltext key。

在 (A, B) 上有索引，如果再在 (A) 上建立索引则是一种浪费。因为 (A, B) 是 (A) 的最左前缀。

## 索引实例研究

### 优化排序

可以为以下 sql 添加 (sex, score) 索引

``` sql
select id, name from student where sex = 'male' order by score limit 10;
```

但是以下高偏移量将会话费时间扫描将要丢掉的数据，可以使用 `Denormalizing`，`Precomputing` 和 `Cache` 来解决问题。

``` sql
select id, name from student where sex = 'male' order by score limit 10000, 10;
```

另外，可以先提取需要的行的主键，然后连接。

``` sql
select id, name from student s inner join (
  select id from student where x.sex = 'male' order by score limit 10000, 10
) as x on x.id = s.id;
```

## 正则化和非正则化

### 正则化的利弊

正则化的表一般都满足第二范式

利
+ 无冗余数据
+ 更新快
+ 改动快

弊
+ 查询时需要建立联接

### 非正则化的利弊

非正则化不需要联接表，即使在最坏的情况下，全表扫描也要比联接快很多，因为它避免了随机IO。

### 结合正则化和非正则化

部分非正则，缓存，汇总，触发器
