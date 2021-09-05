import os
import time
import sys

if len(sys.argv) != 2:

    print('>>sys.stderr,"请输入需要读取的文件名！"')

filename = sys.argv[1]

if not os.path.isfile(filename):
  print('>>sys.stderr,"请给出需要的文件：\%s\: is not a file" % filename')

"""
实现持续读取某一个文件内容
"""
filename = os.path.abspath(__file__)
print(filename)

with open(filename,'r') as f:
    # 获取文件内字符数量
    filesize = os.stat(filename)[6]
    # 移动光标到指定位置,从最后开始读取
    f.seek(filesize)
    while True:
        # 获取当前光标位置
        where = f.tell()
        # 每一行文件内容
        line = f.readline()
        # 判断如果改行没有内容将休眠一秒钟，并且将光标移动到最后位置
        if not line:
            time.sleep(1)
            f.seek(where)
        else:
            # 来消息后将会打印文件内容
            print(line)
