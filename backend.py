import sqlite3

import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "book_project.db")


def connect():
    with sqlite3.connect(db_path) as conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author TEXT, year INT, isbn INT)")
        conn.commit()


def insert(title, author, year, isbn):
    with sqlite3.connect(db_path) as conn:
        cur=conn.cursor()
        cur.execute("INSERT INTO book(title,author,year,isbn) VALUES (?,?,?,?)",(title, author, year, isbn))
        conn.commit()


def view():
    with sqlite3.connect(db_path) as conn:
        cur= conn.cursor()
        cur.execute("SELECT * FROM book")
        rows=cur.fetchall()
        return rows

def search(title="", author="", year="", isbn=""):
    with sqlite3.connect(db_path) as conn:
        cur= conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=? ", (title, author, year, isbn))
        rows=cur.fetchall()
        return rows

def delete(id):
    with sqlite3.connect(db_path) as conn:
        cur=conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()

def update(id, title, author, year, isbn):
    with sqlite3.connect(db_path) as conn:
        cur=conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        conn.commit()



#connect()
#insert("Native Son", "Richard Wright", 1960, 99822390)
#insert("Black Boy", "James Baldwin", 1980, 291902023)
#insert("The Sun", "John Smith", 1918, 923129321)
#delete (4)
#update(2,'Black Boy','Richard Wright', 1980, 29183943489)
#print(view())
#print(search(author= 'Richard Wright' ))
