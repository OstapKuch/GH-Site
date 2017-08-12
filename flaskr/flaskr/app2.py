from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)
import sqlite3



@app.route('/')
def home():
    print('MOROZIVo')
    return render_template('login.html')
    print('MOROZIVo')


@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('sign in.html')
