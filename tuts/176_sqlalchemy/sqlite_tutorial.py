

"""
https://docs.python.org/3/library/sqlite3.html

Run this as a standalone Python module.

How-to guides for further reading:

        How to use placeholders to bind values in SQL queries

        How to adapt custom Python types to SQLite values

        How to convert SQLite values to custom Python types

        How to use the connection context manager

        How to create and use row factories

        Explanation for in-depth background on transaction control.
"""

import sqlite3
con = sqlite3.connect("tutorial.db")    # IMPLICITLY CREATES DB IF DOESN'T ALREADY EXIST.

# In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor. Call con.cursor() to create the Cursor:

cur = con.cursor()

# create a database table called "movie" with columns for title, release year, and review score. Thanks to the flexible typing feature of SQLite, specifying the data types is optional

try:
    cur.execute("CREATE TABLE movie(title, year, score)") 
except:
    pass 
    
# verify that the new table has been created by querying the "sqlite_master" table built-in to SQLite, which should now contain an entry for the movie table definition

res = cur.execute("SELECT name FROM sqlite_master")

print(res.fetchone())	# fetch the resulting row.

# look for a table that doesn't exist.
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
print(res.fetchone())

# add 2 rows of data to the table
# INSERT statement implicitly opens a transaction, which needs to be committed before changes are saved in the database
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit() 

# verify that the data was inserted correctly by executing a SELECT query. 
res = cur.execute("SELECT score FROM movie")
print(res.fetchall() )       # fetch all rows.

# insert three more rows by calling cur.executemany(...) 
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.

# Notice that ? placeholders are used to bind data to the query. Always use placeholders instead of string formatting to bind Python values to SQL statements, to avoid SQL injection attacks (see How to use placeholders to bind values in SQL queries for more details).


# We can verify that the new rows were inserted by executing a SELECT query, this time iterating over the results of the query:
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

# Finally, verify that the database has been written to disk by calling con.close() to close the existing connection, opening a new one, creating a new cursor, then querying the database:
con.close()

new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()

print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
new_con.close()



