# yolo 학습 시 train.txt 파일 만드는 코드

f = open('./label/train.txt', 'r')

while True:
    data = f.readline()

    if not data:
        break

    print('data/custom/images/'+data.strip('\n')+'.jpg')

f.close()
