import  logging

"""
Handler 是真真正执行输出的模块，负责将指定的messages 发送到指定的输出介质内:

常用的Handler输出介质有如下:
logging.StreamHandler                       将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象
logging.FileHandler                         将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
logging.handlers.RotatingFileHandler        将日志消息发送到磁盘文件，并支持日志文件按大小切割
logging.hanlders.TimedRotatingFileHandler   将日志消息发送到磁盘文件，并支持日志文件按时间切割
logging.handlers.HTTPHandler                将日志消息以GET或POST的方式发送给一个HTTP服务器
logging.handlers.SMTPHandler                将日志消息发送给一个指定的email地址

"""