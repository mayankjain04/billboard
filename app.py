from flask import Flask, render_template, request, redirect
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

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        connection = get_db_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)  # Use DictCursor to get dictionaries instead of tuples
        username = request.form.get("username")
        name = request.form.get("name")
        if not username or not name:
            print("enter valid data")
            return redirect("/error")
        if username.lower() == "admin":
            print("Sorry, 'Admin' is a reserved username.")
            return render_template("error.html", message="Sorry, 'Admin' is a reserved username.")
        db.execute("INSERT INTO test(username, name) VALUES(%s, %s)", (username, name,))
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
        return render_template("show.html", table=table)

@app.route('/error')
def error():
    return render_template("error.html", message="INVALID DATA")

if __name__ == '__main__':
    app.run()
