from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def load():
    return render_template('index.html')
import sqlite3
@app.route('/', methods=['GET', 'POST'])
def connect():
	if request.method == 'POST':
		a1 = request.form['email']
		a2 = request.form['password']
		a3 = "('" + a1 + "', '" + a2 + "')"
		t =  "('" + a1 + "',)"
		print(t)
		a1 = str(a1)
		print(a3)
		conn = sqlite3.connect('Proj')
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('login'))

    # show the form, it wasn't submitted
    return render_template('login.html')

	






    




