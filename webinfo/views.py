from webinfo import app
from flask import render_template, flash, redirect, session, request, url_for
from .models import User, db
import os

@app.route("/")
@app.route("/index.html")
def index():
    username = session.get('username', '')
    return render_template("index.html", username=username)

@app.route("/about_us.html")
def about_us():
    return render_template("web/about_us.html")

@app.route("/contact.html")
def contact():
    return render_template("web/contact.html")

@app.route("/event.html")
def event():
    return render_template("web/event.html")

@app.route("/food.html")
def food():
    return render_template("web/food.html")  
@app.route("/join.html")
def join():
    return render_template("web/join.html")


@app.route("/layout.html")
def layout():
    return render_template("layout.html") 

@app.route("/kohchang.html")
def kohchang():
    return render_template("web/kohchang.html") 

@app.route("/kohtao.html")
def kohtao():
    return render_template("web/kohtao.html") 

@app.route("/monjong.html")
def monjong():
    return render_template("web/monjong.html") 

@app.route("/phukradueng.html")
def phukradueng():
    return render_template("web/phukradueng.html")  

@app.route("/sutongpe.html")
def sutongpe():
    return render_template("web/sutongpe.html")  
@app.route("/test.html")
def test():
    return render_template("web/test.html")  

@app.route("/test2.html")
def test2():
    return render_template("web/test2.html")  

@app.route("/travel.html")
def travel():
    return render_template("web/travel.html")  

@app.route("/nav.html")
def test4():
    return render_template("nav.html")

app.secret_key = os.urandom(12)
@app.route("/login.html", methods=["GET","POST"])
def login():
    error = None
    username = session.get('username', '')
    password = session.get('password', '')
    if request.method == 'POST':
        if request.form['username'] == '' and request.form['password'] == '':
            error = 'Please enter your username and password.'
        elif request.form['username'] == '':
            error = 'Please enter your username'
        elif request.form['password'] == '':
            error = 'Please enter your password'
        else:
            users = User.query.all()
            for user in users:
                if request.form['password'] == user.password and request.form['username'] == user.username:
                    flash('Login successfully.', 'success')
                    if username:
                        session['username'] = username
                    else:
                        session['username'] = request.form['username']
                    return redirect(url_for('.index'))
                else:
                    error = 'Invalid username or password. Please try again.'
    return render_template('login.html', error=error, username=username, password=password)

@app.route("/register.html", methods=["GET","POST"])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == '' or password == '':
            error = 'Please enter your username or password'
        else:
            if error == None:
                try:
                    new_user = User(username=username,password=password)
                    db.session.add(new_user)
                    db.session.commit()
                    session['username'] = username
                    session['password'] = password
                    flash('Register successfully.', 'success')
                    return redirect(url_for('.login'))
                except:
                    db.session.rollback()
                    error = "Username or Password already exists."
                    flash('Something Wrong!', 'error')
    return render_template("register.html", error=error)

@app.route('/logout')
def logout():
    session['username'] = ''
    flash('You were logged out')
    return redirect(url_for('index'))
    