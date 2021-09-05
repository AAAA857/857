import os
import logging


'''获取绝对路径'''
dir = os.path.dirname(os.path.realpath(__file__))
class Logger(object):

    def __init__(self,log_file,log_level):
        # 创建出一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 输出到文件
        fh = logging.FileHandler(log_file)
        fh.setLevel(log_level)
        # 输出到屏幕
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        # 日志输出格式
        log_format = logging.Formatter('%(asctime)s - %(process)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(log_format)
        fh.setFormatter(log_format)
        # 添加事件
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):

        self.logger.debug(message)

    def error(self, message):

        self.logger.error(message)




