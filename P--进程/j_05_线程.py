import threading
from time import sleep

m = 89
def download(q):
    global m
    images = ['000.jpg', '001.jpg', '002.jpg', '003.jpg', '004.jpg', '005.jpg']
    for i in images:
        print("{} 正在下载,时间".format(i, ))
        sleep(q)
        print("下载完成：{}".format(i, ))
        m+=5


def listMu(q):
    global m
    music = ["入海", "春风十里", "狂妄", "红玫瑰", "玫瑰少年"]
    for i in music:
        print("听 {} 这首歌".format(i, ))
        sleep(q)
        print("{} 听完".format(i, ))
        m += 10

if __name__ == '__main__':

    t = threading.Thread(target=download, args=(1,))
    t.start()
    n = 1
    t1 = threading.Thread(target=listMu,args=(0.4,))
    t1.start()

    t.join()
    t1.join()
    print(m)    # 169
    while True:
        sleep(0.3)
        print(n)
        n += 1
