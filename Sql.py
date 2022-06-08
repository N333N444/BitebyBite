import sqlite3


connection = sqlite3.connect("BitebyBite.db")
c = connection.cursor()
#c.execute("create table ingredients (price real, name text)")



list1 = [(2.30, "Aspergus"),(3.30, "Apples"),(4.50, "Apples")]
list2 = [("logged_in", "Melvin"),("logged_out", "Nena")]


c.executemany("insert into ingredients values (?,?)", list1)

for row in c.execute("select * from ingredients"):
    print(row)
print("******")
c.execute("select * from ingredients")
ingredients = c.fetchall()

c.execute("select * from ingredients where name=:c", {"c": "Apples"})
ApplesSearch = c.fetchall()
print(ApplesSearch)

print("**********")
for i in ingredients:
    if i[1] == "Apples":
        price = i[0]
        adprice = price + 1
        ingredients[i][0] = [adprice if 3.30]
        print(price)

    
    
    
    #if ingredients[i][1] == "Apples":
    #    ingredients[i][0] = 4.60, "Apples"











connection.close()