from flask import Flask, render_template, request, url_for
app = Flask(__name__)


    
@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  msg = Message(form.subject.data, sender='ostapco220@gmail.com', recipients=['ostapko220@gmail.com'])
  msg.body = 'sadads das sadsad asdsa dasdasd a'
  mail.send(msg)
  return render_template('contact.html')