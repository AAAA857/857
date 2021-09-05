import logging


class IgnoreBackupFilter(logging.Filter):

    def filter(self, record):       # 固定语法
        """
        定义日志只输出A开头的信息
        """
        if record.getMessage().startswith("A"):
            # True 将返回信息
            return  True
        # False 不会返回信息
        return False

# 定义一个handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义一个format
f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(f)

# 初始化一个logger接口
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)
logger.addFilter(IgnoreBackupFilter())

logger.info("Abc")


