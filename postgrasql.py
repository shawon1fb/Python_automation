import psycopg2

print("start")
try:
    con = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="1516")
except Exception as e:
    print(e)

# cursor
print("con")
print(con)
cur = con.cursor()
print("ok")
print('PostgreSQL database version:')
cur.execute('select * from information_schema.tables')
db_version = cur.fetchone()
print(db_version)
