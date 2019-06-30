import sqlite3


class Database:
    #create connection - need to do init to ensure that this is called 
    #INITIALIZE AND OBJECT sort of like a constructor 
    #the datbase object is sent to __init__
    #you need to pass a parameter - and the object instance will be passed through it
    def __init__(self, db): 
        self.conn=sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()


#THESE ARE NOT CALLED BECAUSE WE NEED TO CALL THESE FUNCTIONS

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES(Null, ?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * from book")
        rows = self.cur.fetchall()
        return rows

    #need the empty titles so the function doesnt return an error
    def search(self,title="", author="", year="", isbn=""):
        #Need an OR statement incase he searches either option
        self.cur.execute("SELECT * from book where title=? OR author=? OR year=? or isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows


    def delete(self,id):
         self.cur.execute("DELETE from  book where id=?",(id,))
         self.conn.commit()


    def update(self,id, title, author, year, isbn):
         self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? where id=?",(title, author, year, isbn,id))
         self.conn.commit()
        #conn.close()

#special method to be executed when the program is closed
    def __del__(self):
        print("closed")
        self.conn.close()

    '''
    CALLING FUNCTIONS
    '''

#insert("The Earth", "John Smith", 1920, 19181715)
#print(search(author= "John Smith"))
#delete(2)
#update(1,"The Sea","Jogn Smooth",1222, 34562337)
#print(view())
