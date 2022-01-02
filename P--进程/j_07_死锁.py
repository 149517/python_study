from threading import Thread,Lock
from time import sleep

lockA = Lock()
lockB = Lock()

class MyThread(Thread):
    def run(self):
        if lockA.acquire():
            print(self.name,"获取了A锁")
            sleep(0.5)
            if lockB.acquire():
                print(self.name,"获取了B锁，还有一个A锁")
                lockB.release()
            lockA.release()

class MyThread2(Thread):
    def run(self):
        if lockB.acquire():
            print(self.name,"获取了B锁")
            sleep(0.5)
            if lockA.acquire():
                print(self.name,"获取了A锁，还有一个B锁")
                lockA.release()
            lockB.release()

if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread2()

    t1.start()
    t2.start()