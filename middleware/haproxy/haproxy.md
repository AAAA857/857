# haproxy

简介

```shell
HAProxy 是一款提供高可用性、负载均衡以及基于TCP（第四层）和HTTP（第七层）应用的代理软件，支持虚拟主机，它是免费、快速并且可靠的一种解决方案。 HAProxy特别适用于那些负载特大的web站点，这些站点通常又需要会话保持或七层处理。HAProxy运行在时下的硬件上，完全可以支持数以万计的 并发连接。并且它的运行模式使得它可以很简单安全的整合进您当前的架构中， 同时可以保护你的web服务器不被暴露到网络上。

```

负载均衡类型

```shell
LVS：
1、抗负载能力强。抗负载能力强、性能高，能达到F5硬件的60%；对内存和cpu资源消耗比较低
2、工作在网络4层，通过vrrp协议转发（仅作分发之用），具体的流量由linux内核处理，因此没有流量的产生。
2、稳定性、可靠性好，自身有完美的热备方案；（如：LVS+Keepalived）
3、应用范围比较广，可以对所有应用做负载均衡；
4、不支持正则处理，不能做动静分离。
5、支持负载均衡算法：rr（轮循）、wrr（带权轮循）、lc（最小连接）、wlc（权重最小连接）
6、配置 复杂，对网络依赖比较大，稳定性很高。
 
Ngnix：
1、工作在网络的7层之上，可以针对http应用做一些分流的策略，比如针对域名、目录结构；
2、Nginx对网络的依赖比较小，理论上能ping通就就能进行负载功能；
3、Nginx安装和配置比较简单，测试起来比较方便；
4、也可以承担高的负载压力且稳定，一般能支撑超过1万次的并发；
5、对后端服务器的健康检查，只支持通过端口来检测，不支持通过url来检测。
6、Nginx对请求的异步处理可以帮助节点服务器减轻负载；
7、Nginx仅能支持http、https和Email协议，这样就在适用范围较小。
8、不支持Session的直接保持，但能通过ip_hash来解决。、对Big request header的支持不是很好
9、支持负载均衡算法：Round-robin（轮循）、Weight-round-robin（带权轮循）、Ip-hash（Ip哈希）
10、Nginx还能做Web服务器即Cache功能。

HAProxy的特点是：

1、支持两种代理模式：TCP（四层）和HTTP（七层），支持虚拟主机；
2、能够补充Nginx的一些缺点比如Session的保持，Cookie的引导等工作(每一个会话都有一个cookie实现会话保持)
3、支持url检测后端的服务器出问题的检测会有很好的帮助。
4、更多的负载均衡策略比如：动态加权轮循(Dynamic Round Robin)，加权源地址哈希(Weighted Source Hash)，加权URL哈希和加权参数哈希(Weighted Parameter Hash)已经实现
5、单纯从效率上来讲HAProxy更会比Nginx有更出色的负载均衡速度。
6、HAProxy可以对Mysql进行负载均衡，对后端的DB节点进行检测和负载均衡。
9、支持负载均衡算法：Round-robin（轮循）、Weight-round-robin（带权轮循）、source（原地址保持）、RI（请求URL）、rdp-cookie（根据cookie）
10、不能做Web服务器即Cache。
11、没有web功能仅能做反向代理。
```



会话保持

```shell
cookie支持语法：

   cookie <name> [ rewrite | insert | prefix ] [ indirect ] [ nocache ] [ preserve ]
配置样例:

   backend dynamic_servers
     cookie app_cook  insert  nocache
     server app1      192.168.100.22:80 cookie server1
     server app2      192.168.100.23:80 cookie server2
        
解析:
 
  cookie： 指令
  app_cook: 响应头部中cookie的名字 ，对应的value是 server1 server2
  insert: cookie 下面的一个指令集
  nocache:  受缓存影响
  
  
cookie支持类型:

   insert：   表示在响应首部添加一条cookie ，这个cookie在响应报文的头部将独占一个"Set-Cookie"字段 Set-Cookie:app_cook=server2; path=/
   
   rewrite:  一般不设置这条，当后端服务器设置了cookie时，使用rewrite模式时，haproxy将重写该cookie的值为后端服务器的标识符。
   
   prefix:   haproxy将在已存在的cookie(例如后端应用服务器设置的)上添加前缀cookie值这个前缀部分是server指令中的cookie设置的，代表的是服务端标识符
 
 
 注意:
     
     上面的cookie设置方式不会进行持久化的保存没有maxAge属性，仅仅会保留在web页面缓存中。
```

