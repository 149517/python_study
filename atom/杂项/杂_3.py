# print("hello world!")
# print("good")
# name = "bilibili"
#
# print(name.upper())#大写函数
# #列表
# # list=["c","c++","python","javaScrpit","Linux"]
# # print(list[2])
# # list.pop()#删除末尾的元素
# # print(list)
# # list.remove("c++")#根据元素名称删除
# # print(list)
# # print(list[-1])#访问列表最后一个元素
# nas=["zhangxiao","liguang","hezijian","zhongzhiping","mingming"]
# nas.sort()#永久性的重新排序，sorted是暂时性的
# print(nas)
# for na in nas:#创建新的变量，将nas的值储存起来并且循环遍历
#     print(na)
# magicians=['alice','divid','carolina']
# for magician in magicians:
#     print(magician.title()+",that was a great trick")
#     print("hello!")
#     print("\t")
# for value in range(1,12):#生成从1到11的数字
#     print(value)
#
# #转换为数字列表
# li = list(range(1,34))#list()形成列表
# print(li)
# lis = list(range(2,25,2))#第三个参数是表示从2开始每一项都加2，直到结束
# print(lis)
# squares=[]
# for va in range(1 ,13):
#     square = va**2
#     squares.append(square)
# print(squares)
# min(squares)
# max(squares)
# sum(squares)
# print(sum(squares))
# sq=[s**3 for s in range(1,9)]
# print(sq)
# a=list(range(1,1000001))
# print(min(a))
# print(max(a))
# print(sum(a))
# b=list(range(1,21,2))#从1到20内的奇数
# for c in b:
#     print(c)
# #3的倍数
# d = list(range(3,31,3))
# for e in d:
#     print(e)
#
# g = []
# for f in range(1,21):
#     gs=f**3
#     g.append(gs)
#
# print(g)
# print(g[1:6])#切片，将列表中下标为1~6的元素提取出来
# #gn=g------这样是错误的
# gn=g[:]#需要使用切片
# print(gn)
# gn.pop()#不适用切片的方法会同时修改两个列表
# print(g)
# print(gn)
# gn=["12","45"]
# print(gn)
# #元组
# dimensions = (200,50)
# for dimension in dimensions:
#     print(dimension)
# dimensions =(300,400)#重新赋值，但并不允许修改元组元素
# for dimension in dimensions:
#     print(dimension)
#
#
# cars =['audi','bmw','subaru','toyota']
# for car in cars:
#     if car=='bmw'or car =='toyota':
#         print(car.upper())
#     else:
#         print(car)
# print('audi' in cars)  #打印结果为True，
# #in 用于检查某个元素是否在列表中
# #not in  检查元素是否不再列表中
# banned_users = ['andrew','carolina','david']
# user = 'marie'
# if user not in banned_users:
#     print(user.title()+",you can post a response if you wish.")
# # 返回True后执行打印
# ba = list(range(12,22))
# for bas in ba:
#     if bas >=18:
#         print("chennian")
#     elif bas >= 15:  #else if---elif  可以使用多个elif
#         print(bas)
#     else:
#         print("xiaohai")
# alien_color = ['green','yellow','red','white','black','blue']
# for alien in alien_color:
#     if alien == 'white':
#         print("*****")
#     elif alien == 'red':
#         print("jisha")
#     else:
#         print(alien)
# ac = []
# ssc = []
# bba = ['12']
# if ac == ssc:  #在这里我使用了一个空列表与原来的列表进行参照，检查是否为空列表
#     print("kong")
# if bba:   #这里直接使用了if检查
#     print("feikong")
# if ac:
#     print("shenm")
#
# #字典
# alien_0 = {'color':'green','point':5}
# print(alien_0)
# print(alien_0['color'])
# alien_0['color']='blue'#修改值
# print(alien_0)
# alien={'seep':1,'color':'white',}
# a='medium'
# if a=='slow':
#     alien['seep']+=1
# elif a=='medium':
#     alien['seep'] += 2
# else:
#     alien['seep'] += 3
# print(alien['seep'])
# del alien['color']  #删除‘键’
# print(alien)
# favorite_languages = {
#     'jen' : 'python',
#     'sarah' : 'C',
#     'edward' : 'ruby',
#     'phil':'java',
#     }
# print("Sarah's favorite_language is "+ favorite_languages['sarah'])
# vocabulary={
#     'print':'屏幕输出',
#     'range':'一串数字',
#     'list':'清单列表',
#     'str':'输出时，将整形转化为字符输出',
#     'for   in   :':'循环，创造新的变量储存遍历',
#     'append':'将元素添加到列表末尾',
#     'insert':'在列表任意位置添加元素',
#     'del':'删除某个元素',
#     'pop':'删除列表末尾的元素，并接着使用这个元素',
#     'remove':'根据元素值来删除元素,只删除列表中第一个这样的值',
#     'sort':'永久性的更改列表排序，首字母',
#     'sort(reverse=True)':'首字母反向顺序',
#     'sorted':'暂时性的排序，并不影响初始的列表排序',
#     'reverse':'反向打印列表',
#     'len':'列表长度',
#     '[1:4]':'列表切片，将这里面的值提取出来',
#     'items':'返回一个键-值对列表',
#     'keys':'返回字典中键的键,也可以返回一个列表（包含所有字典中的所有键）用于判断某个键是否包含与列表',
#     'values':'返回字典中的值',
#     'set':'剔除重复的值，是每个元素都是独一无二的，集合'
#     }
# print(vocabulary)
# for voca,vo in vocabulary.items():   #这里用了两个变量储存值
#     print("\nvocabulary:"+voca)
#     print("user:"+vo)
# for v in vocabulary.keys():
#     print(v.title())
# if 'keys' not in vocabulary.keys():   #返回false,所以print没有运行
#     print("keys,please take our poll.")
# for voca in sorted(vocabulary.keys()):    #按顺序遍历
#     print(voca.title())
# for voc in vocabulary.values():  #返回字典中的值，
#     print(voc)
# for voc in set(vocabulary.values()):   #set 集合 ，剔除了重复的值
#     print(voc)
#
# aliens = []
# for alien_number in range(30):  #这里的  range(30)  的作用是告诉计算机循环30次
#     new_alien = {'color':'green','point':5,'speen':'slow'}
#     aliens.append(new_alien)   #所以new.alien 内有30个字典，然后又都被储存进aliens
#
# for alien in aliens[:5]:
#     print(alien)
# print("···")
#
# print("Total number of aliens:"+str(len(aliens)))
# #修改
# for alien in aliens[:4]:   #将 aliens的前4个字典赋给alien
#     if alien['color'] =='green':
#         alien['color']='yellow'
#         alien['point']=10
#         alien['speen']='medium'
#     print(alien)
#
# pizza = {
#     'crust':'thiick',
#     'toppings':['mushrooms','extra cheese'],   #字典中包含列表
# }
# for pi in pizza.keys():
#     print(pi)
# for piz in pizza.values():
#     print(piz)
# for pizz in pizza['toppings']:
#     print(pizz)
#
# ma ={
#     'name':'zhang',
#     'fri':{'boys':['mingm','zhanliang'],
#            'grils':'liuz'},   #字典中包含字典
#     'num':"mimi",
# }
# na=[]
# ns = []
# for na,ns in ma.items():
#     print(na)
#     print(ns)
#
#
# # message = input("Tell me something,and I will repeat it back to you:\n")
# # print(message)
# # age = input("How old are you?\n")
# # age = int(age)   #转化了类型
# # if age >= 20:
# #     print("cehngnain")
# # elif age >=65:
# #     print("laonian")
# # else:
# #     print("weichengn")
#
# # boo = int(input("How old aare you?\n"))
# #
# # lian = int(input("输入随机值，判断他是否是3的倍数：\n"))
# # if lian % 3 == 0:
# #     print(str(lian)+"是3的倍数。")
# # else:
# #     print(str(lian)+"不是3的倍数")
# vb = 1
# while vb <=6:
#     print(vb)
#     vb+=1
#
# # vbc = 0
# # vbc = input("qin shu ru:")
# # while vbc != 'f':   # 这里如果使用变量就是死循环， 但是用input()每次进入while 都会运行一次input
# #     print("hello world")
#
# # print("12岁以下的免票，未成年人半价：")
# # while input("输入quit结束程序。") != 'quit':
# #     age = int(input("请输入你的年龄、"))
# #     if age <=12:
# #         print("mianfei youwang")
# #     elif age <=18:
# #         print("mengiao banjia ")
# #     else:
# #         print("quanpiao")
# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []
#
# while unconfirmed_users:   #一直循环，直到列表为空值时候停下
#     current_user = unconfirmed_users.pop()   #删除最后一个元素并使用这个元素
#
#     print("Verifying user:"+current_user.title())
#     confirmed_users.append(current_user)
# pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)
#
# while 'cat' in pets:    #运用while和remove删除列表中的重复元素
#     pets.remove('cat')
# print([pets])
#
# mes = {'book':'nihao',
#        'age':18,}
# v=True
# count=1
#
# #实现有while循环加键和值进入字典
# while v:
#     name = input("\nWhat is your name?")
#     response = input("Which mountain would you like to climb someday?")
#     mes[name]=response   #将输入与储存进字典分开
#     count+=1
#     if count==5:
#         v=False
# for me in mes.items():
#     print(me)
""""函数"""
def greet_user(username):
    print("hello, "+ username.title()+"!")

