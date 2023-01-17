#!/usr/bin/env python
# coding: utf-8

# # 期末レポート課題

# ### 1.
# 逆に並べても元の数になる数を「回文数」と呼ぶ. 
# 
# 回文数の例：1,2,3,...,9, 11,22,...,99,101,...
# 
# n = 1〜10000 の中で回文数であるものの個数を数え，表示させよ
# 

# In[46]:


n1 = 0#数字代入
n1_list = []#リスト作成

for i in range (1,10000+1):#forループ
    if str(i) == str(i)[::-1]:#条件
        n1 += 1#n1をまとめ
        n1_list += [i]#数字はリストに
    else:#その他
        continue#継続
print(n1_list)#結果を表示


# In[47]:


print(n1)#結果を表示


# ### 2. adjacent.txt に記録されている数について「隣接する n 桁の積の最大値」が最も大きくなる n を求めよ．

# In[11]:


import functools#インポートする
import operator#インポートする
f = open ("adjacent.txt", "r", encoding="utf-8")#ファイルを開く
h = f.read()#ファイルを読む
number = 1#変数代入
max_number = 0#変数代入
for i in range (0,1000):#forルーブルを使用
    if h[i]  != "0":#0じゃなかったら
        number *= int(h[i])
    else:#その他
        if number > max_number:
            max_number = number
        number = 1
print(len(str(max_number)))#結果を表示


# In[ ]:



