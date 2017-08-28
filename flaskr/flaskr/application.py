from flask import Flask, render_template



@app.route("/")
def load():
  return render_template('about_us.html')