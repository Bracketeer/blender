from flask import Flask, render_template, redirect, url_for, request, session, flash
from peewee import *
from functools import wraps
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)

#config
import os
app.config.from_object(os.environ['APP_SETTINGS'])

#database
db = SqliteDatabase('clients.db')

#login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return	wrap

class Client(Model):
	id = IntegerField(primary_key=True)
	name = CharField()
	email = CharField()
	blog = CharField()

	class Meta:
		database = db

def create_tables():
	db.connect()
	db.create_tables([Client])

@app.route('/')
@login_required
def home():
	return render_template('client-table.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = "Invalid username or password."
		else:
			session['logged_in'] = True
			flash('Login Successful')
			return redirect(url_for('home'))
	return render_template('login.html', title='home', error=error)

@app.route('/logout')
@login_required
def logout():
	flash('Logout Successful')
	session.pop('logged_in', None)
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run()
