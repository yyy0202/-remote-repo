import datetime
def getYesterday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    return yesterday
 
print(getYesterday())


total = 0
  
list1 = [1,2,3,4,5,6,7,8,9,10]  
  
for ele in range(0, len(list1)): 
    total = total + list1[ele] 
  
print("列表元素之和为: ", total)

def dic1():  
    print ("按键(key)排序:")   
    for i in sorted (key_value) : 
        print ((i, key_value[i]), end =" ") 
def dic2():
     print()
     print ("按值(value)排序:")   
     print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))     
   
  
key_value ={}                
key_value[2] = 56       
key_value[1] = 2 
key_value[5] = 12 
key_value[4] = 24
key_value[6] = 18      
key_value[3] = 323    
dic1()
dic2()

str='yzb'
print(str[::-1])


lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
 
for num in range(lower,upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)