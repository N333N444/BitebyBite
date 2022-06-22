import sqlite3


# Tables: ingredients, user_status, user_password

def ReadDatabase():
    print("Tables:\ningredients\nuser_status\nuser_password\n\n")
    table = input("Enter your table: ")
    sql = "select * from "
    for row in c.execute(sql + table):
        print(row)


connection = sqlite3.connect("BitebyBite.db")
c = connection.cursor()

# Create the tables
c.execute("create table ingredients (name text, price real)")
c.execute("create table user_status (user text, status text)")
c.execute("create table user_password (user text, password text)")
c.execute("create table cart (name text, price real, quantity integer)")
c.execute("create table mbcounter (name text, amount integer)")

# Make the list to put in the corresponding table in the database
list1 = [("MealboxVeganKap", 5.99), ("White_Asparagus", 3.49), ("Green_Asparagus", 3.49), ("Chinese_Cabbage", 1.49),
         ("Pak_Soi", 1.39), ("Organic_Radish", 0.99), ("Organic_Carrots", 1.49), ("Bananas", 1.29), ("Walnuts", 2.49)]
list2 = [("Melvin", "logged_in"), ("Nena", "logged_out")]
list3 = [("Melvin", "admin"), ("Nena", "admin")]
list4 = [("MealboxVeganKap", 1)]

# populate the tables
c.executemany("insert into ingredients values (?,?)", list1)
c.executemany("insert into user_status values (?,?)", list2)
c.executemany("insert into user_password values (?,?)", list3)
c.executemany("insert into mbcounter values (?,?)", list4)

connection.commit()
connection.close()
