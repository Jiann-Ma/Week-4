#如何成功跑出CSS：https://yanwei-liu.medium.com/python%E7%B6%B2%E9%A0%81%E8%A8%AD%E8%A8%88-flask%E4%BD%BF%E7%94%A8%E7%AD%86%E8%A8%98-%E4%BA%8C-89549f4986de
#包含css一定要放進static裡面，html一定要放進templates裡面之類的

from flask import Flask #載入Flask
from flask import request #載入Request物件
from flask import render_template, redirect, session, url_for
from markupsafe import escape

app=Flask(              #載入Application物件，可以設定靜態檔案的路徑處理
    __name__,
    #static_folder="templates",  #只能有一個靜態資料夾  #靜態檔案的資料夾名稱(可以自訂，但要記得實體資料夾名稱也要同時改)
)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'\xe8s\xb9\x0e\xddZ \xc3\x80\xa5\x1a\x11\x99J\xe7V'

@app.route("/") #基本路由設定語法 @app.route("路徑") <-> 動態路由設定語法 @app.route("/固定字首/<參數名稱>")
def home():
    if "account" in session:  
        return 'Logged in as %s' % escape(session["account"])     
    return render_template("homeWork-4-html.html")

@app.route("/member")
def success():
    return render_template("homeWork-4-html-sucess.html")

@app.route("/error")
def failure():
    return render_template("homeWork-4-html-faillure.html")

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        if request.form["account"] == "test" and request.form["password"] == "test":
            return redirect("/member")
        else:
            return redirect("/error")
    if request.method == "GET":
        session["account"] = request.form["account"]
        return redirect(url_for("home"))

@app.route("/signout")
def signout():
    # remove the username from the session if it's there
    session.pop("account", None)
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(port=3000)