from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3

app = Flask(__name__)
app.database = "clients.db"

@app.route('/')
def index():
	g.db = connect_db()
	cur = g.db.execute('select * from clients')
	clients = [dict(
	id=row[0],
	first_name=row[1],
	last_name=row[2],
	email=row[3],
	cta1_text=row[4],
	cta1_url=row[5],
	cta2_text=row[6],
	cta2_url=row[7],
	blog_url=row[8],
	website=row[9],
	address=row[10],
	city=row[11],
	state=row[12],
	zip=row[13],
	market_are=row[14],
	company_name=row[15],
	hex_color=row[16],
	phone=row[17]
	) for row in cur.fetchall()]
	g.db.close()
	return render_template('index.html', clients=clients)

def connect_db():
	return sqlite3.connect(app.database)

# app.run()
