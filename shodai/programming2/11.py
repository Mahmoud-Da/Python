#!/usr/bin/env python
# coding: utf-8

# # 6. 授業課題

# ### 1. 文字列の format 機能を使い，適当な文章を表示させよ.

# In[7]:


a = "{} Rank" #フォーマットの定義
for i in ["first", "secund", "third","fourth","fifth" ]:# forループ 使用して
    print(a.format(i)) #結果を表示する


# ### 2. set 型のメソッドを 1 つ選び，使ってみよ(結果も表示させよ).

# In[9]:


S1 = {"Tokyo","Paris","Damascus","Istanbul","Bairut","Aleppo"} # S1 の定義
S1.add("Osaka") # S1 の要素に Osakaを追加
print(S1) #結果を表示する


# ### 3. for 文を使って，
# - 30 a
# - 28 b
# - 26 c
# - ...
# - 10 k
# 
# ### が表示されるプログラムを作成せよ（Hint: enumerate() や zip() を使うと簡単）．

# In[9]:


for nomber,alphabet in zip([30,28,26,"...",10], ["a", "b", "c","","k"]):
    print(nomber,alphabet) #結果を表示# zip() を使ったループ処理


# In[ ]:

