from flask import Flask, session, render_template, request, url_for, escape
from flask_login import current_user
from flask_mail import Mail, Message

app = Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ostapco220@gmail.com'
app.config['MAIL_PASSWORD'] = '123xer098'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/send")
def send():
   msg = Message('Hello', sender = 'ostapco220@gmail.com', recipients = ['ostapko220@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

@app.route("/")
def load():
    return render_template('index.html')

import sqlite3
import sqlite3 as sql
import sys


	
@app.route('/connect', methods=['GET', 'POST'])
def connect():
	if request.method == 'POST':

		
		a1 = request.form['email']
		a2 = request.form['password']
		a3 = "('" + a1 + "', '" + a2 + "')"
		t =  "('" + a1 + "',)"
		print(t)
		a1 = str(a1)
		print(a3)
		conn = sqlite3.connect('228')
		c = conn.cursor()
		c.execute('SELECT email, password FROM Users WHERE email=?', [a1])
		a = c.fetchall()
		c.execute('SELECT admin FROM Users WHERE email=?', [a1])
		b = c.fetchall()
		print(a[0])
		b = b[0]
		b = str(b)
		y = a[0]
		y = str(y)
		a3 = str(a3)
		print(b)
		if b == '(0,)':
			l = "admin"
		else:
			l = 'user'
		if y == a3:
			session['username'] = a1
			print(session['username'])
			return render_template('show_entries.html')
		else:
			return render_template('sign in.html')


@app.route('/registr', methods=['GET', 'POST'])
def registr():
    return render_template('registr.html')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('sign in.html')





@app.route('/create', methods=['GET', 'POST'])
def create():
	import random
	c = 0
	a = ""
	while c < 6:
		b = random.randint(1,9)
		b = str(b)
		a = a + b
		c= c + 1
	print(a)

	if request.method == 'POST':
		
		email = request.form['email']
		pas = request.form['password']
		num = request.form['number']
		name = request.form['name']
		surname = request.form['surname']
		adm = 0
		conn = sqlite3.connect('228')
		c = conn.cursor()
		c.execute("INSERT INTO Users_temp (email, number, name, surname, admin, code, password) VALUES (?, ?, ?, ?, ?, ?,?)",(email, num, name, surname, adm, a, pas))
		conn.commit()
		c.close()
		msg = Message('Hello', sender = 'ostapco220@gmail.com', recipients = [email])
		msg.body = "Dear "+ name +", its your security code:  " + a + " Please enter it in confirm field to finish registration."
		mail.send(msg)
		return render_template('confirm.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return render_template('index.html')

@app.route('/contact')
def contact():
    # remove the username from the session if it's there
    return render_template('contact.html')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'   




@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
	if request.method == 'POST':
		a1 = request.form['code']
		t =  "('" + a1 + "',)"
		print(t)
		a1 = str(a1)
		conn = sqlite3.connect('228')
		c = conn.cursor()
		c.execute('SELECT code FROM Users_temp WHERE code=?', [a1])
		a = c.fetchall()
		c.close()
		print(a[0])
		y = a[0]
		y = str(y)
		t = str(t)
		if y == t:
			conn = sqlite3.connect('228')
			c = conn.cursor()
			c.execute('SELECT email FROM Users_temp WHERE code=?', [a1])
			em = [str(item[0]) for item in c.fetchall()]
			c.execute('SELECT password FROM Users_temp WHERE code=?', [a1])
			pas = [str(item[0]) for item in c.fetchall()]
			c.execute('SELECT number FROM Users_temp WHERE code=?', [a1])
			num = [str(item[0]) for item in c.fetchall()]
			c.execute('SELECT name FROM Users_temp WHERE code=?', [a1])
			nam = [str(item[0]) for item in c.fetchall()]
			c.execute('SELECT surname FROM Users_temp WHERE code=?', [a1])
			sur = [str(item[0]) for item in c.fetchall()]
			c.close()
			adm = 1
			print(em[0], pas[0], num[0], nam[0], sur[0])
			f = em[0]
			f = str(f)
			print(f)
			print(em, pas, num, nam, sur, adm)
			conn = sqlite3.connect('228')
			c = conn.cursor()
			print(em, pas, num, nam, sur, adm)
			c.execute("INSERT INTO Users (email, password, number, name, surname, admin) VALUES (?, ?, ?, ?, ?, ?)",(em[0], pas[0], num[0], nam[0], sur[0], adm))
			print(em[0], pas[0], num[0])
			c.execute('DELETE FROM Users_temp WHERE email=?', [f])
			conn.commit()
			c.close()
			print(em[0], pas[0], num[0])
			return render_template('sign in.html')



@app.route('/form', methods=['GET', 'POST'])
def form():
	if request.method == 'POST':
		conn = sqlite3.connect('228')
		c = conn.cursor()
		email = session['username']
		c.execute('SELECT name FROM Users WHERE email=?', [email])
		nam = [str(item[0]) for item in c.fetchall()]
		c.execute('SELECT surname FROM Users WHERE email=?', [email])
		sur = [str(item[0]) for item in c.fetchall()]
		c.execute('SELECT number FROM Users WHERE email=?', [email])
		num = [str(item[0]) for item in c.fetchall()]
		nam = str(nam)
		msg = Message('Hello', sender = 'ostapco220@gmail.com', recipients = [email])
		msg.body = "User " + nam + " " + str(sur) + " made an order. His email is: " + str(email) + ", number is: " + str(num) + " "
		mail.send(msg)
		return render_template('contact.html')


@app.route('/forr', methods=['GET', 'POST'])
def forr():
	conn = sqlite3.connect('228')
	c = conn.cursor()
	c.execute("SELECT * from Photo")
	a = c.fetchall()
	print(a)
	return render_template("bus_pg_01.html")

	
@app.route('/list')
def list():
   con = sql.connect("228")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("SELECT * from Cars")
   
   rows = cur.fetchall(); 
   return render_template("bus_pg_01.html",rows = rows)

@app.route('/regcar')
def regcar():
	return render_template('registr_car.html')
@app.route('/regdrive')
def regdrive():
	return render_template('registr_driver.html')

@app.route('/reggcar', methods=['GET', 'POST'])
def reggcar():
	conditions = request.form['conditions']
	countries = request.form['countries']
	places = request.form['places']
	print(places)
	conn = sqlite3.connect('228')
	c = conn.cursor()	
	c.execute("INSERT INTO Cars (conditions, rode, places) VALUES (?, ?, ?)",(conditions, countries, places))
	conn.commit()
	conn.close()
	return redirect(url_for('list2'))

@app.route('/reggdriver', methods=['GET', 'POST'])
def reggdriver():
	name = request.form['name']
	surname= request.form['surname']
	number = request.form['number']
	print(number)
	conn = sqlite3.connect('228')
	c = conn.cursor()	
	c.execute("INSERT INTO Drivers (name, surname, number) VALUES (?, ?, ?)",(name, surname, number))
	conn.commit()
	conn.close()
	return redirect(url_for('list2'))





@app.route('/list2', methods=['GET', 'POST'])
def list2():
   con = sql.connect("228")
   con.row_factory = sql.Row
   
   cur = con.cursor()

   cur.execute("select * from Cars")
   rowss = cur.fetchall();

   cur.execute("select * from Orders")
   rows = cur.fetchall();


   cur.execute("select * from Drivers")
   rowsss = cur.fetchall();  

   return render_template('admin_panel.html',rowss = rowss,rows = rows,rowsss = rowsss)
