from flask import Flask, session, render_template, request, url_for, escape, redirect, send_from_directory
from flask_mail import Mail, Message
from werkzeug import secure_filename
import sqlite3
import os
import sqlite3 as sql




UPLOAD_FOLDER = 'static/img/cars/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lviv.trans.tour@gmail.com'
app.config['MAIL_PASSWORD'] = '123_xer_098'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



@app.route("/")
def load():
    return redirect(url_for('list3'))

@app.route('/connect', methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        a1 = request.form['email']
        a2 = request.form['password']
        a3 = "('" + a1 + "', '" + a2 + "')"
        t =  "('" + a1 + "',)"
        a1 = str(a1)
        conn = sqlite3.connect('228')
        c = conn.cursor()
        c.execute('SELECT email, password FROM Users WHERE email=?', [a1])
        a = c.fetchall()
        c.execute('SELECT admin FROM Users WHERE email=?', [a1])
        b = c.fetchall()
        c.execute('SELECT admin FROM Users WHERE email=?', [a1])
        g = [item[0] for item in c.fetchall()]
        b = b[0]
        b = str(b)
        y = a[0]
        y = str(y)
        a3 = str(a3)
        arr = (a1, g[0])
        if b == '(0,)':
            l = "admin"
        else:
            l = 'user'
        if y == a3:

            session['username'] = arr
            return redirect(url_for('list3'))
        else:
            return render_template('sign in.html')
@app.route('/registr', methods=['GET', 'POST'])
def registr():
    return render_template('registr.html')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return redirect(url_for('list3'))
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
    if request.method == 'POST':
        email = request.form['email']
        pas = request.form['password']
        num = request.form['number']
        name = request.form['name']
        surname = request.form['surname']
        adm = 0
        conn = sqlite3.connect('228')
        c = conn.cursor()
        c.execute("SELECT email from Users WHERE email=?",[email])
        em = [str(item[0]) for item in c.fetchall()]
        if len(em) < 1:
          c.execute("INSERT INTO Users_temp (email, number, name, surname, admin, code, password) VALUES (?, ?, ?, ?, ?, ?,?)",(email, num, name, surname, adm, a, pas))
          conn.commit()
          c.close()
          msg = Message('Hello', sender = 'lviv.trans.tour@gmail.com', recipients = [email])
          msg.body = "Dear "+ name +", its your security code:    " + a + "    Please enter it in confirmation field to finish registration."
          mail.send(msg)
          return render_template('confirm.html')
        else:
          error = ("This email is already in use")
          return render_template('registr.html',error=error)




























@app.route('/regadm', methods=['GET', 'POST'])
def regadm():
  if request.method == 'POST':
      email = request.form['email']
      pas = request.form['password']
      num = request.form['number']
      name = request.form['name']
      surname = request.form['surname']
      adm = 0
      conn = sqlite3.connect('228')
      c = conn.cursor()


      c.execute("INSERT INTO Users (email, number, name, surname, admin, password) VALUES (?, ?, ?, ?, ?,?)",(email, num, name, surname, adm, pas))
      conn.commit()
      c.close()
      return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('about_us.html')
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('list3'))
@app.route('/contact')
def contact():
    # remove the username from the session if it's there
    return render_template('contact.html')
@app.route('/panel')
def panel():
    # remove the username from the session if it's there
    return render_template('admin_panel.html')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    if request.method == 'POST':
        a1 = request.form['code']
        t =  "('" + a1 + "',)"
        a1 = str(a1)
        conn = sqlite3.connect('228')
        c = conn.cursor()
        c.execute('SELECT code FROM Users_temp WHERE code=?', [a1])
        a = c.fetchall()
        c.close()
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
            f = em[0]
            f = str(f)
            conn = sqlite3.connect('228')
            c = conn.cursor()
            c.execute("INSERT INTO Users (email, password, number, name, surname, admin) VALUES (?, ?, ?, ?, ?, ?)",(em[0], pas[0], num[0], nam[0], sur[0], adm))
            c.execute('DELETE FROM Users_temp WHERE email=?', [f])
            conn.commit()
            c.close()
            return render_template('sign in.html')
@app.route('/list', methods=['GET', 'POST'])
def list():
   a = request.form.get('bus')
   con = sql.connect("228")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT * from Cars WHERE id=?",([a]))
   rows = cur.fetchall();
   cur.execute("SELECT * from Photos WHERE id_car=?",([a]))
   phot = cur.fetchall();
   if len(rows) > 0:
    return render_template('bus_pg_01.html',rows = rows, phot = phot)
   else:
    return redirect(url_for('list3'))





@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        conn = sqlite3.connect('228')
        c = conn.cursor()
        email = session['username'][0]

        c.execute('SELECT id FROM Users WHERE email=?', [email])
        id = [str(item[0]) for item in c.fetchall()]
        c.execute('SELECT name FROM Users WHERE email=?', [email])
        nam = [str(item[0]) for item in c.fetchall()]
        c.execute('SELECT surname FROM Users WHERE email=?', [email])
        sur = [str(item[0]) for item in c.fetchall()]
        c.execute('SELECT number FROM Users WHERE email=?', [email])
        num = [str(item[0]) for item in c.fetchall()]
        car_id = request.form.get('sendMessage')
        dest = request.form['destination']
        date = request.form['date']
        peop = request.form['people']
        date2 = request.form['date2']
        c.execute("INSERT INTO Orders (car_id, user_id, date, destination, people, data2) VALUES (?, ?, ?, ?, ?, ?)",(car_id, id[0], str(date), dest, peop, date2))
        conn.commit()
        conn.close()
        conn = sqlite3.connect('228')
        c = conn.cursor()
        c.execute("SELECT MAX(id) from Orders")
        iddd = [str(item[0]) for item in c.fetchall()]
        msg = Message('Hello', sender = 'lviv.trans.tour@gmail.com', recipients = [email])
        msg.body = "User " + nam[0] + " " + sur[0] + " made an order with id " + iddd[0] + " . His email is: " + email + ", number is: " + num[0] + " "
        mail.send(msg)
        return redirect(url_for('list3'))












