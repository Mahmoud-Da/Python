#!/usr/bin/env python
# coding: utf-8

# # 10. 授業課題

# exam.csv について，以下の処理を行うプログラムを作成せよ:
# 1. 数学の点数を $x$ 軸に，理科の点数を $y$ 軸に描画した散布図を作成
# 2. 各点数の平均点・中央値・分散・標準偏差を求め，各統計量の棒グラフを作成
# 3. 各点数のヒストグラムを作成

# In[32]:


import pandas as pd# pandasをpdという名前で読み込む4
exam_data = pd.read_csv("exam.csv")#pandasのread_csv メソッドを利用して読込
print(exam_data.head(5))#最初の5 行を表示
print(exam_data["math"])#PetalLength の列だけ表示
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt#matplotlib 内のpyplot モジュールをplt としてインポート
plt.plot(exam_data["math"], exam_data["science"], "o")# 花弁のデータをプロット
plt.xlabel("math") # x 軸にラベル名をつける
plt.ylabel("science") # y 軸にラベル名をつける
exam_mean = exam_data.mean()# mean()で各列の平均値を計算
print(exam_mean)#結果を表示
exam_median = exam_data.median()# median()で各列の中央値を計算
print(exam_median)# 結果を表示
exam_var, exam_std = exam_data.var(), exam_data.std()# var(),std() で各列の分散・標準偏差を計算
print(exam_var, exam_std) # 結果を表示
exam_mean.plot(kind="bar", rot=45)
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt # pyplotをplt としてインポート
import pandas as pd # pandas をpd としてインポート
import numpy as np # numpy をnp としてインポート
dat = pd.read_csv("exam.csv")
dat.head(10)
x= dat["math"]
y = dat["science"]
plt.plot(x, y, "o") # plt.plot() で散布図を描画
plt.xlim(0, 100) # x の範囲を指定
plt.ylim(0, 100) # y の範囲を指定
plt.xlabel("math") # x のラベルを設定
plt.ylabel("science") # y のラベルを設定
plt.show()
exam_mean.plot(kind="bar", rot=100)#棒グラフ
exam_data.hist()#ヒストグラム


# アヤメデータ iris.csv における
# - Petal Length を x 軸,
# - Petal Width を y 軸 
# 
# 
# にとり,
# 1. 散布図を描け.
# 2. 相関係数 Cor(x, y) を求め,画面に表示させよ.
# 3. 最小二乗法で単回帰分析をせよ(回帰直線を求め,散布図と併せて 描画せよ).

# In[43]:


import pandas as pd # pandas をpd という名前で読み込む4
iris_data = pd.read_csv("iris.csv") # pandasのread_csv メソッドを利用して読込
print(iris_data.head(5)) # 最初の5 行を表示
print(iris_data["Petal Length"]) # PetalLength の列だけ表示
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt #matplotlib 内のpyplot モジュールをplt としてインポート
plt.plot(iris_data["Petal Length"], iris_data["Petal Width"], "o")# 花弁のデータをプロット
plt.xlabel("Petal Length") # x 軸にラベル名をつける
plt.ylabel("Petal Width") # y 軸にラベル名をつける
corrcoef = np.corrcoef(x,y)#相関係数の計算
print(corrcoef)#結果を表示
from sklearn import linear_model#scikit-learn を用いた最小二乗法
model = linear_model.LinearRegression()
model.fit(x[:, np.newaxis], y)
print(model.coef_, model.intercept_)


# In[ ]:



