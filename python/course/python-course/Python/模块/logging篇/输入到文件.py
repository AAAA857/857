import logging

# 创建一个日志输出handler
fh = logging.FileHandler(filename='file.txt')
# 初始化一个日志输出格式
ft = logging.Formatter('%(levelname)s - %(message)s - %(asctime)s - %(name)s')
# 给handler绑定格式
fh.setFormatter(ft)


# 创建一个程序调用接口
logger = logging.getLogger(__file__)

# 设置日志输出级别
logger.setLevel(logging.INFO)

# 给接口设置一个handler
logger.addHandler(fh)

logger.info('info')
logger.error('error')
logger.warning('warning')