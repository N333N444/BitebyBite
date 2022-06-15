import sqlite3

print("**************")
connection = sqlite3.connect('BitebyBite.db')
c = connection.cursor()


def ReadDatabase():
    print("Tables:\ningredients\nuser_status\nuser_password\n\n")
    table = input("Enter your table: ")
    sql = '''SELECT * FROM '''
    for row in c.execute(sql+table):
        print(row)

def AddIngredient():
    product = input("Enter product name: ")
    cost = input("Enter product cost: ")
    costnm = float(cost)
    newproduct = (product, costnm)
    c.execute('''INSERT INTO ingredients values (?,?)", newproduct''')

def ChangePrice():
    c.execute('''SELECT * FROM ingredients''')
    results = c.fetchall()
    #These are our products:
    print(results)
    productlist = []
    for i in results:
        product = i[0]
        productlist.append(product)
    print(productlist)

    #Search for your chosen product
    productselect = input("SELECT a product: ")
    sql1 = '''SELECT * FROM ingredients WHERE name=:c'''
    sql2 = {"c": productselect}
    c.execute(sql1, sql2)
    Productsearch = c.fetchall() # our tuple [(Aspergus, 2.3)]

    currentprice = Productsearch[0][1]
    print(f"The current price of this product is: {currentprice}")
    print(Productsearch)
    
    #replace price
    chosenprice = input("Choose a new price: ")

    #replace in table
    c.execute('''SELECT * FROM ingredients''')
    ingredient = c.fetchall()
    print(ingredient)
    
    sql20 = '''UPDATE ingredients SET price = '''
    sql21 = ''' WHERE name="'''
    sql22 = '''"'''
    c.execute(sql20 + chosenprice + sql21 + productselect + sql22)

ChangePrice()
print("You have changed the price")
ReadDatabase()















connection.commit()
connection.close()