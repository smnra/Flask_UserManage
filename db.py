# coding = utf-8
import pymysql as MySQLdb
conn = MySQLdb.connect(host = '192.168.3.74',
                       port = 50014,
                       user = 'root',
                       password = '10300',
                       database = 'temp'
                       )
cur = conn.cursor()

def addUser(username,password):
    sql = 'insert into user (username,password) values ("%s","%s")' % (username,password)
    cur.execute(sql)
    conn.commit()
    conn.close()