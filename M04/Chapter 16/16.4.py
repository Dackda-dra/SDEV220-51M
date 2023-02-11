

#assignment 16

import sqlite3 

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE IF NOT EXISTS books
    (title PRIMARY KEY,
     author STR,
     year INT)''')
    
curs.execute('INSERT INTO books VALUES("The Weirdstone of Brisingamen", "Alan Garner", 1960)')
curs.execute('INSERT INTO books VALUES("Perdido Street Station", "China Miéville" , 2000)')
curs.execute('INSERT INTO books VALUES("Thud!", "Terry Pratchett", 2005)')
curs.execute('INSERT INTO books VALUES("The Spellman Files", "Lisa Lutz", 2007)')
curs.execute('INSERT INTO books VALUES("Small Gods", "Terry Pratchett", 1992)')


selectQuery = 'Select title FROM books ORDER BY title ASC'
cursor = curs.execute(selectQuery)

curs.execute('Select title FROM books ORDER BY title ASC')
for row in cursor:
   print(row[0])
