from flask import Flask, request, jsontify, render_template, redirect, url_for, session

app = Flask(__name__) # Initialize the Flask application
app.secret = "your_secret_key"  # Set a secret key for session management   

render_template("login.html")  # Render the login page

#dictionary will serve as our database
users = {}


# Dealing with a GET request
@app.route("handle_request", methods = ["GET"])
def handle_get():
    if request.method == "GET":
        username = request.args("username")
        password = request.args("password")
        if username in users and users[username] == password:
            return jsontify("Welcome!! You were successfully logged in."),200
        else:
            return jsontify("Invalid Credentials"),401
    else:
        return render_template("login.html")
    
#Dealing with a POST request
@app.route("handle_request", methods = ["POST"])
def handle_post():
    if request.method == "POST":
        username = request.form("username")
        password = request.form("password")
        if username in users and users[username] == password:
            return jsontify("Welcome!! You were successfully logged in."), 200
        else:
            return jsontify("Invalid Credentials"), 401
    else:
        return render_template("login.html")