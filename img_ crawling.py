from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
import os
import urllib.request # 추가
import json # 추가

# 어찌어찌 하다 되었기에 일단 저장..정리는 나중에..

def search_naver(search_name):  #네이버 api 이용

    client_id = "네이버 api id"
    client_secret = "네이버 api ps"
    encText = urllib.parse.quote(search_name)
    url = "https://openapi.naver.com/v1/search/image?query=" + encText

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    # 이미지 저장 경로
    savePath = "이미지가 저장될 폴더의 경로/" + search_name
    if (rescode == 200):
        response_body = response.read()
        result = json.loads(response_body)
        img_list = result['items']

    for i, img_list in enumerate(img_list, 1):
        # 이미지링크 확인
        print(img_list['link'])

        # 저장 파일명 및 경로
        FileName = os.path.join(savePath, search_name + str(i) + '.jpg')

        # 파일명 출력
        print('full name : {}'.format(FileName))

        # 이미지 다운로드 URL 요청
        urllib.request.urlretrieve(img_list['link'], FileName)

def search_google(search_name, search_limit):
  
    # 폴더 만들기
    savePath = "이미지가 저장될 폴더의 경로" + search_name
    if not os.path.exists(savePath) :
        os.mkdir(savePath)

    # url 설정
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    browser = webdriver.Chrome('chromedriver가 설치된 폴더의 경로')
    browser.get(search_url)

    image_count = len(browser.find_elements_by_tag_name("img"))

    browser.implicitly_wait(2)

    # 이미지 크롤링 + 폴더에 저장
    for i in range(search_limit):
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot(savePath + "/" + search_name + str(i) + ".png")
    browser.close()


if __name__ == "__main__":
    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    search_google(search_name, search_limit)
    search_naver(search_name)
