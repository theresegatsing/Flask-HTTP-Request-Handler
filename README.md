📡 Flask HTTP Request Handler
A simple Flask web app that demonstrates how to handle GET and POST HTTP requests using login and registration forms. The app mimics a basic user authentication system using a Python dictionary as the database.

🚀 Features
✅ Login using a GET request

✅ Register using a POST request

✅ Handles user input via HTML forms

✅ Simulated database using a Python dictionary

✅ Flask templating with render_template

✅ Session-ready setup with app.secret_key

🧠 How It Works
🔐 Login (GET request)
Users submit their credentials.

The server checks if the credentials match existing users.

Returns a "Welcome" message or an "Invalid credentials" message.

📝 Registration (POST request)
Users submit new credentials via a form.

If the username doesn't exist, it’s added to the dictionary.

Returns a "Successfully registered" message.

If the username already exists, it returns "User Already exists".
