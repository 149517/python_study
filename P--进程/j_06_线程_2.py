# import threading
#
# ticket = 0
# def task():
#     global ticket
#     for i in range(1000000):
#         ticket += 1
#     print("task---->de ticket 是 ",ticket)
#
#
# def task2():
#     global ticket
#     for i in range(1000000):
#         ticket += 1
#     print("task2---->de ticket 是 ",ticket)
#
#
# t = threading.Thread(target=task)
# t1 = threading.Thread(target=task2)
# t.start()
# t1.start()
# t1.join()
# print("ticket最后的值为：",ticket)

# 不添加锁的情况下，数据就会不安全，多次重复使用，导致最后的结果不正确
# 数据量过大，自带的 GIL 就会解开


import threading

ticket = 0
def task():
    lo.acquire()
    global ticket
    for i in range(1000000):
        ticket += 1
    print("task---->de ticket 是 ",ticket)
    lo.release()


def task2():
    lo.acquire()
    global ticket
    for i in range(1000000):
        ticket += 1
    print("task2---->de ticket 是 ",ticket)
    lo.release()


lo = threading.Lock()   # 添加锁
t = threading.Thread(target=task)
t1 = threading.Thread(target=task2)
t.start()
t1.start()
t1.join()
print("ticket最后的值为：",ticket)