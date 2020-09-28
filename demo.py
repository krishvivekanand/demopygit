import mysql.connector
#mydb = mysql.connector.connect(host="localhost", user="root",passwd="root")
mydb = mysql.connector.connect(host="localhost", user="root",passwd="root",database="telusko")
mycursor = mydb.cursor()
#mycursor.execute("show databases")
mycursor.execute("select * from student")
#result = mycursor.fetchall()
result = mycursor.fetchone()
print(result)
# for i in mycursor:
#     print(i)
for i in result:
    print(i)