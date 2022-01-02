from greenlet import greenlet
from time import sleep

def aa():
    for i in range(6):
        print("A" + str(i))     # 输出展示
        gb.switch()             # 手动协成调用
        sleep(0.4)              # 阻塞


def bb():
    for i in range(6):
        print("B" + str(i))
        gc.switch()
        sleep(0.4)


def cc():
    for i in range(6):
        print("C" + str(i))
        ga.switch()
        sleep(0.4)


if __name__ == '__main__':
    ga = greenlet(aa)
    gb = greenlet(bb)
    gc = greenlet(cc)

    ga.switch()
