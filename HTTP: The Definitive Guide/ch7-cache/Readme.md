# 缓存

## 7.1 冗余的数据传输
## 7.2 带宽瓶颈
## 7.3 Flash Crowds
## 7.4 距离时延
## 7.5

+ cache hit
+ cache miss
+ cache hit rate
+ byte hit rate

## 7.6 缓存的拓扑结构

+ private cache
  + Chrome: chrome://cache/
+ public cache
+ hierarchy
  + 一级缓存
  + 二级缓存
  + 三级缓存
+ cache mesh
+ content router
+ sibling cache


## 7.7 缓存的处理步骤

1. 接收
2. 解析
3. 查询
  + 保存缓存的同时也会保留元数据，比如放了多行时间，被用了多少次
4. 新鲜度检测
5. 创建响应
6. 发送
7. 日志


## 7.8 保持副本的新鲜

+ 新鲜度
  + Cache-Control
  + Experies
+ 再验证
  + If-Modified-Since:<date>
    + IMS
      + true: 返回文档与新的过期时间
      + false: 304 只返回 headers
  + If-None-Match:<tags>
    + 如果修改了一些不重要的修改
    + Entity Tag
