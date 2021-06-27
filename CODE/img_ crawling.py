from selenium import webdriver
from urllib.request import urlopen
from urllib.parse import quote_plus
from selenium.webdriver.common.keys import Keys
import os
import urllib.request
import json
import time
# 코드별 설명은 차후에 진행 예정

# 네이버 api 이용
def search_naver(search_name,save_path,start_index):
    print("naver start")
    client_id = "id"
    client_secret = "secret"
    encText = urllib.parse.quote(search_name)
    url = "https://openapi.naver.com/v1/search/image?query=" + encText

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        result = json.loads(response_body)
        img_list = result["items"]
        length = len(img_list)

    for i, img_list in enumerate(img_list):
        start = time.time()
        # print(img_list['link'])   # 저장 파일명 및 경로
        FileName = os.path.join(save_path, search_name + str(start_index + i) + ".jpg")
        print(str(i) + "/" + str(length) + ' ' + search_name + " 다운로드 중....... Download time : " + str(
            time.time() - start)[:5] + " 초")
        urllib.request.urlretrieve(img_list["link"], FileName)
        
    print(search_name + " ---다운로드 완료---")

def search_google(search_name,save_path) :
    print("google start")
    chromedriver = "C:/Users/ILIFO-104/PycharmProjects/YAYE_project/chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    driver.implicitly_wait(3)

    # 구글 이미지 검색 접속 및 검색어 입력
    driver.get("https://www.google.co.kr/imghp?hl=ko")

    Keyword = driver.find_element_by_xpath("//*[@id='sbtc']/div/div[2]/input")
    Keyword.send_keys(search_name)

    driver.find_element_by_xpath("//*[@id='sbtc']/button").click()

    # 스크롤
    elem = driver.find_element_by_tag_name("body")
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)

    try:
        driver.find_element_by_xpath("//*[@id='islmp']/div/div/div/div/div[3]/div[2]/input").click() # 현재 '검색 결과 더보기'의 xpath - 개발자 도구에서 확인
        for i in range(60):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
    except:
        pass

    # 이미지 개수
   links = []
    images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
    for i in range(1, len(images)):
        try:
            driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img').click()
            links.append(driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute('src'))
            driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[2]/a').click()
            print(keyword + ' 링크 수집 중..... number :' + str(i) + '/' + str(len(images)))
        except:
            continue

    # 이미지 다운로드
    forbidden = 0
       for k, i in enumerate(links):
        try:
            url = i
            start = time.time()
            urllib.request.urlretrieve(url, save_path + search_name + str(
                k + 1) + ".jpg")
            print(str(k + 1) + '/' + str(len(links)) + ' ' + search_name + " 다운로드 중....... Download time : " + str(
                time.time() - start)[:5] + " 초")
        except:
            forbidden += 1
            continue
        
    print(search_name + " ---다운로드 완료---")
    driver.close()
    return len(links)

# 폴더 생성
def make_folder(search_name):
    save_path = "C:/Users/ILIFO-104/Desktop/프로젝트/이미지 크롤링/" + search_name
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    save_path = save_path + "/"
    return save_path

if __name__ == "__main__":
    search_name = input("검색하고 싶은 키워드 : ")
    save_path = make_folder(search_name)
    start_index = search_google(search_name,save_path)
    #search_naver(search_name,save_path,start_index)
