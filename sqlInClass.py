import mysql.connector

mydb = mysql.connector.Connect(
    host="localhost",
    user="user",
    password="lf187935",
    database="website"
)
# print(mydb)
mycursor = mydb.cursor()
#sql = "SELECT * FROM user WHERE name='{}'" .format(text)
sql = "SELECT * FROM user"
mycursor.execute(sql)
myresult = mycursor.fetchall()
# print(myresult[0][2])
# print(myresult[0])
# print(myresult)
print("------------------分界線1--------------------")
# print(type(myresult))

# if myresult[1][2] == text:
#     print(myresult[1][1])
# userdatainfo = list(myresult[0])
# print(userdatainfo)
print("------------------分界線2--------------------")
# for i in myresult:
#     a = myresult[i]
#     list(a)
#     # userdatainfo = list(myresult[0])
#     userDataBox.append(a)
#     print(userDataBox)
# if text == myresult[i][2]:
#     print(myresult[i][1])
userDataTable = []
userDataBox = []
for i in myresult:
    userDataBox.append(i[2])
print("------------------分界線3--------------------")
name = "謝瑞蓮"
username = "小蓮花"
password = "456"
if username in userDataBox:
    pId = userDataBox.index(username)
    if password == myresult[pId][3]:
        print(myresult[pId][1])
    else:
        print("密碼不對")
else:
    print("沒有這個使用者")
print("------------------分界線4--------------------")


def chack(username, password):
    userDataBox = []
    for i in myresult:
        userDataBox.append(i[2])

    if username in userDataBox:
        pId = userDataBox.index(username)
        if password == myresult[pId][3]:
            print(myresult[pId][1])
        else:
            print("密碼不對")
    else:
        print("沒有這個使用者")
