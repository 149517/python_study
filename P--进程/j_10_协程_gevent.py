import gevent
import time
from gevent import monkey
monkey.patch_all()
def aa():
    for i in range(6):
        print("A" + str(i))     # 输出展示
        time.sleep(0.4)              # 阻塞


def bb():
    for i in range(6):
        print("B" + str(i))
        time.sleep(0.4)


def cc():
    for i in range(6):
        print("C" + str(i))
        time.sleep(0.4)


if __name__ == '__main__':
    ga = gevent.spawn(aa)
    gb = gevent.spawn(bb)
    gc = gevent.spawn(cc)

    ga.join()
    gb.join()
    gc.join()
