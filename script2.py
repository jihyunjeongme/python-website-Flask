# Import dependencies
from flask import Flask

# Create instance of Flask App
app = Flask(__name__)

# Define Route and Contant of that page


@app.route("/")
def home():
    return("Jihyun Home page")

# Define 2nd Route and Content


@app.route("/about")
def about():
    return("About me, Jihyun")


# Running and Controlling the script
if (__name__ == "__main__"):
    app.run(debug=True)
