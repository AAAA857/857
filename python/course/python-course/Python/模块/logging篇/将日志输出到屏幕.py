import  logging

# 设置日志输出到终端
ch = logging.StreamHandler()

# 设置日志级别
# ch.setLevel(level='INFO')

# 给日志设置一个标准记录格式
f = logging.Formatter('%(levelname)s - %(asctime)s - %(name)s - %(message)s')

# 给ch 绑定一个日志格式
ch.setFormatter(f)

# 创建一个程序可调用的日志接口
logger = logging.getLogger(__file__)

# 给日志接口设置一个日志级别
logger.setLevel(logging.DEBUG)

# 给接口绑定一个事件输出到屏幕
logger.addHandler(ch)

# 调用接口
logger.error('error')
logger.info('info')
logger.warning('warning')

