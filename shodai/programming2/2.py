#!/usr/bin/env python
# coding: utf-8

# # 中間レポート課題

# ### 1.
# フィボナッチ数列の項の内，
# 偶数かつ 1000 未満 の項を全て足した値を求め，表示させよ

# In[1]:


a = 1 #　フィボナッチ数列の２　つ前のころを表す変数
b = 1 #　フィボナッチ数列１つ前のころを表す変数
c = a + b # フィボナッチ数列の現在のころを表す変数

total = 0 #　答えを格納しておく変数

while c < 1000: #1000未満のとき
    if c % 2 == 0: #偶数のときの処理
        total += c  #ｃだけ増やす
      
    a, b, c = b, c, b +c#アンパック代入を利用
print(total)#結果を表示


# ### 2.
# 5 番目のメルセンヌ素数をプログラミングにより求め，表示させよ.
#      

# In[5]:


def isprime(n): #　素数でかを判断する関数
    for i in range (2,n-1):
        if n % i == 0:
            return False
    return True

def ismersenne(n): #　n が　２~ｍ－１ の形をしているかどうか判定する関数
    m = 1
    while n >= 2**m - 1:
        if n == 2**m -1: #　n が　２~ｍ－１を等しい　とき
            return True
        m += 1
    return False

count = 0 #メルセンヌ素数の個数を格納しておく変数
n = 3

while True:
    if isprime(n) == True and ismersenne(n) == True:
        count += 1
        if count == 5: #5番目メルセンヌ素数の個数が見つけたとき
            break
    n += 1
print(n) #結果を表示


#  ### 3.
# adjacent.txt には 1000 桁の数が 1 個記録されている.
# 
# この数の隣接する 4 桁の数の積の最大値は 9×9×8×9 = 5832である.
# 
# さて，adjacent.txt に記録されている数について，
# 隣接する 13 桁の積の最大値を求めよ.
# 

# In[3]:


import functools
import operator
with open("adjacent.txt", "r", encoding="utf-8") as f:#ファイルを開く
    numbers = list(f.read().strip())  # ファイルを読み込み、各要素が1つの数字を表すリストにする
    numbers = list(map(int, numbers))  # 文字列を int 型に変換
size = 13
max_prod = 0
for i in range(len(numbers) - size + 1):#forループ使用
    chunk = numbers[i:i + 13]  # i, i + 1, ..., i + 12 番目の13個の数字を取り出す。
    prod = functools.reduce(operator.mul, chunk, 1)# 部分リストのすべての値の積
    max_prod = max(max_prod, prod)# 最大値更新


print(max_prod)#結果を表示


# ### 4.
# 1 以上 1, 000以下の初期値 n の内，
# 
# コラッツ予想に関する操作を繰り返して，1 になるまでの数列の長さが
# 
# 最大になる n を求め，表示させよ.

# In[4]:


def collatz(n):#コラッツ予想に関する操作を表示する関数
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n +1
    
def length_collatz(n):
    length = 1
    while True:#無限レープ
        n = collatz(n)#コラッツ予想に関する操作して、新たなんいする
        length += 1#１回操作をするたびに、lengthの直を１だけを増やす
        if n == 1:
            break
    return length#　n＝＝１　になったときのlengthの直の出力


ans = 1
max_length = 1

for n in range (1,1001):
    if max_length < length_collatz(n):
        ans = n
        max_length = length_collatz(n)
print(ans)#
print(length_collatz(871))#結果を表示


# In[ ]:



