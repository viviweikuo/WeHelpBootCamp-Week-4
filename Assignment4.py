from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session

Assignment4 = Flask (
    __name__,
    static_folder = "public",
    static_url_path = "/"
)

Assignment4.secret_key = "le sserafim daisuki 우리 핌둥이 꽃길만 가자"

#首頁
@Assignment4.route("/")
def index():
    if "id" in session:
        return redirect("/member")
    else:
        return render_template("index.html")

#signin 驗證功能網址 POST
#memner 登入成功訊息(網頁) & error 登入失敗訊息(要求字串)
@Assignment4.route("/signin", methods = ["POST"])
def signin():

    memberID = request.form["id"]
    memberPassword = request.form["password"] 

    if (memberID == "test" and memberPassword == "test"):
        session["id"] = memberID
        session["password"] = memberPassword
        return redirect("/member")
    elif (memberID == "" or memberPassword == ""):
        return redirect(url_for("error", message = "請輸入帳號、密碼"))
    elif (memberID != "test" or memberPassword != "test"):
        return redirect(url_for("error", message = "帳號或密碼輸入錯誤"))

@Assignment4.route("/member")
def member():
    if "id" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@Assignment4.route("/error")
def error():
    result = request.args.get("message")
    return render_template("error.html", message = result)

#signout 登出功能用GET
@Assignment4.route("/signout")
def signout():
    session.pop("id", None)
    session.pop("password", None)
    return redirect("/")

#計算正整數
from tkinter import *
from tkinter import messagebox

@Assignment4.route("/positive-integer")
def positiveinteger():

    number = request.args.get("number", "")
    number = float(number)

    if (number % 1 != 0 or number < 0):
        return messagebox.showerror("警告", "這不是正整數")
    else:
        return redirect(url_for("square", num = number))

@Assignment4.route("/square/<num>")
def square():
    number = request.args.get("num")
    number = int(number)

    result = number * number
    return render_template("square.html", data = result)

Assignment4.run(port=3000)


