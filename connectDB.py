import MySQLdb

db = MySQLdb.connect(host="192.168.3.72",    # your host, usually localhost
                     user="root",         # your username
                     passwd="12345678",  # your password
                     db="mydb")        # name of the data base

cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS student (id Integer, name varchar(255));")
cur.execute("INSERT into student (id,name) VALUES ('1','jin');")
cur.execute("SELECT * FROM student")
for row in cur.fetchall():
    print(str(row[0])+row[1])

db.close()


# print('Enter your name:')
# x = input()
# print('Enter your id:')
# y = input()
# print('New student id: '+y+" name: "+x+" has been created!")
