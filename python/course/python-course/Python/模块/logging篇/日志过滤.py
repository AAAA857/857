import logging
'''
1. 将标准信息打印到终端
2. 将error 日志过滤出来输出到日志
'''
class IgnoreBackupFilter(logging.Filter):

    def filter(self, record):

        return "error" not in record.getMessage()

        # if "error" in record.getMessage():
        #
        #     logger.addHandler(fh)

''' 设置日志输出格式 '''
fm = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
''' 创建一个handler '''
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='1.txt')

'''handler绑定日志输出格式'''
ch.setFormatter(fm)
fh.setFormatter(fm)


'''创建一个日志调用接口'''
logger = logging.getLogger(__name__)

'''设置默认日志级别'''
logger.setLevel(logging.DEBUG)

'''设置接口输出路径'''
logger.addHandler(ch)

'''绑定filter实际'''
logger.addFilter(IgnoreBackupFilter())
logger.info('error')
