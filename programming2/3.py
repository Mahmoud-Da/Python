#!/usr/bin/env python
# coding: utf-8

# # 中間レポート課題

# ### 1.
# フィボナッチ数列の項の内，
# 偶数かつ 1000 未満 の項を全て足した値を求め，表示させよ

# In[16]:


def fib(n):#関数の定義
    one, two = 0, 1#変数を作成
    if n == 1:#nが1だった場合
        return one#変数を返し
    elif n == 2:#変数を返し
        return two#nが2だった場合
    else:#さっきの条件満たさないとその代わりに
        for i in range (n-2):#forループ使用
            one, two = two, one + two#変数に代入した直を入れ替えて、計算する
        return two#変数を返し
fibs = []#リストを作成する
for n in range (1,18):#forループ使用
    if fib(n) % 2 == 0:#偶数だったら
        fibs += [fib(n)]
print(sum(fibs))#結果を表示     


# ### 2.
# 5 番目のメルセンヌ素数をプログラミングにより求め，表示させよ.
#      

# In[15]:


from sympy import isprime#モジュールsympyとインポートisprime
a = 2#変数aに代入する
result = []#リストを作成する
while len(result) < 5:#whileループ使用する
    b = 2 ** a - 1#式を代入する
    if isprime(b):#偶数だったら
        result.append(b)#リストに一つずつを追加する
    a += 1#aは一つずつ増やす
        
print (result[-1])#結果を表示


#  ### 3.
# adjacent.txt には 1000 桁の数が 1 個記録されている.
# 
# この数の隣接する 4 桁の数の積の最大値は 9×9×8×9 = 5832である.
# 
# さて，adjacent.txt に記録されている数について，
# 隣接する 13 桁の積の最大値を求めよ.
# 

# In[14]:


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
# 1 以上 1, 000, 000 以下の初期値 n の内，
# 
# コラッツ予想に関する操作を繰り返して，1 になるまでの数列の長さが
# 
# 最大になる n を求め，表示させよ.

# In[ ]:


list_m = [] #リスト作成する
def collaz(a): #関数の作成する
    cnt = 0 #変数cntに０を代入する
    collaz_number = a #変数collaz_numberに代入する
    while collaz_number != 1: #１ではないとき
        if collaz_number % 2 == 1: #奇数だったら
            collaz_number = collaz_number * 3 +1 #コラッツの偶数時
            cnt += 1 #稼働したら、+1  する  
        else: #それ以外
            collaz_number //= 2 #コラッツの偶数時の
            cnt += 1 #式を稼働した場合、回数を１足す
    return a, cnt #変数aと変数cntを返す（１になった時）
for t in range(2, 1000): #繰り返する
    total = collaz(t) #変数totalに代入する
    if total[1] > 177: #繰り返しが177以上を表示
        list_m.append(collaz(t)) #値を追加
m_count = max(1,len(list_m)) #最大値を表示
for d in range(m_count): #変数を繰り返す
    print(list_m[d]) #結果を表示　一つ目にaを表示　二つ目に回数を表示
    
###先生へ（1000000が大きい数字で実行するとjupyterが反応してくれませんのでエラーメッセージが出てるかどうか分かりません）
####　なお：PDFと同じ形で1000に変えていました


# In[ ]:



