print("Hello_python\nHello_pyCharm")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def sit(self):
            print(f"{self.name} is now sitting.")

        def roll_over(self):
            print(f"{self.name} rolled over!")


my_dog = Dog('While', 6)
print(f"My dog's name is {my_dog.name}.")
# f 是 format 的简写 合并两个或者多个值
print(f"My dog is {my_dog.age} years old.")


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
my_new_car.update_odometer(33)  # 使用一个方法修改里程
my_new_car.read_odometer()
my_new_car.update_odometer(32)  # 在类方法中  设置了 防止回调机制
my_new_car.read_odometer()
my_used_car = Car('adui', 'a3', '2017')
my_used_car.update_odometer(23500)
my_used_car.read_odometer()


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # 超类  能够调用父类的方法
        self.battery_size = 75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def fill_gas_tank(self):
        print("电动车没有汽油箱!")


my_tesla = ElectricCar('tesla', 'model S', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

from random import randint

print(randint(23,89))   #返回一个随机数字

from random import choice
players = ['charles','martina','michael','florence','eil']
first_up = choice(players)      #  choice  随机返回列表或者元组内的一个元素
print(first_up)

with open('001.txt') as file_1:
    for line in file_1:
        print(line)     #使用逐行读取，  会增加较多的空行
with open('001.txt') as file_2:
    for line in file_2:
        #print(line.rstrip())    #删除结尾的空行
        print(line.strip())     #删除每行中的空格
with open('001.txt') as file_3:
    contents = file_3.read()
    print("\n"+contents)
    print(len(contents.rstrip()))
with open('001.txt') as file_4:
    lines = file_4.readlines()
    tes = ''
    for line in lines:
        tes += line.strip()
    print(tes)

# with open('pi_million_digits.txt') as file_5:
#     lines = file_5.readlines()
#     string = ''
#     for line in lines:
#         string += line.strip()
#     birthday = input("Enter your birthter,in the form mmddyy:")
#     if birthday in string:
#         print("Your birthday appears in the first million digits of pi !\n")
#     else:
#         print("Your birthday does not appear in the first million diaits of pi.\n")
#     string.replace('149517','_____________________________________________________________________________________')
#     print(f"前54位：{string[:54]}....")
#     print(len(string))
# filename = '210806.txt'
# with open(filename,'a') as file_6:
#     file_6.write("\n现在时间是2021年8月7日，早上09点48分\n")
#     file_6.write(str(78945641))

# na = input("请输入你的用户名;\n")
# mi = input("亲输入你的密码：\n")
# with open('002.txt','a') as file_7:
#     file_7.write(na+"\n"+mi)
# print("录入完成")

with open('002.txt','r') as file_8:
    line_1 = file_8.readline()
    line_2 = file_8.readline()
    print(f"账号为：{line_1}")
    print(f"密码为：{line_2}")
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
