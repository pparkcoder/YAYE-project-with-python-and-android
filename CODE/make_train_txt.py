# yolo 학습 시 train.txt 파일 만드는 코드
# # /train_data/img\a.jpg 생성 -> # /train_data/img/a.jpg 변경

import glob
filenames = []
files = sorted(glob.glob("./train_data/img/*.jpg"))
f = open("./train.txt",'a')
for i in range(len(files)) :
    f.write(files[i].lstrip('./') +'\n')
f.close()
# /train_data/img\a.jpg

txt = open('train.txt','r')
f = open('train2.txt','w') 
while True : 
    line = txt.readline() 
    if not line: 
        break 
    temp = line.replace('\\','/')
    f.write(temp) 
txt.close()
f.close()
# /train_data/img/a.jpg
