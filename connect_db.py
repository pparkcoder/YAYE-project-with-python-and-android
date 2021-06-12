import pymysql 
import pandas as pd

#1. MariaDB 연결 : 연결자변수 = pymysql.connect(연결옵션)
#2. 커서 생성 : 커서변수 = 연결자변수.cursor()
#3. SQL문 실행 : 커서변수.execute("쿼리문")
#4. 데이터 저장 : 연결자변수.commit()
#5. MariaDB 연결종료 : 연결자변수.close()

def data_preprocessing() :
    # 전처리 함수 구현 예정
    
def data_select() :
    '''
    음식 분류를 통해 각 음식에 대한 영양정보를 select
    후에, 부족한 칼로리 및 영양소를 계산한 뒤
    다시 db에 접근하여 필요한 음식을 return -> 필요한 음식의 우선순위를 어떻게 둘지 고민이 필요
    ```
    
def data_insert() :# 전처리 된 데이터 db에 insert 하는 함수
    data = pd.read_excel("food_db.xlsx")
    length = data.shape[0]
    
    sql = "create table if not exists food_db (name varchar(10),kcal float,protein float,carb float,carbohydrate float)" # 음식이름, 칼로리, 단백질, 지방, 탄수화물
    
    cur.execute(sql)

    for i in range(length):
        sql = "insert into food_db(name, kcal, protein, carb, carbohydrate) values (%s, %s, %s, %s, %s)"
        cur.execute(sql, (data['식품명'][i], data['에너지(kcal)'][i], data['단백질(g)'][i], data['지방(g)'], data['탄수화물(g)']))

if __name__ == '__main__' :
    conn = pymysql.connect(host='IP',user='ID',password='PS',db='DB 명',charset='utf8') # 연결
    cur = conn.cursor() # 커서 생성
    # cur.execute("set names utf8") - 한글이 안되는 경우
    
    # 음식의 개수 만큼 select 문 실행 
    
    conn.commit() # 저장
    conn.close() # 종료
