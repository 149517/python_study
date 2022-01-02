"""使用pip下载时候可以在包后面加上一个 -i 加上国内镜像网址、
列如：pip install Django -i https://pypi.tuna.tsinghua.edu.cn/simple"""

import random

coins = 0

while (input("输入 0 退出")) != 0:
    while coins > 5:
        coins -= 5
        print("开始进行猜大小。（两个骰子 大于6为大）")
        n = random.randint(1, 13)
        y = input("输入你的答案：输入大（d） 小（x）")
        if n <= 6 and y == "x":
            print("duile ")
            coins += 6
            print("coins surplus :" + str(coins))
        elif n > 6 and y == "d":
            print("duile")
            coins += 6
            print("coins surplus :" + str(coins))
        else:
            print("error")
            coins -= 2
            print("coins surplus :" + str(coins))
    else:
        m = int(input("充值（1）或退出（0）"))
        if m == 1:
            j = int(input("输入充值金额："))
            coins = j * 10
            print("coins surplus :" + str(coins))
        else:
            print("game over")
            print("coins surplus :" + str(coins))
