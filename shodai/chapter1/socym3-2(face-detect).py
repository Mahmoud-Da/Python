import matplotlib. pyplot as plt 
import cv2 
# カスケードファイルを指定して検出器を作成 
cascade_file = "haarcascade_frontalface_alt.xml" 
cascade = cv2. CascadeClassifier (cascade_file) 
# 画像を読み込んでグレイスケールに変換する
img = cv2. imread ("dodo.jpg") 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# 顔認識を実行 
face_list = cascade. detectMultiScale(img_gray, minSize=(150,150))
# 結果確認 
if len(face_list) == 0: 
    print("失敗") 
    quit() 
# 認識した部分に印をつける 
for (x, y, w, h) in face_list: 
    print("顔の座標=", x, y, w, h) 
    red = (0, 0, 255) 
    cv2.rectangle(img, (x, y), (x+w, y+h), red, thickness=10) 
#画像出力 
cv2. imwrite("face-detect.png", img) 
plt. imshow (cv2. cvtColor (img, cv2. COLOR_BGR2RGB)) 
plt. show() 
