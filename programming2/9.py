#!/usr/bin/env python
# coding: utf-8

# # 9. 授業課題

# ### 1. 以下の値を求め,画面に表示させるプログラムを作成せよ:
# 
# $$\frac{\sqrt{e}}{\pi^{3}}$$
# 

# In[63]:


import math # math モジュールをインポート
a= math.pi # 円周率 π の近似値を表示
b=math.e # 自然対数の底 e の近似値を表示
c=math.sqrt(b) # πの3畳を表示
d=math.pow(a, 3)
print(c//d)#結果を表示


# ### 2. どの目も同じ確率で出るサイコロを表す関数 dice() を定義し，
# ### そのサイコロを 1000 回振ったときに出る目の平均値を計算せよ．

# In[67]:


import random #random モジュールをインポート
m = 0
def dice(m): #定義
    m = [1 ,2 ,3 ,4 ,5 ,6 ]#m(サイコロ)のリスト
    return random.choice(m)#引数に渡したシーケンスをシャッフル
n = 0
for cnt in range (1000):#forループ使用
    n += dice(m)
print(n/1000)#結果を表示
    


# In[ ]:



