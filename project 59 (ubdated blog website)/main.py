from flask import Flask, render_template,request
import requests
import datetime
import smtplib

date=datetime.datetime.now().date()
author="Ibrahim"
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts,author=author,date=date)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post,author=author,date=date)

@app.route('/contact',methods=['GET','POST'])
def receive_data():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)









if __name__ == "__main__":
    app.run(debug=True, port=5001)