greet_user('jesse')

#位置实参，按照顺序传递
def get_sum(a,b):
    sum=a+b
    print("a+b="+str(sum))
v=0
while v<=10:
    get_sum(23,45)
    get_sum(87,95)
    print(v)
    print("\n")
    v+=1
def get_quyu(c,d):
    return c%d

print(get_quyu(50,6))


abv =234
bac =654
print(abv)
def get_(adv,bac):
    return adv*bac

print(get_(abv,bac))   #使用关键字做形参

def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
#返回一个字典
musician = build_person('jimi','hendrix')
for music in musician.values():
    print(music)

# def get_sums(sh,mo):
#     return int(sh+mo)
#
# while True:
#     sh = int(input("sh="))
#     mo = int(input("mo="))
#     print(type(sh))
#     if sh == 0:
#         break
#     print("两数之和为："+str(get_sums(sh,mo)))

#斐波那契数列
# m =1
# n =1
# count =2
# mn = int(input("kon zhi shu:"))
# print("1  1  ")
# while int(count) < mn:

    # m=m+n
    # n=m+n
    # print("count="+str(count))
    # print(str(m)+'  ')
    # count+=1
    # print(str(n)+'  ')
    # count += 1

# def Prin(size,*toppings):   #无论传递多少数组都会被存储到toppings中，
#     print("Making a pizza with the follwing toppings:")
#     for topping in toppings:
#         print("-"+topping)
# #在传递时先匹配位置实参和关键字实参
# Prin(12,'mushrooms','green peppers','extra chess')
#
# def build_profile(first,last,**user_info):
# #将诸多的形参储存到字典
#     profile={}
#     profile['first_name']=first
#     profile['last_name']=last
#     for key,value in user_info.items():
#         profile[key]=value
#     return profile
# user_profile = build_profile('albert','einstein',location='princeton',filed='physics')
# print(user_profile)
# import ma    #导入文件ma
# print(ma.Sum(1123,98))   #调用ma中的Sum 函数，，需要用句点来表示
# from ma import Sur   #调用来自ma文件的 Sur函数，不用先导入文件
# print(Sur(43,3))
#
# from ma import SumSur as L  #调用来自ma 中的函数SumSur 并重命名为 L
# print(L(45,4))
#
# from ma import*    #导入模块中所有的函数，不需要用句点表示

