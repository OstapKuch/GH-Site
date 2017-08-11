from flask import Flask, session, render_template, request, url_for, escape
app = Flask(__name__)

@app.route('/')
def load():
    return render_template('index.html')

import sqlite3

@app.route('/connect', methods=['GET', 'POST'])
def connect():
	if request.method == 'POST':

		session['username'] = 'admin'
		a1 = request.form['email']
		a2 = request.form['password']
		a3 = "('" + a1 + "', '" + a2 + "')"
		t =  "('" + a1 + "',)"
		print(t)
		a1 = str(a1)
		print(a3)
		conn = sqlite3.connect('Proj1')
		c = conn.cursor()
		c.execute('SELECT email, password FROM Users WHERE email=?', [a1])
		a = c.fetchall()
		print(a[0])
		y = a[0]
		y = str(y)
		a3 = str(a3)
		if y == a3:
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
	if request.method == 'POST':
		email = request.form['email']
		pas = request.form['password']
		num = request.form['number']
		name = request.form['name']
		surname = request.form['surname']
		idd = 15
		adm = 0
		conn = sqlite3.connect('Proj1')
		c = conn.cursor()
		c.execute("INSERT INTO Users (id, email, password, number, name, surname, admin ) VALUES (?, ?, ?, ?, ?, ?, ?)",(idd, email, pas, num, name, surname, adm))
		conn.commit()
		c.close()
		return render_template('sign in.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return render_template('index.html')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'   