@app.route('/regcar')
def regcar():
    if session['username'][1] == 0:
      return render_template('registr_car.html')
@app.route('/regdrive')
def regdrive():
    return render_template('registr_driver.html')

@app.route('/reggdriver', methods=['GET', 'POST'])
def reggdriver():
  if session['username'][1] == 0:
    name = request.form['name']
    surname= request.form['surname']
    number = request.form['number']
    conn = sqlite3.connect('228')
    c = conn.cursor()
    c.execute("INSERT INTO Drivers (name, surname, number) VALUES (?, ?, ?)",(name, surname, number))
    conn.commit()
    conn.close()
    return redirect(url_for('list2'))


@app.route('/list2', methods=['GET', 'POST'])
def list2():
   if session['username'][1] == 0:
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


@app.route('/list3', methods=['GET', 'POST'])
def list3():
   con = sql.connect("228")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT * from Cars")
   rowss = cur.fetchall()
   return render_template('index.html',rowss = rowss)





@app.route('/deny', methods=['GET', 'POST'])
def deny():
   con = sql.connect("228")
   con.row_factory = sql.Row
   c = con.cursor()
   d = request.form.get('but1')
   c.execute("DELETE from Orders where Orders.id=?",([d]))
   con.commit()
   con.close()
   return redirect(url_for('list2'))

@app.route('/deny1', methods=['GET', 'POST'])
def deny1():
   con = sql.connect("228")
   con.row_factory = sql.Row
   c = con.cursor()
   d = request.form.get('but1')
   c.execute("DELETE from Cars where Cars.id=?",([d]))
   c.execute("DELETE from Photos where id_car=?",([d]))


   con.commit()
   con.close()
   return redirect(url_for('list2'))

@app.route('/deny2', methods=['GET', 'POST'])
def deny2():
   con = sql.connect("228")
   con.row_factory = sql.Row
   c = con.cursor()
   d = request.form.get('but1')
   c.execute("DELETE from Drivers where Drivers.id=?",([d]))
   con.commit()
   con.close()
   return redirect(url_for('list2'))






@app.route('/registr_car.html/<filename>')
def uploaded_file(filename):
  return send_from_directory(app.config['UPLOAD_FOLDER'],filename)



@app.route('/send_file/<filename>')
def send_file(filename):
  return send_from_directory(app.config['UPLOAD_FOLDER'], filename)










@app.route('/accept', methods=['GET', 'POST'])
def accept():
   con = sql.connect("228")
   c = con.cursor()
   a = request.form.get('but')
   l = request.form['inp']
   k = request.form['inp1']
   j = request.form['inp2']
   h = request.form['inp3']
   g = request.form['inp4']
   f = request.form['inp5']
   d = request.form['inp6']


   print(l)

   c.execute("UPDATE Orders SET car_id=?, date=?, price=?, destination=?, waylong=?, driver_id=?, data2=?, confirm=1 where Orders.id=?",(k,j,g,h,f,l,d,a))
   con.commit()
   con.close()
   return redirect(url_for('list2'))




@app.route('/reggcar', methods=['GET', 'POST'])
def reggcar():
  if session['username'][1] == 0:
    uploaded_files = request.files.getlist("file[]")
    f = request.files['files']
    filenames = []
    conditions = request.form['conditions']
    countries = request.form['countries']
    places = request.form['places']
    conn = sqlite3.connect('228')
    c = conn.cursor()
    c.execute("SELECT MAX(id) from Cars")
    em = [(item[0]) for item in c.fetchall()]
    em = em[0]
    em = em + 1
    st = os.path.splitext(f.filename)
    st = str(em) + str(st[1])
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], st))
    c.execute("INSERT INTO Cars (conditions, rode, places, photo) VALUES (?, ?, ?, ?)",(conditions, countries, places, st))
    conn.commit()
    conn.close()
    conn = sqlite3.connect('228')
    c = conn.cursor()
    c.execute("SELECT MAX(id) from Cars")
    em = [(item[0]) for item in c.fetchall()]
    em = em[0]
    for file in uploaded_files:
        conn = sqlite3.connect('228')
        c = conn.cursor()
        c.execute("SELECT MAX(id) from Photos")
        mm = [(item[0]) for item in c.fetchall()]
        mm = mm[0]
        mm = mm + 1
        strip = os.path.splitext(file.filename)
        strip = str(mm) + str(strip[1])
        c.execute("INSERT INTO Photos (id_car, photo) VALUES (?, ?)",(em, strip))
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], strip))
        filenames.append(filename)
        conn.commit()
        conn.close()
    return render_template('registr_car.html', filenames=filenames)

@app.route('/orders', methods=['GET', 'POST'])
def orders():
  con = sql.connect("228")
  con.row_factory = sql.Row
  cur = con.cursor()
  email = session['username'][0]
  cur.execute('SELECT id FROM Users WHERE email=?', [email])
  idd = [str(item[0]) for item in cur.fetchall()]
  cur.execute("SELECT * from Orders WHERE user_id=?",(idd))
  rows = cur.fetchall();
  return render_template('my orders.html',rows = rows)