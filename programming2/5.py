#!/usr/bin/env python
# coding: utf-8

# # 5. 授業課題

# ### 1. 
# - x を入力したときに，西暦 x 年が
# 
#         うるう年ならば True を返し，
#         うるう年でなければ False を返す
# 
#   ような関数 is_leapyear(x) を作れ.
# - 西暦 1 年から西暦 2000 年におけるうるう年の回数を数え，その回数を表示させよ.

# In[5]:


def is_leapyear(x):  # 関数の定義
    if x %4 == 0:  # 4で割り切れるときはうるう年
        if x % 100 == 0 and x % 400 !=0: # 100で割り切れて、400で割り切れない場合はうるう年ではない
            return False  #Falseを返し
        elif x % 100 == 0 and x % 400 ==0:  # 100で割り切れて、400で割り切れる場合はうるう年
            return True　#True 返し
        else:                             # 4で割り切れて、100で割り切れない場合はうるう年
            return True#True 返し
    else:
        return False　#Falseを返し
results_number = 0    
for x in range (1,2000):        # 1が第一,2000が第2
    if is_leapyear(x) == True: 　   
        result+=1
    else:
        pass　　　　　　#何も実行しない
print(result)  # 結果表示
    

        
    


# ### 2. 正の整数 n を引数にしたときに,
# - n が素数ならば True を返し,
# - n が素数でなければ False を返す ような関数 isprime(n) を作成し,
# 
# n に自分の学籍番号を代入した結果を表示させるプログラムを作成せよ．

# In[6]:


def is_prime(n): #関数の定義
    for k in range(2, n): #nの値をいれる
        if n % k == 0:#n素数じゃなかったら
            return False#falseを返し
        else:#以外
            continue# 判断せずに次の数値へ継続
    return True # Trueを返し
print(is_prime(5)) #   表示結果


# ### 3. 以下を求めるプログラムを作成し，結果を表示させよ．
# - 2 から 10000 までの数の間で素数であるものが何個あるか数えよ．
# - 2 から 10000 までの数の間で素数であるものの総和を求めよ．

# In[82]:


def isprime(n): # 関数の定義
    for i in range (2,n): #nの値をいれる
        if n % i ==0:  #n素数じゃなかったら
            return False #falseを返し
        else:  #以外
            continue # 判断せずに次の数値へ継続
    return True #　Trueを返し
v = 0 #v 変数に0を代入
vnumber = 0　#vnumber 変数に0を代入
for  pnumber in range (2,10000): #2が第一,10000が第2
    if isprime(pnumber) == True: #if pnumber がtrueなら
        vnumber = vnumber + pnumber#vnumber+pnmberを足す
for p in range (2,10000):#2が第一,10000が第2
    if isprime(p) == True: #　Trueを返し
         v += 1
print(v) #   表示結果
print(vnumber)#   表示結果


# In[ ]:



