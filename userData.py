import mysql.connector

mydb = mysql.connector.Connect(
    host="localhost",
    user="user",
    password="lf187935",
    database="website"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM user"
mycursor.execute(sql)
myresult = mycursor.fetchall()


def keeper(username, password):
    userDataBox = []
    for i in myresult:
        userDataBox.append(i[2])
    if username in userDataBox:
        pId = userDataBox.index(username)
        if password == myresult[pId][3]:
            return(myresult[pId][1])
        else:
            print("密碼不對")
    else:
        print("沒有這個使用者")
