import sqlite3

print("**************")
connection = sqlite3.connect('BitebyBite.db')
c = connection.cursor()


def ReadDatabase():
    print("Tables:\ningredients\nuser_status\nuser_password\n\n")
    table = input("Enter your table: ")
    sql = "select * from "
    for row in c.execute(sql+table):
        print(row)

def AddIngredient():
    product = input("Enter product name: ")
    cost = input("Enter product cost: ")
    costnm = float(cost)
    newproduct = (product, costnm)
    c.execute("insert into ingredients values (?,?)", newproduct)

def ChangePrice():
    c.execute("select * from ingredients")
    results = c.fetchall()
    print(results)
#print("******")
#c.execute("select * from ingredients")
#ingredients = c.fetchall()

#c.execute("select * from ingredients where name=:c", {"c": "Apples"})
#ApplesSearch = c.fetchall()
#print(ApplesSearch)

#print("**********")
#for i in ingredients:
#    if i[1] == "Apples":
#        price = i[0]
#        adprice = price + 1
#        print(price)


ReadDatabase()

ChangePrice()


























connection.commit()
connection.close()