import sqlite3


#Tables: ingredients, user_status, user_password

def ReadDatabase():
    print("Tables:\ningredients\nuser_status\nuser_password\n\n")
    table = input("Enter your table: ")
    sql = "select * from "
    for row in c.execute(sql + table):
        print(row)


connection = sqlite3.connect("BitebyBite.db")
c = connection.cursor()

#Create the tables
c.execute("create table ingredients (name text, price real)")
c.execute("create table user_status (user text, status text)")
c.execute("create table user_password (user text, password text)")
c.execute("create table cart (name text, price real, quantity integer)")

#Make the list to put in the corresponding table in the database
list1 = [("MealboxVeganKap", 5.99),("WhiteAsparagus", 3.49),("GreenAsparagus", 3.49),("OrganicLeek", 0.69),("OrganicCarrots", 1.49),("OrganicRadish", 0.99),("PakSoi", 1.39),("RedOnions", 0.89),("ChineseCabbage", 1.49)]
list2 = [("Melvin", "logged_in"),("Nena", "logged_out")]
list3 = [("Melvin", "admin"),("Nena","admin")]

#populate the tables
c.executemany("insert into ingredients values (?,?)", list1)
c.executemany("insert into user_status values (?,?)", list2)
c.executemany("insert into user_password values (?,?)", list3)

connection.commit()
connection.close()