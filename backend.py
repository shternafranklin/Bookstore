import sqlite3

#create connection 
def connection():
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()



def insert(title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(Null, ?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()



def view():
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * from book")
    rows = cur.fetchall()
    conn.close()
    return rows

#need the empty titles so the function doesnt return an error
def search(title="", author="", year="", isbn=""):
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    #Need an OR statement incase he searches either option
    cur.execute("SELECT * from book where title=? OR author=? OR year=? or isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE from  book where id=?",(id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? where id=?",(title, author, year, isbn,id))
    conn.commit()
    conn.close()

'''
CALLING FUNCTIONS
'''

#always run this function since we are importing this into the frontend.py
connection()


#insert("The Earth", "John Smith", 1920, 19181715)
#print(search(author= "John Smith"))
#delete(2)
#update(1,"The Sea","Jogn Smooth",1222, 34562337)
#print(view())
