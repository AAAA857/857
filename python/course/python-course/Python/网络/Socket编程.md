# Socket编程

## 架构类型:

```python
1.C/S架构
  C = client 端
  S = Server 端
  
2.B/S架构
  B = brock 浏览器
  S = Server 服务端


```

## OSI模型:

```python
计算机系统是由 硬件、操作系统、应用软件组成

OSI七层模型:

应用层
表示层
会话层

传输层:
  定义TCP/UDP协议层及端口
  
网络层: 
  IP协议标识局域网络

数据链路层: 
  负责把数据包进行分组（电信号），使用的以太网协议（Ethernet）
  其中包含数据报头信息等（MAC地址信息）
  
物理层: 
  物理链接介质（网线、光缆）,发送电信号

```

## Socket层:

```python
"Socket 运行在传输层与应用层之间"

应用层：
   跑着应用软件，应用层如果要I/O数据则需要一层Socket
socket:
   "Socket 就是TCP/UDP与IP协议的一种封装"，只需要按照socket编程规范就可以进行网络编程
   给应用软件定义一个IP:Port

PID：
  是同一台机器上面的"进程"或"线程"的唯一表示符号

```

