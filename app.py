from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        return f"Login successful! Username: {username}, Email: {email}"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)