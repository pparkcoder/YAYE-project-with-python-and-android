from selenium import webdriver
from urllib.request import urlopen
from urllib.parse import quote_plus
from selenium.webdriver.common.keys import Keys # 추가
import os
import urllib.request
import json  
import time # 추가

# 코드별 설명은 차후에 진행 예정

def search_naver(search_name):  # 네이버 api 이용

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
    if not os.path.exists(savePath):
        os.mkdir(savePath)

    # url 설정
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    browser = webdriver.Chrome('chromedriver가 설치된 폴더의 경로/chromedriver.exe')
    browser.get(search_url)

    image_count = len(browser.find_elements_by_tag_name("img"))

    browser.implicitly_wait(2)

    # 이미지 크롤링 + 폴더에 저장
    for i in range(search_limit):
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot(savePath + "/" + search_name + str(i) + ".png")
    browser.close()

def search_google2(search_name) :
    chromedriver = 'chromedriver가 설치된 폴더의 경로/chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    driver.implicitly_wait(3)
    
    # 구글 이미지 검색 접속 및 검색어 입력
    driver.get('https://www.google.co.kr/imghp?hl=ko')

    Keyword = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
    Keyword.send_keys(search_name)

    driver.find_element_by_xpath('//*[@id="sbtc"]/button').click()

    # 스크롤
    elem = driver.find_element_by_tag_name("body")
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)

    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[3]/div[2]/input').click() # 현재 '검색 결과 더보기'의 xpath - 개발자 도구에서 확인
        for i in range(60):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
    except:
        pass

    # 이미지 개수
    links = []
    images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
    for image in images:
        if image.get_attribute('src') != None:
            links.append(image.get_attribute('src'))

    print(search_name + ' 찾은 이미지 개수:', len(links))
    time.sleep(2)

    # 이미지 다운로드
    for k, i in enumerate(links):
        url = i
        start = time.time()
        urllib.request.urlretrieve(url, "이미지가 저장될 폴더의 경로/" + search_name + "/" + search_name + str(k) + ".jpg")
        print(str(k + 1) + '/' + str(len(links)) + ' ' + search_name + ' 다운로드 중....... Download time : ' + str(time.time() - start)[:5] + ' 초')
    print(search_name + ' ---다운로드 완료---')

    driver.close()

if __name__ == "__main__":
    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    search_google(search_name, search_limit)
    search_google2(search_name)
    search_naver(search_name)
