from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def load():
    return render_template('registr.html')
import sqlite3
@app.route('/', methods=['GET', 'POST'])
def connect():
	if request.method == 'POST':
		email = request.form['email']
		pas = request.form['password']
		num = request.form['number']
		name = request.form['name']
		surname = request.form['surname']
		idd = 2
		adm = 0
		
		conn = sqlite3.connect('Proj')
		c = conn.cursor()
		c.execute("INSERT INTO Users (id, email, password, number, name, surname, admin ) VALUES (?, ?, ?, ?, ?, ?, ?)",(idd, email, pas, num, name, surname, adm))
		conn.commit()
		return render_template('sign in.html')



	
