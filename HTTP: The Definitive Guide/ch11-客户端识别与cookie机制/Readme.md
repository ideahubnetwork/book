# 客户端识别与客户端机制

## 11.2 HTTP 首部

与用户信息相关的首部
+ From
+ User-Agent
+ Referer
+ Authorization
+ Client-IP
+ X-Forwarded-For
+ Cookie

## 11.4 用户登录

+ Authorization

## 11.5 胖URL

## 11.6 cookie

+ 类型
  + 会话cookie
    > 没有设置 Expires 与 Max-Age 或者 Discard 参数
  + 持久cookie
    > 存储在硬盘上
+ cookie
  + 域名
  + 路径
  + 版本
    + 0
    + 1 (RFC2965)
      + Discard
      + Max-Age
      + port
      + $
  + 缓存
    + Cache-Control: no-cache="Set-Cookie"
    + Cache-Control: public
    + Cache-Control: must-revalidate, max-age=0
