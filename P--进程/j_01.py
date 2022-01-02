from multiprocessing import Process
from time import sleep
import os

m = 0


    # def task1():
    #     while True:
    #         sleep(2)
    #         print("task___1")
    # 使用参数
def task1(s):
    global m
    while True:
        m+=1
        sleep(s)
        print("____task1  #############"+str(m))
            # print(os.getppid())  # 打印当前进程号



def task2():
    global m
    while True:
        m += 1
        sleep(1)
        print("task____2  #############"+str(m))
            # print(os.getppid())

num = 0
if __name__ == "__main__":
        # 第一个子进程
        # p = Process(target=task1, name="任务1")

    p = Process(target=task1,name="任务1",args=(0.5,))
        # args 代表传递的参数，为可迭代对象，需要添加括号， 也可以传递多个，使用多个变量接收
    p.start()
        # 主进程
    print(p.name + "__")
        # print(os.getppid())

        # 第二个子进程
    p1 = Process(target=task2, name="任务2")
    p1.start()
        # 主进程
    print(p1.name)

        # 停止
        # while True:
        #     num += 1
        #     sleep(0.3)
        #     if num == 50:
        #         p.terminate()
        #         p1.terminate()
        #         break
        #     else:
        #         print("-----------------------------" + str(num))
    while True:
        sleep(1)
        m += 1
        print("==================================" + str(m))
    


    print("@@@@@@@@@@@@")