# 操作
# 1，实现图书信息的录入
# 2，现有图书的查询
# 3，图书的售出（删除）
#

import os

# 信息录入
    book={}     # 创建字典
    names=[]
    authors=[]
    pieces = []
def _input():
    while(True):
        print("输入 000 退出录入。")
        name = input("输入图书名：")
        if name == '000':
            break
        author = input("输入作者信息：")
        piece = int(input("输入价格："))

    names.append(name)
    authors.append(author)
    pieces.append(piece)
    book = dict(zip(names,[authors, pieces]))
    return book

_input()
print(book)
