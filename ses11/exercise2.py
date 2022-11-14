#Context manager class
#Create a class “Makeparagraph” that “decorates” a text with an html <p> tag.



#Contextlib
#In the code example below we can se that the connect() function is a context manager.
# It has an __enter__ and an __exit__ method, and therefore works together with the “with” keyword.

from sqlite3 import connect

with connect('testfiles/school.db') as conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE students(id int PRIMARY KEY, name text, cpr text)')
    cur.execute('INSERT INTO students(id, name, cpr) VALUES (1, "Claus", "223344-5566")')
    cur.execute('INSERT INTO students(id, name, cpr) VALUES (2, "Julie", "111111-1111")')
    cur.execute('INSERT INTO students(id, name, cpr) VALUES (3, "Hannah", "222222-2222")')

    for i in cur.execute('SELECT * FROM students'):
        print(i)

    cur.execute('DROP TABLE students')



from contextlib import contextmanager

@contextmanager
def connect():
    f = open('testfiles/school.db')
    yield f
    f.close()