from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from helpers import login_required
import pymysql

app = Flask(__name__)

# Database connection details
host = 'Billboard.mysql.pythonanywhere-services.com'
user = 'Billboard'
password = 'local123'
db = 'Billboard$default'

def get_db_connection():
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=db
    )
    return connection



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        connection = get_db_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)  # Use DictCursor to get dictionaries instead of tuples
        username = session['username'] if 'username' in session else "Anonymous"
        text = request.form.get("text")
        if not text:
            print("enter valid data")
            return redirect("/error")
        db.execute("INSERT INTO test(username, name) VALUES(%s, %s)", (username, text,))
        connection.commit()
        table = db.fetchall()
        db.close()
        connection.close()
        return redirect("/")
    else:
        connection = get_db_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)  # Use DictCursor to get dictionaries instead of tuples
        db.execute("SELECT Row_Number() OVER (ORDER BY id) AS id, username, name FROM test")
        table = db.fetchall()
        db.close()
        connection.close()
        return render_template("index.html", table=table)

@app.route('/error')
def error():
    return render_template("error.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            session.clear()
            connection = get_db_connection()
            db = connection.cursor(pymysql.cursors.DictCursor)
            username = request.form.get("username")
            password = request.form.get("password")
            db.execute("SELECT * FROM users WHERE username = %s", (username,))
            result = db.fetchone()
            if not (username or password):
                return render_template("error.html", message="please enter valid data")
            if not result:
                return render_template("error.html", message="user not registered")
            if not result['password'] == password:
                return render_template("error.html", message="incorrect password")
            session['user_id'] = result['user_id']
            session['username'] = result['username']
            return redirect('/')
        else:
            if 'user_id' in session:
                session.clear()
                return redirect("/")
            return render_template("login.html")
    finally:
        if 'db' in locals():
            db.close()
        if 'connection' in locals():
            connection.close()

@app.route('/register', methods=["GET", "POST"])
def register():
    try:
        if request.method == "POST":
            connection = get_db_connection()
            db = connection.cursor(pymysql.cursors.DictCursor)
            username = request.form.get("username")
            password = request.form.get("password")
            confirmation = request.form.get("confirm")
            db.execute("SELECT user_id FROM users WHERE username = %s", (username,))
            result = db.fetchone()
            if not (username and password and confirmation):
                return render_template("register.html", message="please enter valid data")
            if result:
                return render_template("register.html", message="username not available")
            if not confirmation == password:
                return render_template("register.html", message="passwords do not match")
            db.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            connection.commit()
            db.execute("SELECT user_id FROM users WHERE username = %s", (username,))
            result = db.fetchone()
            connection.commit()
            session['user_id'] = result['user_id']
            session['username'] = username
            return render_template('login.html', message="registered successfully")
        else:
            return render_template("register.html")
    finally:
        if 'db' in locals():
            db.close()
        if 'connection' in locals():
            connection.close()

if __name__ == '__main__':
    app.run()
