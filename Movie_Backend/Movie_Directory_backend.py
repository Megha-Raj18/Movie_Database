import sqlite3
def connect():
    mycon=sqlite3.connect(r'C:\Users\Raj\Anaconda3\Library\bin\movies.db')
    cursor=mycon.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS movies(ID INTEGER PRIMARY KEY,Movie_title VARCHAR(100),Director VARCHAR(100),Year INTEGER,Category VARCHAR(100),Duration INTEGER)")
    mycon.commit()
    mycon.close()
    
def insert(title,director,year,category,duration):
    mycon=sqlite3.connect(r'C:\Users\Raj\Anaconda3\Library\bin\movies.db')
    cursor=mycon.cursor()
    cursor.execute("INSERT INTO movies VALUES(NULL,?,?,?,?,?)",(title,director,year,category,duration))
    mycon.commit()
    mycon.close()
    
def view():
    mycon=sqlite3.connect(r'C:\Users\Raj\Anaconda3\Library\bin\movies.db')
    cursor=mycon.cursor()
    cursor.execute("SELECT * FROM movies")
    resultset=cursor.fetchall()
    mycon.close()
    return resultset

def search(title="",director="",year="",category="",duration=""):
    mycon=sqlite3.connect(r'C:\Users\Raj\Anaconda3\Library\bin\movies.db')
    cursor=mycon.cursor()
    cursor.execute("SELECT * FROM movies WHERE Movie_title=? OR Director=? OR Year=? OR Category=? OR Duration=?",(title,director,year,category,duration))
    resultset=cursor.fetchall()
    mycon.close()
    return resultset

def delete(Id):
    mycon=sqlite3.connect(r'C:\Users\Raj\Anaconda3\Library\bin\movies.db')
    cursor=mycon.cursor()
    cursor.execute("DELETE FROM movies WHERE ID=?",(Id,))
    mycon.commit()
    resultset=cursor.fetchall()
    mycon.close()
    
def update(Id,title,director,year,category,duration):
    mycon=sqlite3.connect(r'C:\Users\Raj\Anaconda3\Library\bin\movies.db')
    cursor=mycon.cursor()
    cursor.execute("UPDATE movies SET Movie_title=?,Director=?,Year=?,Category=?,Duration=? WHERE ID=?",(title,director,year,category,duration,Id))
    mycon.commit()
    resultset=cursor.fetchall()
    mycon.close()
