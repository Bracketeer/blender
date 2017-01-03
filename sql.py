import sqlite3

with sqlite3.connect('clients.db') as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE clients(
	id INTEGER PRIMARY KEY,
	first_name TEXT,
	last_name TEXT,
	email TEXT,
	cta1_text TEXT,
	cta1_url TEXT,
	cta2_text TEXT,
	cta2_url TEXT,
	blog_url TEXT,
	website TEXT,
	address TEXT,
	city TEXT,
	state INTEGER,
	zip INTEGER,
	market_area TEXT,
	company_name TEXT,
	hex_color INTEGER,
	phone INTEGER
	)""");
	c.execute("""INSERT INTO clients VALUES(
	1,
	"Brent",
	"Stradling",
	"brent.stradling@gmail.com",
	"Home Value",
	"google.com",
	"Home Search",
	"twitter.com",
	"eyegoop.com",
	"eyegoop.com",
	"4841 Orchard Ave.",
	"Omaha",
	4,
	68117,
	"Omaha",
	"Eye Goop",
	123456,
	4023206766
	)""");

	c.execute("""INSERT INTO clients VALUES(
	2,
	"Bryce",
	"Stradling",
	"brent.stradling@gmail.com",
	"Home Value",
	"google.com",
	"Home Search",
	"twitter.com",
	"eyegoop.com",
	"eyegoop.com",
	"4841 Orchard Ave.",
	"Omaha",
	4,
	68117,
	"Omaha",
	"Lossless",
	123456,
	4023206766
	)""");
