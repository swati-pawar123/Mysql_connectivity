import mysql.connector
mydb=mysql.connector.connect(host='localhost',username='root',passwd='root',database='account')
mycursor=mydb.cursor()
'''
mycursor.execute('show databases')
for i in mycursor:
        print(i)
'''

'''
mycursor.execute('select * from customers')
result = mycursor.fetchall()
for i in result:
    print(i)
'''
'''
mycursor.execute('select name from customers')
result = mycursor.fetchall()
for i in result:
    print(i)
'''
'''
mycursor.execute('select * from customers WHERE name = "swati"')
result = mycursor.fetchall()
for i in result:
    print(i)
'''
mycursor.execute("INSERT into customers values('aniket','aurangabad')")
mycursor.execute('select * from customers')
result = mycursor.fetchall()
for i in result:
    print(i)