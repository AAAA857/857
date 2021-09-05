import subprocess as sp
from  logger import  Logger
import os

dir = os.path.dirname(os.path.realpath(__file__))

class Command(object):

    def __init__(self,file):

        self.file = file
        self.log = Logger(self.file,"INFO")

    def run_with_env(self, args, executable_type=None):

        """
        封装subprocess.Popen，使用/bin/bash进行执行
        :param args: 命令行或数组
        :param if_shell: 是否是命令行  True
        :param executable_type:默认传None,ubuntu下需要/bin/bash
        :param shell: 接收字符串类型的命令进行执行
        :param check: 接收命令执行错误返回的一个错误状态 "sp.CalledProcessError"
        :return:shell命令结果
        """
        self.log.info('subprocess start,cmd : %s' % args)
        try:
            command_line_process = sp.Popen(args,executable_type,shell=True,stdout=sp.PIPE, stderr=sp.STDOUT,)
            stdout, stderr = command_line_process.communicate()
            a = command_line_process.returncode

            if not a == "":
                self.log.info("action cmd %s" %args)

        except (OSError, sp.CalledProcessError) as exception:
            self.log.error('subprocess failed,exception occurred: ' + str(exception), exec_info=True)
            return False, None

        self.log.info('subprocess finished,cmd : %s' % args)

        return stdout

    def run(self,args, if_shell=None, executable_type=None):

        output = self.run_with_env(args,executable_type)

        return output

    def shell_command(self,cmd):
        print(cmd)
        res = self.run(cmd)

        return res


    def Scp(self,cmd):

        res = self.run(cmd)

        return res



    def Check(self,cmd,If_timeout=2):

        Status = ""

        try:
            '''
            :param stderr=sp.DEVNULL: 表示不输入执行的内容，直需要一个结果
            '''
            self.log.info("Start Check Directory: %s"%cmd)
            sp.check_output(cmd,shell=True, timeout=If_timeout)

            Status = "True"
            self.log.info("Check Directory Status: %s" % Status)
            return  Status

        except Exception as  E:

            print(E)

            Status = "False"
            self.log.error("Check Directory Status: %s" % Status)
            return Status





if __name__ == '__main__':

    obj = Command(os.path.join(dir, "log", "command.log"))

    print(obj.Check("ls /"))