开启cookie但不进行会话保持

```shell
aproxy允许"即使使用了cookie也不进行会话绑定"的功能。这可以通过ignore-persist指令来实现。当满足该指令的要求时，表示不将该cookie插入到cookie表中，因此无法实现会话保持，即使haproxy设置了cookie也没用。


backend dynamic_group
		acl url_static  path_beg         /static /images /img /css
    acl url_static  path_end         .gif .png .jpg .css .js
    acl url_dynamic   path_end  -i .php   // 表示当请求uri以".php"结尾时，将忽略会话保持功能
    ignore-persist  if url_dynamic
    cookie app_cook insert nocache
    server app1 192.168.100.60:80 cookie app_server1
    server app2 192.168.100.61:80 cookie app_server2
    
    
 TCP协议不支持cookie http支持cookie
```



健康状态检测

```shell
haproxy健康状态检测方式:

1、 基于四层的传输端口做状态监测
2、 基于指定的uri做状态监测
3、 基于指定的URI的resquest请求头部内容做状态监测


基于四层端口检测:
   
   四层传输时可以基于ip或者port做监测，也可以将ip和port监测在后端服务器上的另一个地址和端口用来实现数据通道和监测通道的分离.
   
frontend web
  bind 172.20.27.20:80
  mode tcp
  use_backend web_server
backend web_server
  server web1 192.168.27.21 check addr 192.168.27.21 port 80 inter 3s fall 3 rise 5
  server web2 192.168.27.22 check addr 192.168.27.22 port 80 inter 3s fall 3 rise 5
  
  
  addr:  检测的IP地址
  port:  检测的端口
  inter: 检测间隔时间
  fall:  失败次数
  rise:  检测失败后，多少次成功认为服务可以使用。
  
  
基于uri进行健康状态检测:

   指定uri做状态监测是，在后端服务器上建立一个用户无法访问到的页面，然后再haproxy上对此页面做监测，如果能访问到此页面则表示后端服务器正常.
   
   
frontend web
  bind 172.20.27.20:80
  mode http
  use_backend web_server
  option httpchk GET /monitor-page/index.html HTTP/1.0   #添加需要监测的uri

backend web_server
   server web1 192.168.27.21 check addr 192.168.27.21 port 80 inter 3s fall 3 rise 5
   server web2 192.168.27.22 check addr 192.168.27.22 port 80 inter 3s fall 3 rise 5

注意事项:
    GET的监测方式存在一点问题，如果页面文件很大，页面每隔几面就需要完整的传输一次，这样就造成了不必要的了网络消耗，所以将探测方式改为只查看请求头部内容做状态监测.
    
    
基于url方式进行状态检测:
   基于uri的request请求头部的状态做监测和url做监测类似
   
frontend web
  bind 172.20.27.20:80
  mode http
  use_backend web_server
  option httpchk HEAD /monitor-page/index.html HTTP/1.0   #添加需要监测的uri 指定类型为 HEAD
backend web_server
  server web1 192.168.27.21 check addr 192.168.27.21 port 80 inter 3s fall 3 rise 5
   server web2 192.168.27.22 check addr 192.168.27.22 port 80 inter 3s fall 3 rise 5
   
   
 
```



haproxy 支持的算法

```shell

```





Haproxy 配置文件

```shell
haproxy 配置文件可以分为五部分

global: 全局配置段，配置haproxy启动前进程即系统相关配置
defaults:  配置一些默认参数，如果listen 、frontend、backend 未配置则会使用默认配置
frontend: 用于配置接收客户所请求的域名，uri等
backend: 定义后端服务器集群，cookie等配置在里面。
```



haproxy日志级别

```shell


```





驱动类型

```shell
进程模型:
    1.事件驱动 
    2.单一进程模型，此模型支持非常大的并发连接数
```

![img](https://images2015.cnblogs.com/blog/720333/201609/720333-20160922162036496-1642863922.png)

支持代理模式

```shell
1.tcp
2.http
```

