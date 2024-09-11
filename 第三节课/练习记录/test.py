#!/usr/bin/python3
 
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
abbababbab [ \n ]。
"""
print (para_str)
 
print ("我叫 %s 今年 %d 岁!" % ('yzb', 18))

list=[1,2,3,4,"bxxx"]
print( list[0] )
print( list[1] )
print( list[4] )
print( list[-1] )
print(list[2:4])
list[0]=6
list.append(7)
print(list)
del list[0]
print(list)
print([1,2,3]+list)
print(list*4,end=" ")
list2=[list,[123],[456]]
print(list2)
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))

tup=(1,2,3,"yzb")
tup2=(2,3,4)
tup3=tup+tup2
print(tup)
print(tup2)
print(tup3)
del tup3
print(tup*2)
print(len((1,2,3)))
print(tup[1])
print(tup[0:3])

d={"name":"yzb","学号":"23020007139"}
print(len(d))
print(type(d))
print("name ",d["name"])
print("学号 ",d["学号"])
d["school"]="ouc"
print(d)
del d["school"]
print(d)
d.clear
del d   

set2={1,2,3,4}
set1=set([1,2,3,4,5,6])
print(set1&set2)
print(set1-set2)
print(set1^set2)
set2.add(9)
set2.update([2,6,7,4])
print(set2)
set2.remove(1)
print(set2)
set2.discard( 2)
print(set2)

set2.pop() 
print(set2)
len(set2)
set2.clear()
print(set2)


score = int(input("请输入一个成绩（0-100 之间的整数）: "))  
   
if not (0 <= score <= 100):  
    print("输入错误")  
else:  
    if score < 60:  
        print("不及格")  
    elif 60 <= score <= 79:  
        print("及格")  
    elif 80 <= score <= 89:  
        print("良好")  
    else: 
         print("优秀")



def fibonacci(n):  
    if n <= 0:  
        return 0  
    elif n == 1:  
        return 1  
      
    a, b = 0, 1  
    for _ in range(2, n + 1):  
        a, b = b, a + b  
    return b  
  
# 测试  
n = int(input("请输入N的值："))  
print(f"斐波那契数列的第{n}项是：{fibonacci(n)}")

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# 使用示例
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("栈顶元素:", stack.peek())  # 输出: 栈顶元素: 3
print("栈大小:", stack.size())    # 输出: 栈大小: 3

print("弹出元素:", stack.pop())  # 输出: 弹出元素: 3
print("栈是否为空:", stack.is_empty())  # 输出: 栈是否为空: False
print("栈大小:", stack.size())    # 输出: 栈大小: 2


import cmath

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))
 
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
 
print('结果为 {0} 和 {1}'.format(sol1,sol2))