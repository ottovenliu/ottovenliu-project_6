import mysql.connector

mydb = mysql.connector.Connect(
    host="localhost",
    user="user",
    password="lf187935",
    database="website"
)
# print(mydb)
text = "小蓮花"
mycursor = mydb.cursor()
#sql = "SELECT * FROM user WHERE name='{}'" .format(text)
sql = "SELECT * FROM user"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(myresult[0][2])
print(myresult[0])
print(myresult)
print("------------------分界線1--------------------")
print(type(myresult))

# if myresult[1][2] == text:
#     print(myresult[1][1])
userdatainfo = list(myresult[0])
print(userdatainfo)
print("------------------分界線2--------------------")
userDataTable = []
userDataBox = []
for i in myresult:
    for j in myresult:
        userDataBox.append(j)
    userDataTable.append(userDataBox)

print(userDataBox)

# for i in myresult:
#     a = myresult[i]
#     list(a)
#     # userdatainfo = list(myresult[0])
#     userDataBox.append(a)
#     print(userDataBox)
# if text == myresult[i][2]:
#     print(myresult[i][1])
