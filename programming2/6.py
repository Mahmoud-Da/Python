#!/usr/bin/env python
# coding: utf-8

# # 4. 授業課題

# 
# ### 1. 変数 x の値が,
# - 3 の倍数ならば文字列「Fizz」を表示,
# - 5 の倍数ならば文字列「Buzz」を表示,
# - 15 の倍数ならば文字列「FizzBuzz」を表示
# 
# ### するプログラムを作り，x = 自分の学籍番号を代入したときの結果を表示させよ.

# In[1]:


i =2191180 # x に数値を代入
a = i % 3 == 0 # i が3 の倍数のときは
b = i % 5 == 0 # i が5の倍数のときは
c = i % 15 == 0 # i が15の倍数のときは
if c :
 print("x=", i, ":FizzBuzz")#Fizz Buzz
elif b :
 print("x=", i, ":Buzz") #Buzz
elif a:
 print("x=", i, ":Fizz") #Fizz
else:
 pass # なにもしない


# ### 2. 変数 x の値が,
# - 3 の倍数ならば文字列「Fizz」を表示,
# - 5 の倍数ならば文字列「Buzz」を表示,
# - 15 の倍数ならば文字列「FizzBuzz」を表示
# 
# ### するプログラムを作り，x = 1~1000 まで繰り返して結果を表示させよ.

# In[2]:


for x in range (1,1000):
    if x % 3 == 0 and not x %5 == 0 :# i が3 の倍数のときは
     print("x=",x, ":Fizz")
    elif x % 5 == 0 and not x %3 == 0 : # i が5の倍数のときは
     print("x=", x, ":Buzz") #Buzz
    elif x % 15 == 0 : # i が15の倍数のときは
     print("x=", x, ":FizzBuzz")#Fizz Buzz
