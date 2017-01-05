from flask import Flask, render_template
from peewee import *

db = SqliteDatabase('clients.db')

app = Flask(__name__)

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
def index():
	client = Client.select()
	return render_template('index.html', client=client)

if __name__ == '__main__':
	app.run(debug=True)
# app.run(debug=True)
