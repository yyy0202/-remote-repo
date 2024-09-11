#!/usr/bin/python3

print("Hello, World!")
'''
多行注释
多行注释
'''
#注释
"""
多行注释
多行注释
"""
#行与缩进
if True:
   print("true")
else:
   printf("false")
#多行语句
a=1
b=2
c=3
d=4
total=a+\
      b+\
      c+\
      d+1+4+6
print(total)
#数字和字符串
word='字符串'
sentence="不想学习"
paragraph='''不想学习的段落
不想学习的段落'''
str='2274691497'
print(str)
print(str[0:-1])#输出整个字符串
print(str[0])#输出第一个字符
print(str[3:])#输出第四个开始到最后的字符串
print(str[1:5:2])#步长为2
print(str*2)
print(str+"yzb")
print("hello\nyzb")
print(r"hello\nyzb")

#空行分割代码
# 等待用户输入 
'''
user_input = input("请输入一些文本: ")  
  
# 显示输入的文本  
print("你输入了:", user_input)
input("\n\n按下 enter 键后退出。")
'''
'''
#同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

#代码组
i=input("输入一个数字")
num=int(i)
if(num==1):
   print("你输入的是1")
elif(num==2):
   print("你输入的是2")
else:
   print("你输入的不是1也不是2")

#print输出
x="abc"
y="efg"
#换行输出
print(x)
print(y)
#不换行输出
print(x,end="")
print(y)

#导入sys模块
import sys#sys模块提供有关Python解释器及其环境的变量和函数。
print('================Python import mode==========================')
print ('命令行参数为:')  
for i in sys.argv:  #sys.argv是一个列表，其中包含了命令行参数的字符串。
    print (i)
print ('\n python 路径为',sys.path)

from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

'''
#隐式数据类型转换
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int 数据类型为:",type(num_int))
print("num_flo 数据类型为:",type(num_flo))

print("num_new 值为:",num_new)
print("num_new 数据类型为:",type(num_new))
#显式数据类型转换
y=int(2.8)
x=float(3)
num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("类型转换前，num_str 数据类型为:",type(num_str))

num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:",type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:",num_sum)
print("sum 数据类型为:",type(num_sum))

#多个变量赋值
a, b, c = 1, 2, "runoob"
print(a)
print(b)
print(c)
#Number

a=20.0
print(type(a))
isinstance(a,int)
isinstance(a,float)
isinstance(bool,int)
var1=2
var2=3
print(var1,var2)
del var2,var1

import random  
  
def choose_random_player(players):  
    if not players:  
        raise ValueError("玩家列表不能为空")  
      
    return random.choice(players)  
  
players = ["A", "B", "C", "D"]  
chosen_player = choose_random_player(players)  
print(f"随机选择的玩家是: {chosen_player}")

var1 = 'Hello World!'
var2 = "Runoob"
 
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
print ("已更新字符串 : ", var1[:6] + 'Runoob!')
import time

for i in range(101):
    print("\r{:3}%".format(i),end=" ")
    time.sleep(0.05)
#"\r"的作用是将光标移回当前行的开头，但不换行。
#"{:3}%".format(i)是一个字符串格式化表达式，
# 其中{:3}指定了一个宽度为3的字段，用于格式化整数i，后面跟着一个百分号%。
#end=''不换行

#转移字符print('\'Hello, world!\'')  # 输出：'Hello, world!'

print("Hello, world!\nHow are you?")  # 输出：Hello, world!
                                        #       How are you?

print("Hello, world!\tHow are you?")  # 输出：Hello, world!    How are you?

print("Hello,\b world!")  # 输出：Hello world!

print("Hello,\f world!")  # 输出：
                           # Hello,
                           #  world!

print("A 对应的 ASCII 值为：", ord('A'))  # 输出：A 对应的 ASCII 值为： 65

print("\x41 为 A 的 ASCII 代码")  # 输出：A 为 A 的 ASCII 代码

decimal_number = 42
binary_number = bin(decimal_number)  # 十进制转换为二进制
print('转换为二进制:', binary_number)  # 转换为二进制: 0b101010

octal_number = oct(decimal_number)  # 十进制转换为八进制
print('转换为八进制:', octal_number)  # 转换为八进制: 0o52

hexadecimal_number = hex(decimal_number)  # 十进制转换为十六进制
print('转换为十六进制:', hexadecimal_number) # 转换为十六进制: 0x2a
