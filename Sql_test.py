#Creating an SQL database using Python.   This code opens up a basic SQL database and facilitates
#the addition of field entries into the database.  To view the entries in the actual database,
#an SQL database platform is required.  I have used the SQLite manager in Firefox to view the database
#entries I have created here.


#Import the Sqlite and the Sqlalchemy modules.
#These modules allow one to set up an sql database locally using Python
import sqlite3
import sqlalchemy



#Create a connection to a new database using the connect command.
conn = sqlite3.connect('example.db')



#Create a cursor object.  The cursor allows people to traverse and manipulate records
#in the database result set.
cur = conn.cursor()



#Using the cursor, we need to use the execute statement to create
#an SQL command.  In this command, SQL is used to create new entries in the data base in
#brackets.  The table called Cars is first created in the data base, and the car entries
#are then inserted into the table using SQL.  Various headings for each entry are created,
#including the entry ID, car name (as text) and car price (as an integer).  This is all done
#using SQL.
cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")


#Commit all these new entries to the database and then close the database.
conn.commit()
conn.close()

