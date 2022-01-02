def descript_prtson(person):
    print("Description of",person['name'])
    print('Age',person['age'])
    try:
        print("Occupation:",person['occupation'])
    except KeyError:pass
descript_prtson({'name':'Boo','age':12})

'''
闭包
1.嵌套函数
2.内部函数引用外部函数变量
3.返回值是内部函数
'''
def Boo(n):
    a=34

    def co():
        print("yigehsuzi:"+str(a+n))
    return co

b = Boo(23)
print(b)
b()

#全局变量在函数内部修改要用 global
print(globals()) #globals() 查看全局变量

print(locals())#locals()  查看局部变量



"""
装饰器

"""



def decorater(func):
    def wap():
        func()
        print('扩建')
        print('装修')
        print('升级')
        print('落成')
    return wap


@decorater
def house():
    print("简陋屋子...")


house()
