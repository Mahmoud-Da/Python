from sklearn import datasets, svm
import matplotlib.pyplot as plt
import cv2

digits = datasets.load_digits()
x = digits.images
y = digits.target
x = x.reshape((-1, 64)) 

def predict_digit(filename):
  my_img = cv2.imread(filename)
  my_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)
  my_img = cv2.resize(my_img, (8, 8))
  my_img = 15 - my_img // 16 
  plt.imshow(my_img, cmap="gray")
  my_img = my_img.reshape((-1, 64))
  res = clf.predict(my_img)
  plt.show()
  return res[0]

n = predict_digit("Mahmoud6.png")
print("Mahmoud6.png = " + str(n))
