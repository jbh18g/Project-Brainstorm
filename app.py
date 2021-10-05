from flask import Flask, render_template, request
import sqlite3 as sql
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run('localhost', debug=True)