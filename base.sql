--clear all tables
DROP TABLE books;
DROP TABLE authors;
DROP TABLE category;
DROP TABLE publisher;


--create new tables
CREATE TABLE IF NOT EXISTS authors (
	id INTEGER NOT NULL PRIMARY KEY,
	firstname VARCHAR NOT NULL,
	lastname VARCHAR NOT NULL);
CREATE TABLE IF NOT EXISTS category (
	id INTEGER NOT NULL PRIMARY KEY,
	title VARCHAR NOT NULL);
CREATE TABLE IF NOT EXISTS publisher (
	id INTEGER NOT NULL PRIMARY KEY,
	title VARCHAR NOT NULL);
CREATE TABLE IF NOT EXISTS books (
	id INTEGER NOT NULL PRIMARY KEY,
	title VARCHAR NOT NULL,
	author INTEGER NOT NULL REFERENCES authors (id),
	category INTEGER NOT NULL REFERENCES category (id) DEFAULT 0,
	description VARCHAR,
	publisher INTEGER NOT NULL REFERENCES publisher (id) DEFAULT 0,
	rating FLOAT NOT NULL DEFAULT 0.0,
	votes INTEGER default 0);

--insert default values
INSERT INTO authors(id, firstname, lastname) VALUES (0, 'ND', 'ND');
INSERT INTO category(id, title) VALUES (0, 'ND');
INSERT INTO publisher(id, title) VALUES (0, 'ND');

--added category_id table and column into category and books tables
CREATE TABLE IF NOT EXISTS category_id (
	id INTEGER NOT NULL PRIMARY KEY,
	title VARCHAR);

ALTER TABLE category ADD COLUMN cat_id INTEGER REFERENCES category_id (id);
ALTER TABLE books ADD COLUMN description_nlp VARCHAR;


--created user base
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY);

CREATE TABLE IF NOT EXISTS users_books (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "user" (id),
    book_id INTEGER NOT NULL REFERENCES books (id));

CREATE TABLE IF NOT EXISTS user_preferences (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "user" (id),
    book_id INTEGER NOT NULL REFERENCES books (id));



