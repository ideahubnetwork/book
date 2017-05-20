# HTTP 报文

## 3.4 状态码
+ 100 Continue
  > Expect
+ 101 Switching Protocals
  > Update
+ 200 OK
+ 201 Created
+ 202 Accepted
+ 204 No Content
  > HEAD
+ 206 Partial Content
+ 301 Moved Permanently
  > Location
  302 Found
  303 See Other
  304 Not Modified
  307 Tempoary Redirect
  400 Bad Request
  403 Forbidden
  404 Not Found
  405 Method Not Allowed
  406 Not Acceptable
  408 Request Tieout
  500 Internal Server Error
  502 Bad Gateway
  503 Service Unvaliable

## 3.5 首部

+ 通用首部
  + Connection
  + Date
  + Cache-Control
+ 请求首部
  + Accept
  + If-Modified-Since
  + If-Range
  + If-Match
  + Cookie
+ 响应首部
  + Set-Cookie
+ 实体首部
  + Location
  + Content-Type
  + Content-Encoding
  + Content-Length
  + Location
  + ETag
  + Experies
  + Last-Modified
