from flask import Flask, request, render_template_string
import logging

app = Flask(__name__)

# Log failed login attempts
logging.basicConfig(filename="login_attempts.log", level=logging.INFO)

HTML = """
<h2>Login Page</h2>
<form method="POST">
  <input type="text" name="username" placeholder="Username" required><br><br>
  <input type="password" name="password" placeholder="Password" required><br><br>
  <button type="submit">Login</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "password123":
            return "✅ Login successful!"
        else:
            logging.info(f"Failed login from {request.remote_addr} for user {username}")
            return "❌ Login failed!"
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
