import os
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_session import Session
from helpers import login_required
import pymysql
from contextlib import contextmanager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)

# Database connection details
host = 'localhost'
user = 'root'
password = "local@123"
db = 'billboard'

@contextmanager
def get_db_connection():
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=db
    )
    try:
        yield connection
    finally:
        if 'db' in locals():
            db.close()
        connection.close()


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem" # use null for testing, filesystem for deployment
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
        text = request.form.get("text")
        if not text:
            flash('enter valid data/empty text field')
            return redirect("/")
        username = session.get("username", "Anonymous")
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:  # Use DictCursor to get dictionaries instead of tuples
                cursor.execute("INSERT INTO test(username, text) VALUES(%s, %s)", (username, text,))
                connection.commit()
        return redirect("/")
    else:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:  # Use DictCursor to get dictionaries instead of tuples
                cursor.execute("SELECT Row_Number() OVER (ORDER BY id) AS id, id as post_id, username, text, time FROM test")
                table = cursor.fetchall()
                return render_template("index.html", table=table)

@app.route('/error')
def error():
    return render_template("error.html")

@app.route('/login', methods=["GET", "POST"])
def login():
        if request.method == "POST":
            # checking for the validity of data submitted by login
            session.clear()
            username = request.form.get("username")
            password = request.form.get("password")
            with get_db_connection() as connection:
                with connection.cursor(pymysql.cursors.DictCursor) as cursor:  # Use DictCursor to get dictionaries instead of tuples
                    cursor.execute("SELECT user_id, pw_hash FROM users WHERE username = %s", (username,))
                    result = cursor.fetchone()
                    if not result:
                        return render_template("login.html", message="user not registered")
                    if not check_password_hash(result['pw_hash'], password):
                        return render_template("login.html", message="incorrect password")
                    session['user_id'] = result['user_id']
                    session['username'] = username
                    return redirect('/')
        else:
            if 'user_id' in session:
                # this happens when the user is trying to log out
                session.clear()
                return redirect("/")
            # this happens when user is trying to log in
            return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            confirmation = request.form.get("confirm")
            if not (username and password):
                return render_template("register.html", message="you sneaky son of a gun, insert valid data.")
            if not confirmation == password:
                return render_template("register.html", message="passwords did not match")
            with get_db_connection() as connection:
                with connection.cursor(pymysql.cursors.DictCursor) as cursor:  # Use DictCursor to get dictionaries instead of tuples
                    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
                    result = cursor.fetchone()
                    if result:
                        return render_template("register.html", message="username not available")
                    hashed_pw = generate_password_hash(password)
                    cursor.execute("INSERT INTO users (username, pw_hash) VALUES (%s, %s)", (username, hashed_pw))
                    connection.commit()
                    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
                    result = cursor.fetchone()
                    session['user_id'] = result['user_id']
                    session['username'] = username
                    return redirect("/")
        else:
            return render_template("register.html")

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
        if request.method=='POST':
            row_id = request.form.get('row_id')
            NewName = request.form.get('NewName')
            with get_db_connection() as connection:
                with connection.cursor(pymysql.cursors.DictCursor) as cursor:  # Use DictCursor to get dictionaries instead of tuples
                    if row_id:
                        cursor.execute("DELETE FROM test WHERE id = %s", (row_id, ))
                        connection.commit()
                        flash('rowdeleted')
                        return redirect(url_for('profile'))
                    if NewName:
                        cursor.execute("SELECT user_id FROM users WHERE username = %s", (NewName,))
                        result = cursor.fetchone()
                        if result:
                            flash('username not available!')
                            return redirect(url_for('profile'))
                        cursor.execute("UPDATE users SET username = %s WHERE user_id = %s", (request.form.get('NewName'), session['user_id'], ))
                        connection.commit()
                        cursor.execute("UPDATE test SET username = %s WHERE username = %s", (request.form.get('NewName'), session['username'], ))
                        connection.commit()
                        session['username'] = request.form.get('NewName')
                        flash('Username changed successfully!')
                        return redirect(url_for('profile'))
                    if request.form.get('NewPass'):
                        hashed_pw = generate_password_hash(request.form.get('NewPass'))
                        cursor.execute("UPDATE users SET pw_hash = %s WHERE user_id = %s", (hashed_pw, session['user_id'], ))
                        connection.commit()
                        flash('Password changed successfully!')
                        return redirect(url_for('profile'))
                    return redirect(url_for('error', message='profile path could not resolve the POST method!'))
        else:
            username = request.args.get('username', session.get('username'))
            with get_db_connection() as connection:
                with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                    cursor.execute("WITH allrows AS (SELECT Row_Number() OVER (ORDER BY id) AS row_id, id, username, text, time FROM test) SELECT * FROM allrows WHERE username = %s", (username,))
                    table = cursor.fetchall()
                    message= request.args.get('message')
                    return render_template("profile.html",username=username, table=table, message=message)

@app.route("/support", methods=["GET", "POST"])
@login_required
def support():
        if request.method=='POST':
            with get_db_connection() as connection:
                with connection.cursor(pymysql.cursors.DictCursor) as cursor:  # Use DictCursor to get dictionaries instead of tuples
                    cursor.execute("INSERT INTO feedback (username, feedback) VALUES(%s, %s)", (session.get('username'), request.form.get('feedback')))
                    connection.commit()
                    flash('Response submitted successfully!', 'success')
                    return redirect("/support")
        else:
            return render_template("support.html")

@app.route("/report", methods=["GET", "POST"])
@login_required
def report():
    if request.method == "POST":
        post_id = request.form.get("post_id", "")
        if not post_id:
            return redirect('/error')
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:  # Use DictCursor to get dictionaries instead of tuples
                cursor.execute("INSERT INTO feedback (username, feedback, post_id) VALUES(%s, %s, %s)", (session.get('username'), request.form.get('post-report', 'error/html bypassed'), post_id)) # the error will only show if user somehow submitted an empty report.
                connection.commit()
        return redirect("/")
    else:
        post_id = request.args.get('post_id', '')
        if not post_id:
            return render_template('error.html', message = "post id not found")
        return render_template("report.html", post_id=post_id, )

if __name__ == '__main__':
    app.run(debug=True)
