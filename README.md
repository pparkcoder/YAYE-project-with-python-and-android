# YAYE (You Are what You Eat)
### [yoloV5](https://lv99.tistory.com/69)를 활용한 음식 object detection 관련 project
---------------------------------------------------------------------------------------
### 1. 구성도
![1](https://user-images.githubusercontent.com/84856055/124592620-9c15c600-de98-11eb-82c7-c136975dee51.JPG)
<br><br>
### 2. 기능 정의
- 사용자가 찍은 사진을 통해 음식 object detection 수행
- 분류한 음식의 칼로리 및 3대 영양소 등을 분석
- 다음 식사에 부족한 칼로리 및 영양소를 채울 수 있는 음식 추천 (아침 점심 저녁 비율 = 2 : 5 : 3 **임의로 설정**)
- GPS를 기반으로 해당 음식을 판매하는 식당 제공
- 음식의 조리법이 담긴 youtube 링크 제공
- 음식을 구매할 수 있는 NAVER 쇼핑 링크 제공 (**리뷰 많은 순** 으로 제공)
<br><br>
### 3. 학습 과정
- batch_size와 epoch를 조절
- **최종적으로 epoch 100 선택**
- bacth_size와 epoch에 따른 precision-recall 그래프
![2](https://user-images.githubusercontent.com/84856055/124592626-9d46f300-de98-11eb-9e21-4b1c0cda5db6.JPG)
<br><br>
### 4. 학습 결과
- epoch 10
![3](https://user-images.githubusercontent.com/84856055/124592627-9ddf8980-de98-11eb-83df-2730457838fe.JPG)
- epoch 100
![4](https://user-images.githubusercontent.com/84856055/124592628-9ddf8980-de98-11eb-9d0f-14449dc059f4.JPG)
<br><br>
### 5. UI/UX
![5](https://user-images.githubusercontent.com/84856055/124593891-21e64100-de9a-11eb-97bd-7bcf75bcef09.JPG)
<br><br>
### 6. 기술 스탯
![6](https://user-images.githubusercontent.com/84856055/124594025-47734a80-de9a-11eb-9b55-57c923728c30.JPG)
### 7. 차후 방향
Android app 을 사용하여 스마트폰 환경에서 이용할 수 있도록 구축 예정
