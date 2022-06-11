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
    #These are our products:
    print(results)
    productlist = []
    for i in results:
        product = i[0]
        productlist.append(product)
    print(productlist)

    #Search for your chosen product
    productselect = input("select a product: ")
    sql1 = "select * from ingredients where name=:c"
    sql2 = {"c": productselect}
    c.execute(sql1, sql2)
    Productsearch = c.fetchall() # our tuple [(Aspergus, 2.3)]


    #repeat is necessary : old productsearch
    sql1 = "select * from ingredients where name=:c"
    sql2 = {"c": productselect}
    c.execute(sql1, sql2)
    OldProductsearch = c.fetchall() # our tuple [(Aspergus, 2.3)]

    currentprice = Productsearch[0][1]
    print(f"The current price of this product is: {currentprice}")
    print(Productsearch)
    
    #replace price
    chosenprice = input("Choose a new price: ")
    oldprice = list(Productsearch[0]) #make the the currenct tupple a [Aspergus, 2.3]
    oldprice[1] = chosenprice # change the price in the list with the chosenprice [Aspergus, 2.6]
    NewProductsearch = Productsearch
    NewProductsearch[0] = tuple(oldprice) # change the list back into a tuple [(Aspergus, 2.6)]

    #replace in table
    c.execute("select * from ingredients")
    ingredient = c.fetchall()
    print(ingredient)
    
    for i in ingredient:
        
        print(i)
        newingredient = [NewProductsearch[0] if value==OldProductsearch[0] else value for value in i]
        print(newingredient)

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

ChangePrice()
print("You have changed the price")
ReadDatabase()















connection.commit()
connection.close()