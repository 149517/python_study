from multiprocessing import Process


# 自定义进程
class MyProcess(Process):

    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    # 自定义进程需要重写 run方法
    def run(self):
        n = 1
        while True:
            print("{}---进程名称；{}".format(n, self.name))


if __name__ == '__main__':
    p = MyProcess("xiao")
    p.start()
    p1 = MyProcess("hong")
    p1.start()
