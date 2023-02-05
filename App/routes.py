from flask import Flask, render_template, request, redirect, url_for
#import pymysql
import pymysql.cursors
from App.confi import *


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            return "Password and Confirm Password must be same"

        try:
            with conn.cursor() as cursor:
                # Check if email is already registered
                sql = "SELECT * FROM user WHERE email=%s"
                cursor.execute(sql, (email,))
                result = cursor.fetchone()

                if result:
                    return "User with this email already exists, try another email."

                # Insert user data
                sql = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, email, password))
                conn.commit()
                if name is None:
                    return "Name cannot be empty."

                return redirect(url_for('login'))

        except Exception as e:
            return "Error occurred while inserting user data: " + str(e)

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'name' in request.form and 'password' in request.form:
        name = request.form['name']
        password = request.form['password']
    else:
        return render_template('login.html', error="The name and password fields are required.")

    # Check if the username and password are in the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE name = %s AND password = %s", (name, password))
    result = cursor.fetchone()
    cursor.close()

    # If the username and password are not in the database, return an error message
    if result is None:
        return render_template('login.html', error="The name and password you entered are incorrect.")

    # Redirect to the form page
    return redirect(url_for('form'))


@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'GET':
        return render_template('forgot_password.html')
    else:
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if the email is in the database
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
        result = cursor.fetchone()
        cursor.close()

        # If the email is not in the database, redirect to the login page with an error message
        if result is None:
            return render_template('login.html', error="The email you entered is not registered.")

        # If the new password and the confirmed password do not match, return an error message
        if password != confirm_password:
            return render_template('forgot_password.html', error="The new password and the confirmed password do not match.")

        # Update the password in the database
        cursor = conn.cursor()
        cursor.execute("UPDATE user SET password = %s WHERE email = %s", (password, email))
        conn.commit()
        cursor.close()

        # Redirect to the login page
        return redirect(url_for('login'))

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Get the form data
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        age = request.form["age"]
        email = request.form["email"]
        mobile_number = request.form["mobile_number"]
        blood_group = request.form["blood_group"]
        address = request.form["address"]
        gender = request.form["gender"]
        organs_donated = request.form.getlist("organs_donated")

        # Store the form data in the MySQL database
        with conn.cursor() as cursor:
            sql = "INSERT INTO donor_info (first_name, last_name, age, email, mobile_number, blood_group, address, gender, organs_donated) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (first_name, last_name, age, email, mobile_number, blood_group, address, gender, ",".join(organs_donated)))
            conn.commit()

        # Redirect to the logout page
        return redirect(url_for("logout"))

    return render_template("logout.html")


@app.route('/about')
def about():

    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/logout")
def logout():


    # Redirect to home page
    return redirect(url_for("home"))