""""类"""
# class Dog():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def sit(self):
#         print(self.name.title()+"is now sitting.")
#
#     def roll_over(self):
#         print(self.name.title()+"rolled over!")
#
# #实例
# my_dog = Dog('while',6)
#
# print("My dog's name is"+ my_dog.name.title()+".")
# print("My dog is "+str(my_dog.age)+"years old.")
#
# class Car():
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odometer_reading=0   #在__init__中指定初始值，一旦指定了初始值就不必为其添加形参数
#
#     def get_descriptive_name(self):
#         long_name = str(self.year)+' '+self.make+' '+self.model
#         return long_name.title()
#     def read_odometer(self):
#         print("This car has "+str(self.odometer_reading)+" miles on it.")
#
#     def update_odometer(self,mileage):
#         #self.odometer_reading = mileage
#         if mileage >= self.odometer_reading:    #控制，预防参数被回调
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles   #递增
#
# my_new_car=Car('auid','a4',2016)
# print(my_new_car.get_descriptive_name())
# #my_new_car.odometer_reading =23    #直接修改属性的值
# my_new_car.update_odometer(42)    #调用并提供了实参，修改了属性的值
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(23500)
# my_new_car.read_odometer()
#
# my_new_car.increment_odometer(100)      #递增特定的量(通过方法递增）
# my_new_car.read_odometer()
#
#
#
#
# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#
# my_tesla = ElectricCar('tesla','model_s',2016)
# print(my_tesla.get_descriptive_name)

