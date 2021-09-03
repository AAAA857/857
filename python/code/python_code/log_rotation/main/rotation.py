import os
import time
import logging.handlers

""" 获取工作路径 """
File_Path = os.path.abspath(os.path.dirname(__file__))

class Log_Cutting(object):

    level_config = {

        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL,

    }

    def __init__(self):

        """:argument

            r_file 表示需要实时读取的日志文件
            r_path 表示需要实时读取的日志位置
            w_file filebeat 需要读取的日志文件
            w_path filebeat 读取的文件路径

        """
        r_file = os.getenv('r_file')
        r_path = os.getenv('r_path')
        w_file = os.getenv('w_file')
        w_path = os.getenv('w_path')
        self.r_file = r_file
        self.r_path = r_path
        self.Log_File = w_file
        self.Log_Path = w_path
        self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.r_path, self.r_file)

        if not os.path.exists(os.path.dirname(os.path.abspath(self.current_path))):

            os.mkdir(os.path.dirname(os.path.abspath(self.current_path)))

        self.logger = logging.getLogger(__file__)
        self.logger.setLevel(self.level_config.get('debug'))

        fh = logging.handlers.RotatingFileHandler(filename=os.path.join(os.path.dirname(os.path.abspath(self.current_path)), w_file),backupCount=5,maxBytes=1024*1024*10)
        self.logger.addHandler(fh)

    """
    1. 实现实时读取日志
    2. 实现日志按照大小进行自动切割
    """

    def Read_Logfile(self):

        if not os.path.exists(self.current_path):

            with open(file=self.current_path,mode='w') as w:

                w.write('')

        with open(file=self.current_path,mode='r') as r :

            """取出文件字符数量"""
            filesize = os.stat(self.current_path)[6]

            r.seek(filesize)

            while True:

                # 获取当前光标位置
                where = r.tell()
                # 每一行文件内容
                line = r.readline()
                # 判断如果改行没有内容将休眠一秒钟，并且将光标移动到最后位置
                if not line:
                    time.sleep(1)
                    r.seek(where)
                else:
                    # 来消息后将会打印文件内容
                    self.Logger(line.strip())

    def Logger(self,data):
        print(data)
        return self.logger.info(data)

if __name__ == '__main__':


    obj = Log_Cutting()

    obj.Read_Logfile()