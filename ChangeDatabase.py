import sqlite3

print("**************")
connection = sqlite3.connect('BitebyBite.db')
c = connection.cursor()

def ReadDatabase():
    c.execute('''SELECT name FROM sqlite_schema''')
    listoftables = c.fetchall()
    print("Tables:")
    for i in listoftables:
        print(i[0])
    #print("Tables:\ningredients\nuser_status\nuser_password\ncart\n\n")
    table = input("Enter your table: ")
    sql = '''SELECT * FROM '''
    c.execute(sql+table)
    selectedtable = c.fetchall()
    for row in selectedtable:
        print(row)

def AddIngredient():
    product = input("Enter product name: ")
    cost = input("Enter product cost: ")
    costnm = float(cost)
    newproduct = (product, costnm)
    c.execute('''INSERT INTO ingredients values (?,?)", newproduct''')

def AddToCart():
    c.execute('''SELECT * FROM ingredients''')
    results = c.fetchall()
    print(results)
    #Search for your chosen product
    chosenproduct = input("Select a product: ")
    sql1 = '''SELECT * FROM ingredients WHERE name=:c'''
    sql2 = {"c": chosenproduct}
    c.execute(sql1, sql2)
    Productsearch = c.fetchall() # our tuple [(Aspergus, 2.3)]
    productname = str(Productsearch[0][0])
    productprice = float(Productsearch[0][1])
    productquantity = int(input("How many do you want? "))
    cartlist = (productname, productprice, productquantity)
    print(type(cartlist))
    #print(NewCartProduct)
    c.execute("insert into cart values (?,?,?)", cartlist)

def RemoveFromCart():
    c.execute('''SELECT * FROM cart''')
    results = c.fetchall()
    print(results)
    #Search for your chosen product
    chosenproduct = input("Select a product to remove: ")
    sql1 = '''SELECT * FROM ingredients WHERE name=:c'''
    sql2 = {"c": chosenproduct}
    c.execute(sql1, sql2)
    Productsearch = c.fetchall() # our tuple [(Aspergus, 2.3, 4)]
    productname = Productsearch[0][0]
    sql41 = '''DELETE FROM cart WHERE name="'''
    sql22 = '''"'''
    c.execute(sql41 + productname + sql22)

def ChangePrice():
    #These are our products:
    c.execute('''SELECT * FROM ingredients''')
    results = c.fetchall()
    print(results)

    #Search for your chosen product
    productselect = input("Select a product: ")
    sql1 = '''SELECT * FROM ingredients WHERE name=:c'''
    sql2 = {"c": productselect}
    c.execute(sql1, sql2)
    Productsearch = c.fetchall() # our tuple [(Aspergus, 2.3)]

    #show current price
    currentprice = Productsearch[0][1]
    print(f"The current price of this product is: {currentprice}")
    
    #replace price
    chosenprice = input("Choose a new price: ")
    
    #UPDATE the table "ingredients"
    sql20 = '''UPDATE ingredients SET price = '''
    sql21 = ''' WHERE name="'''
    sql22 = '''"'''
    c.execute(sql20 + chosenprice + sql21 + productselect + sql22)

def CalcFinalPrice():
    c.execute('''SELECT * FROM cart''')
    results = c.fetchall()
    print(results)
    totalprice = 0
    for i in results:
        totalprice = totalprice + (i[1] * i[2])    
    return totalprice

#var = CalcFinalPrice()
#print(var)
















connection.commit()
connection.close()