import sqlalchemy as sa
from sqlalchemy import select

#conn = sa.create_engine('sqlite:///C:\SDEV220\M04\M04 Programming Assignments\Chapter 16\books.db')
conn = sa.create_engine('sqlite:///books.db')
meta = sa.MetaData()
books = ('books.db')

conn.execute('''CREATE TABLE IF NOT EXISTS books
    (title PRIMARY KEY,
     author STR,
     year INT)''')
    
conn.execute('INSERT INTO books VALUES("The Weirdstone of Brisingamen", "Alan Garner", 1960)')
conn.execute('INSERT INTO books VALUES("Perdido Street Station", "China Miéville" , 2000)')
conn.execute('INSERT INTO books VALUES("Thud!", "Terry Pratchett", 2005)')
conn.execute('INSERT INTO books VALUES("The Spellman Files", "Lisa Lutz", 2007)')
conn.execute('INSERT INTO books VALUES("Small Gods", "Terry Pratchett", 1992)')


selectQuery = 'Select title FROM books ORDER BY title ASC'
cursor = conn.execute(selectQuery)

conn.execute('Select title FROM books ORDER BY title ASC')
for row in cursor:
   print(row[0])
