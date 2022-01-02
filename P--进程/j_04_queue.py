# from multiprocessing import Queue
#
# q = Queue(5)
#
# q.put("a")
# q.put("b")
# q.put("c")
# q.put("d")
# q.put("e")
# s = q.qsize() # 获取队列长度
# print(s)
# # q.full():    # 判断队列是否满了
#
# # q.empty():    # 判断队列是否是空的
# q.put("f", timeout=4)   # timeout 超时，在等待队列的时候，超过一定时间就抛出错误
#
# q.get()
# q.get()
# q.get()
# q.get()
# q.get()

from multiprocessing import Process, Queue
import time


def download(q):
    images = ['000.jpg', '001.jpg', '002.jpg', '003.jpg', '004.jpg', '005.jpg']
    try:
        for i in images:
            print("{} 正在下载,时间{}".format(i,time.time()))
            time.sleep(0.5)
            q.put(i, timeout=2)
    except:
        print("队列已满")

def getfile(q):
    while True:
        try:
            file = q.get(timeout=2)
            print("{} 下载成功".format(file))
        except:
            break



if __name__ == "__main__":

    q = Queue(5)

    p1 = Process(target=download, args=(q,))

    p2 = Process(target=getfile, args=(q,))

    p1.start()
    p2.start()
    p2.join()
    print("00000")