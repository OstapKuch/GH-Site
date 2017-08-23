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
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ostapco220@gmail.com'
app.config['MAIL_PASSWORD'] = '123xer098'
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
        print(a1)
        print(g)
        arr = (a1, g[0])
        print(arr)
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
@app.route('/list', methods=['GET', 'POST'])
def list():
   a = request.form.get('bus')
   print(a)
   con = sql.connect("228")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT * from Cars WHERE id=?",([a]))
   rows = cur.fetchall();
   cur.execute("SELECT * from Photos WHERE id_car=?",([a]))
   phot = cur.fetchall();
   return render_template('bus_pg_01.html',rows = rows, phot = phot)







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
        nam = str(nam)
        msg = Message('Hello', sender = 'ostapco220@gmail.com', recipients = [email])
        msg.body = "User " + nam + " " + str(sur) + " made an order. His email is: " + str(email) + ", number is: " + str(num) + " "
        mail.send(msg)
        car_id = request.form.get('sendMessage')
        print(car_id)
        dest = request.form['destination']
        date = request.form['date']
        peop = request.form['people']
        c.execute("INSERT INTO Orders (car_id, user_id, date, destination, people) VALUES (?, ?, ?, ?, ?)",(car_id, id[0], str(date), dest, peop))
        conn.commit()
        return render_template('contact.html')












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
    print(number)
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
   print(d)
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
   print(d)
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
   print(d)
   c.execute("DELETE from Drivers where Drivers.id=?",([d]))
   con.commit()
   con.close()
   return redirect(url_for('list2'))





def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/registr_car.html/<filename>')
def uploaded_file(filename):  
  return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


@app.route('/send_file/<filename>')
def send_file(filename):
  print(filename)

  print(UPLOAD_FOLDER)
  return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
  
  

























  
@app.route('/accept', methods=['GET', 'POST'])
def accept():
   con = sql.connect("228")
   c = con.cursor()
   a = request.form.get('but')
   print(a)
   l = request.form['inp']

   print(l)

   c.execute("UPDATE Orders SET driver_id=?, confirm=1 where Orders.id=?",(l,a))
   
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
    print(em)
    em = em[0]
    for file in uploaded_files:
      if file and allowed_file(file.filename):  
        conn = sqlite3.connect('228')
        c = conn.cursor()
        c.execute("SELECT MAX(id) from Photos")
        mm = [(item[0]) for item in c.fetchall()]
        print(em)
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

