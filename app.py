from flask import Flask, request, render_template,  session

app = Flask(__name__) # Initialize the Flask application
app.secret_key = "my_secret_key" #Set a secret key for session management   



#dictionary will serve as our database
users = {"yaniv" : "0225", "elvi" : "1247"}

# Render the login page
@app.route('/')
def view_form():
    return render_template("login.html")


# Dealing with a GET request
@app.route('/handle_get', methods=["GET"])
def handle_get():
    if request.method == "GET":
        username = request.args["username"]
        password = request.args["password"]
        if username in users and users[username] == password:
            return'<h1>Welcome!!!</h1>'
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template("login.html")
    
#Dealing with a POST request
@app.route('/handle_post', methods=["POST"])
def handle_post():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            return '<h1>User Already exists!" </h1>'
        else:
            users[username] = password
            
            return '<h1>User Successfully registered!</h1>'
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask application in debug mode