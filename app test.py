import mysql.connector
from flask import Flask
from flask import request, redirect
from flask import render_template
from flask import session
import os
from userData import keeper

# accountInfo = {"test": "test"}

app = Flask(
    __name__,
    static_url_path="/"
)

app.config['SECRET_KEY'] = os.urandom(24)


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


@app.route("/", methods=['GET', 'POST'])
def cindex():
    return render_template("homePage.html")


@app.route("/signout", methods=['GET', 'POST'])
def index():
    session.clear()
    return redirect('/')


@app.route("/signin", methods=["POST"])
def check():
    Account = request.form["account"]
    PassWord = request.form["password"]
    session['username'] = Account
    userDataBox = []
    for i in myresult:
        userDataBox.append(i[2])
    if(Account in userDataBox):
        pId = userDataBox.index(Account)
        if PassWord == myresult[pId][3]:
            return redirect('/member')
        else:
            return redirect("/error")
    else:
        return redirect("/error")

    # if (Account in ):
    #     if(PassWord == accountInfo[Account]):
    #         print("Success")
    #         return redirect('/member')
    #     print("Wrong Password  "+PassWord)
    #     return redirect("/error")
    # print("Wrong Account  "+Account)
    # return redirect("/error")


@app.route("/error", methods=["GET", "POST"])
def error():
    return render_template("errorPage.html")


@app.route("/member", methods=['GET', 'POST'])
def userpage():
    username = session.get('username')
    userDataBox = []
    for i in myresult:
        userDataBox.append(i[2])
    pId = userDataBox.index(username)
    name = myresult[pId][1]
    if username:
        return render_template("userPage.html", user_template=name)
    else:
        return redirect('/')


app.config['DEBUG'] = True
if __name__ == '__main__':
    app.run(port=3000)

# app.run(port=3000)
