# Import dependencies
from flask import Flask

# Create instance of Flask App
app = Flask(__name__)

# Define Route


@app.route("/")
# Content
def home():
    return("My first Home Page using Flask by Jihyun")


# Running and Controlling the script
if (__name__ == "__main__"):
    app.run(debug=True)
