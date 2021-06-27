## yolo mark 설치 및 실행과정
### yolo mark는 이미지 파일에 직접 Bounding Box를 그려줌으로써 Box의 좌표를 도출해 주는 도구
선행과정 : ***Visual Studio 2015, openCV 4.0.1 이 설치되어 있어야 함*** ([참고](https://github.com/pparkcoder/YAYE_project))
<br>
#### 안되는 경우, 3번 4번 꼼꼼하게 확인 후 다시 진행
1. yolo mark 다운
    - [설치 링크](https://github.com/AlexeyAB/Yolo_mark)
<br><br>
2. yolo mark 실행
    - 설치된 경로 -> Yolo_maker_master -> yolo_mark.sln 실행
<br><br>
3. Visual Studio 2015 환경 설정
    - 프로젝트 -> 속성 -> 구성 : Release, 플랫폼 : x64 설정
    - C/C++ -> 일반 -> 추가 포함 디렉토리 편집
    - openCV 폴더에서 include 폴더 경로 넣어주기 (**자신의 경로 넣기**)
        - ![1](https://user-images.githubusercontent.com/84856055/123503153-1d48ae00-d68c-11eb-917b-c9cdbe42a8a9.JPG) 
    <br><br>
    - 링커 -> 일반 -> 추가 라이브러리 디렉터리 편집
    - openCV 폴더에서 lib + @ 폴더 경로 넣어주기 (**자신의 경로 넣기**)
        - ![3](https://user-images.githubusercontent.com/84856055/123503156-1fab0800-d68c-11eb-87d9-06b907e5ce2c.JPG)
<br><br>
4. 각종 파일 옮기기
    - opencv가 설치된 폴더 -> opencv -> build -> x64 -> vc14 -> bin
    - **opencv_world401.dll** 파일 복사
    - 설치된 경로 -> Yolo_maker_master -> x64 -> (Debug,Release) -> 두 폴더에 **opencv_world401.dll** 넣어주기
5. yolo_mark.sln 실행
    - ![1](https://user-images.githubusercontent.com/84856055/123543155-320a6c00-d788-11eb-9e5f-770f863f9964.JPG)
    - 설치된 경로 -> Yolo_maker_master -> x64 -> Release -> yolo_mark.cmd 파일 생성
6. yolo_mark.cmd 실행
    - ![2](https://user-images.githubusercontent.com/84856055/123543156-333b9900-d788-11eb-91b0-2047f5f87f1d.JPG)
    - 위와 같이 창이 뜬다면 빌드 성공