# class Car():
#
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odometer_reading =0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year)+' '+self.make+' '+self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has"+str(self.odometer_reading)+" miles on it.")
#
#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles
#
# class ElectricCar(Car):
#
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery_size = 70      #这里添加了一条属于电瓶车独有的信息，并通过方法将其打印出来
#
#     def describe_battery(self):
#         print("This car has a "+str(self.battery_size)+"-KWH battery.")
#
# my_tesla = ElectricCar('tesla','model s',2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

# class Car():
#
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odometer_reading =0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year)+' '+self.make+' '+self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has"+str(self.odometer_reading)+" miles on it.")
#
#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles
#
# class Battery():
#
#     def __init__(self,battery_size=70):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print("This car has a "+str(self.battery_size)+ "-KWH battery.")
# class ElectricCar(Car):
#
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery = Battery()
#
# my_tesla = ElectricCar('tesla','model s',2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
#
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())    #.rstrip()   删除字符串末尾的空白
#
# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())
#
# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()     #readlines 让文件读取一行，并储存到列表中
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#     print(line.rstrip())
#     print(pi_string)
#     print(len(pi_string))
# filename = 'pi_million_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string=''
# for line in lines:
#     pi_string += line.strip()
# birthday = input("Enter your birthday, in the from mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
#     birthday = birthday.replace('0517','               ')       #将字符串中的特定单词替换
#     #print(pi_string)
# else:
#     print("Your birthday does not appear in the first million digits of pi!")
# print(pi_string[:52]+"····")
# print(len(pi_string))

# filename = 'proramming.txt'
# with open(filename,'w') as file_object:
#     file_object.write("你好，现在是2021年5月30日10:20。")
# with open(filename,'a') as file_object:
#     file_object.write("\n现在是早上。\n")
#
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg="Sorrry, the file "+filename+" does ot exit."
#     print(msg)
# else:
#     words = contents.split()    # 根据空格划分，并将其存储为列表 计算文本中的单词数量， spilt()是依据单词之间的空格划分，所以中文不能够计算出来
#     num_words = len(words)
#     print("The file "+filename+" has about " + str(num_words)+" words.")

def count_words(filename):
    """计算文件大概包含多少个单词"""
    try:
        with open(filename) as file_obj:
            contents=file_obj.read()

    except FileNotFoundError:
        print("Sorry ,the file "+filename + " does to exit.")
        #可以在except  下面输入pass  ，在程序运行失败时候什么都不做 ，直接跳过
    else:
        """计算文件包含多少个单词"""
        w = contents.split()
        num = len(w)
        print("The file " + filename + " has about " + str(num) + " words.")

    #异常
try:
    print(5/0)      #当出现print(5/0) 这样的错误时就会执行except  下的代码，而不会出现 traceback
except ZeroDivisionError:
    print("You can't divide by zero!")

filenaems = ['alice.txt','little_woman.txt','moby_dict.txt','siddhartha.txt','book.txt']
for filename in filenaems:
    count_words(filename)

import json
#引入json
# numbers = [2,3,5,7,9,11,13]
#
# file = 'numbers.json'
# with open(file,'w') as f_obj:     #以写入的方式打开 json
#    json.dump(numbers,f_obj)      #将numbers储存到 f_obj


file = 'numbers.json'
with open(file) as f_obj:
    numbers = json.load(f_obj)      #打开 json，并读取
print(numbers)


#import unittest    #引入测试模块
#from ma import get_formatted_name
# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name:")
#     if first == 'q':
#         break;
#     last = input("Please give me a lase name:")
#     if last =='q':
#         break;
#
#     formatted_name = get_formatted_name(first,last)
#     print("\tNeatly formatted name: "+formatted_name+'.')
# class NamesTestCase(unittest.TestCase):
#     def test_first_last_name(self):
#         formatted_name = get_formatted_name('janis','joplin')
# unittest.main()
print("hello world")