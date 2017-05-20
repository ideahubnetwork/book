# 连接管理

## 4.1 TCP 连接

### TCP Streams Are Segmented and Shipped by IP Packets.

### Programing with TCP Sockets
+ steps
  + socket
  + bind
  + listen
  + accept
  +
  + read
  + write
  +
  + close

## 4.2 TCP Performace Considerations

### 4.2.2 Performance Focus Areas

+ 三次握手
+ 慢启动拥塞控制
+ Nagle 算法
+ delayed acknowledgment algorithm
+ TIME_WAIT delays and port exhaustion

### 4.2.4 延迟确认

ACK 会随相同方向的数据包一块发送，但是需要找，所以有这么个算法

+ 慢启动
  + 为了避免网络的突然过载和拥塞，所以慢启动。1 2 4 8 16 8
  + [为什么http是一点点下载而不是直接下载](https://www.zhihu.com/question/50349911)
+ Nagle 算法
  + 打包小的数据包

## 4.4 并行连接

大量连接会消耗更多内存资源，通常为4个，过多连接不一定更快。

## 4.5 持久连接

+ Keep-Alive 连接的限制以及规则

+ 持久连接与哑代理(Dumb Proxy)

## 4.6 管道化连接
+ 持久连接
+ 顺序 响应与请求顺序
+ 错误处理
+ 幂等
