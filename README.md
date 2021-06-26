# YAYE_project
딥러닝을 이용한 음식관련 프로젝트
<br><br>
## yoloV3 설치 및 실행과정 (순서 중요)
### 필자 환경
   - ### Windows 10 / Visual Studio 2015 / CUDA 10.1, cuDNN 7.6.3 / openCV 4.0.1 / compute capability 6.1
   - 자신이 필요로하는 환경이 없다면 ***동일하게 맞추길 권장하는 바***
<br><br>
1. Visual Studio 2015 다운
   - 2017, 2019 버전은 안되면 해결할 수는 있으나, 정신건강에 안좋으니 ***그냥 2015 다운***
<br><br>
2. NVIDI CUDA 10.1 설치
   - [설치링크](https://developer.nvidia.com/cuda-10.1-download-archive-base?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal)
   - ![1](https://user-images.githubusercontent.com/84856055/123502744-9abeef00-d689-11eb-8dc6-2f04a1e51c4b.JPG)
<br><br>
3. cuDNN 7.6.3 설치
   - 회원가입 필요
   - [설치링크](https://developer.nvidia.com/rdp/cudnn-archive)
   - ![1](https://user-images.githubusercontent.com/84856055/123502850-40725e00-d68a-11eb-8fea-9c1a0bd5b5f1.JPG)
<br><br>
4. openCV 4.0.1 설치
   - [설치링크](https://opencv.org/releases/)
<br><br>
5. Darknet 설치 및 환경 설정
   - [설치링크](https://github.com/AlexeyAB/darknet)
   - 압축 풀고, darknet-master -> build -> darknet 폴더에 **darknet.vcxproj 파일 수정 필요**
      - 오른쪽 마우스 클릭 -> 연결프로그램 -> 메모장
      - 2번째 line에 ToolsVersion="14.0" 으로 수정
      - ctrl + F -> $(VCTargetsPath)\BuildCustomizations\CUDA 10.0.props 검색 -> C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\extras\visual_studio_integration\MSBuildExtensions\CUDA 10.1.props 수정 (**자신의 경로 넣기**)
      - ctrl + F -> $(VCTargetsPath)\BuildCustomizations\CUDA 10.0.targets 검색 -> C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\extras\visual_studio_integration\MSBuildExtensions\CUDA 10.1.targets 수정 (**자신의 경로 넣기**)
      - 저장 후 Visual Studio 실행
<br><br>
6. Visual Studio 2015 환경 설정
    - darknet.sln 실행
    - 프로젝트 -> 속성 -> 구성 : Release, 플랫폼 : x64 설정
    - C/C++ -> 일반 -> 추가 포함 디렉토리 편집
    - openCV, CUDA, cuDNN 각 폴더에서 include 폴더 경로 넣어주기 (**자신의 경로 넣기**)
        - ![1](https://user-images.githubusercontent.com/84856055/123503153-1d48ae00-d68c-11eb-917b-c9cdbe42a8a9.JPG)
    <br><br>
    - CUDA C/C++ -> Device -> Core Generation 편집
    - **PC compute capability 확인 필수**
        - ![2](https://user-images.githubusercontent.com/84856055/123503154-1e79db00-d68c-11eb-8582-46bc79d8735c.JPG)
    <br><br>
    - 링커 -> 일반 -> 추가 라이브러리 디렉터리 편집
    - openCV, CUDA, cuDNN 각 폴더에서 lib + @ 폴더 경로 넣어주기 (**자신의 경로 넣기**)
        - ![3](https://user-images.githubusercontent.com/84856055/123503156-1fab0800-d68c-11eb-87d9-06b907e5ce2c.JPG)
<br><br>
7. 각종 파일 옮기기
    - opencv가 설치된 폴더 -> opencv -> build -> x64 -> vc14 -> bin 
      - ![1](https://user-images.githubusercontent.com/84856055/123503371-9c8ab180-d68d-11eb-8fd8-0c3768f85a50.JPG)
      - darknet-master -> bulid -> darknet -> x64로 위의 파일 옮겨주기
    - CUDA가 설치된 폴더 -> NVIDIA GPU Computing Toolkit -> CUDA -> v10.1 -> bin
      - ![2](https://user-images.githubusercontent.com/84856055/123503372-9dbbde80-d68d-11eb-96e6-e84e86e4ffc1.JPG)
      - darknet-master -> bulid -> darknet -> x64로 위의 파일 옮겨주기
    - cuDNN이 설치된 폴더 -> bin
      - ![3](https://user-images.githubusercontent.com/84856055/123503375-9e547500-d68d-11eb-8ab8-7923e604aeb6.JPG)
      - CUDA가 설치된 폴더 -> NVIDIA GPU Computing Toolkit -> CUDA -> v10.1 -> bin으로 위의 파일 옮겨주기
<br><br>
8. yolo3.weights 다운 (7번과 순서 바뀌어도 무관)
    - [다운받기](https://pjreddie.com/media/files/yolov3.weights)
    - darknet-master -> bulid -> darknet -> x64에 yolo3.weights 파일 옮겨주기
<br><br>
9. darknet.sln 실행 
  - ![build-success](https://user-images.githubusercontent.com/84856055/123503628-271fe080-d68f-11eb-90fd-d4b6c7e38690.JPG)
  - 위의 사진처럼 나왔다면 성공
  - darknet-master -> bulid -> darknet -> x64에 darknet.exe 파일 생성
<br><br>
10. TEST
  - darknet-master -> bulid -> darknet -> x64
  - darknet_yolo_v3.cmd 실행
  - ![yolov3_test](https://user-images.githubusercontent.com/84856055/123503629-28510d80-d68f-11eb-89e2-ba680201f85e.JPG)
  - 위의 사진처럼 나왔다면 성공
<br><br>
11. 학습시키기 - 추가 예정
