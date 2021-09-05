import threading
import time


class My_Threading(threading.Thread):


    def __init__(self):

        self.Enent = threading.Event()

    def run(self):

        print("星期天要补课")
        self.Enent.set()
        time.sleep(3)
        print()



