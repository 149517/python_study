from multiprocessing import Pool
import time
from random import random
import os


# 非阻塞式进程池

# def task(task_name):
#     print("Start the task:", task_name)
#     start = time.time()
#     # sleep
#     time.sleep(random() * 2)
#     end = time.time()
#     print("{},Complete the task, Time use:{}, 进程号: {}".format(task_name, (end - start), os.getpid()))
#
#
# if __name__ == "__main__":
#     pool = Pool(5)
#     tasks = ["吃饭","睡觉","玩游戏","看书","做作业","学习","看视频"]
#     for task1 in tasks:
#         pool.apply_async(task, args=(task1,))
#
#     pool.close()    # 添加任务结束
#     pool.join()     # 堵住主进程
#     # 主进程结束，进程池就会结束。
#
#     print("over!!!")


# 增加回调


def task(task_name):
    print("Start the task:", task_name)
    start = time.time()
    # sleep
    time.sleep(random() * 2)
    end = time.time()
    # print("{},Complete the task, Time use:{}, 进程号: {}".format(task_name, (end - start), os.getpid()))
    return "{},Complete the task, Time use:{}, 进程号: {}".format(task_name, (end - start), os.getpid())


containrt = []

# 将执行之后的返回值储存
def callback_func(n):
    # 接收task 的返回值
    containrt.append(n)
    # 通过回调函数可以使所有任务同时输出，


if __name__ == "__main__":
    pool = Pool(5)
    tasks = ["吃饭", "睡觉", "玩游戏", "看书", "做作业", "学习", "看视频"]
    for task1 in tasks:
        pool.apply_async(task, args=(task1,), callback=callback_func)
        # callback 回调函数

    pool.close()  # 添加任务结束
    pool.join()  # 堵住主进程
    # 主进程结束，进程池就会结束。
    for c in containrt:
        print(c)

    print("over!!!")
