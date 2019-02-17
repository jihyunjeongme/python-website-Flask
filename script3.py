# Import dependencies
from flask import Flask, render_template

# Create instance of Flask App
app = Flask(__name__)

# Define Route and Contant of that page


@app.route("/")
def home(name=None):
    return render_template("index.html", name=name)

# Define


@app.route("/index")
@app.route("/index/<name>")
def index(name=None):
    return render_template("index.html", name=name)

# 채팅방 전체


@app.route("/chats")
def chats():
    return render_template("chats.html")

# Find


@app.route("/find")
def find():
    return render_template("find.html")

# More


@app.route("/more")
def more():
    return render_template("more.html")


# 채팅방 상세
@app.route("/chat")
def chat():
    return render_template("chat.html")

# Profile


@app.route("/profile")
def profile():
    return render_template("profile.html")

# Image


@app.route("/images")
def images():
    return render_template("avartar.jpg")


# Running and Controlling the script
if (__name__ == "__main__"):
    app.run(debug=True)
