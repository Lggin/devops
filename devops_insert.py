import pymysql

conn = pymysql.connect(
    host="localhost",    #MySql 서버 주소
    user = 'root',
    password='1234',
    database = "exampledb",
    charset = 'utf8mb4',
    cursorclass=pymysql.cursors.DictCursor

)

cursor = conn.cursor()

cursor.execute("INSERT INTO employees(name, department, salary) VALUES('이강인', '축구부', 9000)")
print("현제 데이터베이스 :", cursor.fetchone())

conn.close()