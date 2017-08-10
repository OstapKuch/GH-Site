from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def load():
    return render_template('registr.html')
import sqlite3
@app.route('/', methods=['GET', 'POST'])
def connect():
	if request.method == 'POST':
		user = request.form['username']
		pas = request.form['password']
		conn = sqlite3.connect('Project')
		c = conn.cursor()
		c.execute("INSERT INTO users (user, pass) VALUES (?, ?)",(user, pas))
		conn.commit()
		return render_template('sign in.html')



	
