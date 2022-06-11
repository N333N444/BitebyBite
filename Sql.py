import sqlite3


#Tables: ingredients, user_status, user_password

connection = sqlite3.connect("BitebyBite.db")
c = connection.cursor()
c.execute("create table ingredients (name text, price real)")
c.execute("create table user_status (user text, status text)")
c.execute("create table user_password (user text, password text)")

#Make the list and put them in a table in the database
list1 = [("Aspergus", 2.30),("Apples", 3.30),("Apples", 4.50)]
list2 = [("Melvin", "logged_in"),("Nena", "logged_out")]
list3 = [("Melvin", "admin"),("Nena","admin")]

c.executemany("insert into ingredients values (?,?)", list1)
c.executemany("insert into user_status values (?,?)", list2)
c.executemany("insert into user_password values (?,?)", list3)

connection.close()