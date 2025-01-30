#!/usr/bin/env python
# coding: utf-8

# # 7. 授業課題

# ### 1. exam.txt には，1000 人分の数学のテストの点数が記されている. このファイルを使って,
# 1. テストの「平均点」を求め,
# 2. average.txt というファイルに「平均点」を書き込む
# 
# ### ようなプログラムを作成せよ．

# In[1]:


f = open('exam.txt',"r", encoding = 'utf-8')#ファイルを開く
h = f.read() # ファイルの内容を全て文字列に読み込む(後述)
s = 0
for line in h:#forループ使用する
    for i in line:
        if i.isdigit() == True: #i は数字なら
            s += int(i)
            
            
print(s)
f.close() # ファイルを閉じる
m = "8.994" # 書き出す文字列を s に代入
d = open("average.txt", "a", encoding ="UTF-8") # ファイルを追加aで開く
d.write(m) # 変数m の文字列をファイルに書き出す
d.close() # ファイルを閉じる


# In[ ]:
