import pymysql 

#1. MariaDB 연결 : 연결자변수 = pymysql.connect(연결옵션)
#2. 커서 생성 : 커서변수 = 연결자변수.cursor()
#3. SQL문 실행 : 커서변수.execute("쿼리문")
#4. 데이터 저장 : 연결자변수.commit()
#5. MariaDB 연결종료 : 연결자변수.close()

if __name__ == '__main__' :
    # 연결
    conn = pymysql.connect(host='IP',user='ID',password='PS',db='DB 명',charset='utf8') 
    # 커서 생성
    cur = conn.cursor() 
    # 실행
    sql = "create table if not exists testTable (carbohydrate int, protein int,carb int)"   
    cur.execute(sql)
    # 저장
    conn.commit()
    # 종료
    conn.close()
