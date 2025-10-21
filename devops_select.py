import pymysql

conn = pymysql.connect(
    host="localhost",    #MySql 서버 주소
    user = 'root',
    password='1234',
    database = "exampledb",

)

cursor = conn.cursor()

sql = "INSERT INTO employees(name, department, salary) VALUES('이강인', '축구부', 9000)"
cursor.execute(sql)
conn.commit()


conn.close()