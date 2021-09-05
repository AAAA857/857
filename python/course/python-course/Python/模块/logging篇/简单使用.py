import  logging


'''   
logger 提供应用程序可以直接调用的接口
handler 提供将日志输入到的地方
filter  用于过滤某些日志信息
formatter 给予日志一个标准的输出格式
'''

''' 简单使用logging '''
# logging.info("info")
# logging.debug("debug")
# logging.error("error")
# logging.warning("warning")
# logging.basicConfig(filename="info.txt", level=logging.INFO)
# logging.info("123")
# logging.error("error")
# logging.debug("debug")
# logging.warning("warning")
#

''' 日志格式配置  format '''
#
# logging.basicConfig(filename='info.txt',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %l:%M:%S %p')
# logging.info("123")
# logging.warning("wadd")
#


