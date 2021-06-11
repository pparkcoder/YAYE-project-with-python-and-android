from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
import os

def search_naver(search_name):
    # 구현 예정

def search_google(search_name, search_limit):
  
    # 폴더 만들기
    folder_name = "이미지가 저장될 폴더의 경로" + search_name
    if not os.path.exists(folder_name) :
        os.mkdir(folder_name)

    # url 설정
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    browser = webdriver.Chrome('chromedriver가 설치된 폴더의 경로')
    browser.get(search_url)

    image_count = len(browser.find_elements_by_tag_name("img"))

    browser.implicitly_wait(2)

    # 이미지 크롤링 + 폴더에 저장
    for i in range(search_limit):
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot(folder_name + "/" + search_name + str(i) + ".png")
    browser.close()


if __name__ == "__main__":
    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    search_google(search_name, search_limit)
    #search_naver(search_name)
