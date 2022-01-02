from time import sleep

# 使用生成器---完成协程
def task1():
    for i in range(5):
        print("A" + str(i))
        yield
        sleep(0.5)

def task2():
    for i in range(5):
        print("B" + str(i))
        yield
        sleep(1)

if __name__ == "__main__":
    g1 = task1()
    g2 = task2()
    while True:
        try:
            next(g1)
            next(g2)
        except:
            break
