import mysql.connector as sqltor
jebin = sqltor.connect(host='localhost',user = 'root', passwd = 'mysql', database='vaccination')
if jebin.is_connected()== False:
    print("Failed")
if jebin.is_connected() == True:
    print("Success")
cursor = jebin.cursor()
cursor.execute("select* from details")
data = cursor.fetchall()
count = cursor.rowcount
for i in data:
    print(i)
    print(count)

