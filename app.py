from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gonu@1394",  # replace this
    database="twotier"
)

cursor = db.cursor()

@app.route("/", methods=["GET"])
def home():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template("index.html", users=users)


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (username,))
    db.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:id>")
def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    db.commit()
    return redirect(url_for("home"))


@app.route("/edit/<int:id>")
def edit_user(id):
    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cursor.fetchone()
    return render_template("edit.html", user=user)


@app.route("/update/<int:id>", methods=["POST"])
def update_user(id):
    new_name = request.form.get("username")
    cursor.execute("UPDATE users SET name=%s WHERE id=%s", (new_name, id))
    db.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
