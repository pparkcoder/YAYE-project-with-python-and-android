from selenium import webdriver
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import requests
import os
import urllib.request
import time
import pymysql

def link_crawling(search_name):
    encText = urllib.parse.quote(search_name) # incoding

    # 리뷰순
    url = 'https://search.shopping.naver.com/search/all?origQuery=%EC%82%AC%EA%B3%BC&pagingIndex=1&pagingSize=40&productSet=total&query=' + encText + '&sort=review&timestamp=&viewType=list'

    # 랭킹순
    # url = "https://search.shopping.naver.com/search/all?query=" + encText

    # 유튜브 링크
    youtube_url = 'https://www.youtube.com/results?search_query=' + encText

    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    cnt = len(soup.find_all('div', class_='basicList_title__3P9Q7'))

    # 사용자에게 보여질 link 목록
    shopping_link = []

    for i in range(0, cnt):
        show = {}
        metadata = soup.find_all('div', class_='basicList_title__3P9Q7')[i]
        title = metadata.a.get('title')
        print("<제품명> : ", title)  # title

        price = soup.find_all('span', class_='price_num__2WUXn')[i].text
        print("<가격> : ", price)  # 가격

        url = metadata.a.get('href')
        print("<url> : ", url)  # url
        shopping_link.append(url)
        print("===================================================")

        show = {'제품명': title, '가격': price, 'url': url}

    # 검색한 음식 상품 리스트
    print(shopping_link)

    # 검색한 음식 조리법 유튜브 링크
    print(youtube_url)

def data_select():
    '''
    음식 분류를 통해 각 음식에 대한 영양정보를 select
    후에, 부족한 칼로리 및 영양소를 계산한 뒤
    다시 db에 접근하여 필요한 음식을 return -> 필요한 음식의 우선순위를 어떻게 둘지 고민이 필요
    여기에서 음식을 return 하면서 해당 음식의 쇼핑주소와, 유튜브 링크를 제공 - link_crawling 호출
    '''

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
    for image in images:
        if image.get_attribute("src") != None:
            links.append(image.get_attribute("src"))
    time.sleep(2)

    # 이미지 다운로드
    for k, i in enumerate(links):
        url = i
        start = time.time()
        urllib.request.urlretrieve(url, save_path + search_name + str(
            k + 1) + ".jpg")
        print(str(k + 1) + '/' + str(len(links)) + ' ' + search_name + " 다운로드 중....... Download time : " + str(
            time.time() - start)[:5] + " 초")
    print(search_name + " ---다운로드 완료---")
    driver.close()
    return len(links)

def make_folder(search_name):
    save_path = "C:/Users/ILIFO-104/Desktop/프로젝트/이미지 크롤링/" + search_name
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    save_path = save_path + "/"
    return save_path
    
if __name__ == "__main__":
    '''학습을 위한 이미지 데이터 구축 - 실제 프로그램에는 구현되지 않는 부분
    search_name = input("검색하고 싶은 키워드 : ")
    save_path = make_folder(search_name)
    search_google(search_name,save_path)
    '''
    
    ''' 음식분류를 통해 필요한 영양소 등 계산 후 음식 구매가능 링크, 조리법 유튜브 영상 제공    
    conn = pymysql.connect(host='IP', user='ID', password='PS', db='DB 명', charset='utf8')  # 연결
    cur = conn.cursor()  # 커서 생성
    필요한 과정 진행
    conn.commit()  # 저장
    conn.close() # 종료
    '''
