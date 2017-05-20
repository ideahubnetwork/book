# web 服务器

## 5.4 接受客户端连接

+ 根据 IP 地址确认客户端
+ 可以随意拒绝任意一条连接，比如恶意客户端
+ RDNS 可以将 IP 地址转化为主机名，但需要耗费时间，一般禁止解析

## 5.5 接收请求报文

+ CRLF 解析出首行，首部
+ 根据 Content-Length 读出 body

## 5.6 处理请求

## 5.7 资源映射

+ nginx root
+ cgi
+ server side include

## 5.8 构建响应

+ 实体
  + Content-Type
    + MIME
      + Magix typing
  + Content-Length

## 5.9 发送相应
## 4.10 记录日志
