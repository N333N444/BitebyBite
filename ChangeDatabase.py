import sqlite3
from flask import Flask, render_template
app = Flask(__name__)
counterlist = ["0","0","0","0","0"]


@app.route('/')
def index():
  return render_template('index.html', counters = counterlist)

print("**************")
connection = sqlite3.connect('BitebyBite.db', check_same_thread=False)
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

def AddToCart(productname, Currentquantity):
    #Search for your chosen product
    sql1 = '''SELECT * FROM ingredients WHERE name=:c'''
    sql2 = {"c": productname}
    c.execute(sql1, sql2)
    Productsearch = c.fetchall()
    productname = str(Productsearch[0][0])
    productprice = float(Productsearch[0][1])
    cartlist = (productname, productprice, Currentquantity)
    # check if the product is in the cart
    sql1 = '''SELECT * FROM cart WHERE name=:c'''
    sql2 = {"c": productname}
    c.execute(sql1, sql2)
    Productselect = c.fetchall()
    if len(Productselect) == 0:
        c.execute('''INSERT INTO cart VALUES (?,?,?)''', cartlist)
    else:
        sql1 = '''UPDATE cart SET quantity = '''
        sql2 = ''' WHERE name="'''
        sql3 = '''"'''
        c.execute(sql1 + str(Currentquantity) + sql2 + productname + sql3)

def RemoveFromCart(productname, Currentquantity):
    #Search for your chosen product
    sql1 = '''SELECT * FROM ingredients WHERE name=:c'''
    sql2 = {"c": productname}
    c.execute(sql1, sql2)
    if Currentquantity == 0:
        sql41 = '''DELETE FROM cart WHERE name="'''
        sql22 = '''"'''
        c.execute(sql41 + productname + sql22)
    else:
        sql1 = '''UPDATE cart SET quantity = '''
        sql2 = ''' WHERE name="'''
        sql3 = '''"'''
        c.execute(sql1 + str(Currentquantity) + sql2 + productname + sql3)

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


@app.route('/my-link/')

def pluscount():
    productname="Aspergus"
    sql1 = '''SELECT * FROM cart WHERE name=:c'''
    sql2 = {"c": productname}
    c.execute(sql1, sql2)
    Productselect = c.fetchall() # our tuple [(Aspergus, 2.3)]
    print("Plus count uitgevoerd")
    if len(Productselect) == 0:
        Currentquantity = 1
    else:
        quantity = Productselect[0][2]
        Currentquantity = quantity + 1
    AddToCart(productname, Currentquantity)
    counterlist[0] = str(Currentquantity)
    return render_template("index.html", counters = counterlist)

@app.route('/minus/')
def  mincount():
    productname="Aspergus"
    sql1 = '''SELECT * FROM cart WHERE name=:c'''
    sql2 = {"c": productname}
    c.execute(sql1, sql2)
    Productselect = c.fetchall() 
    if len(Productselect) == 0:
        Currentquantity = 0
    else:
        quantity = Productselect[0][2]
        Currentquantity = quantity - 1
        RemoveFromCart(productname, Currentquantity)
    counterlist[0] = str(Currentquantity)
    return render_template("index.html", counters = counterlist)

@app.route('/my-link2/')
def Pluscount():
    productname="Apples"
    sql1 = '''SELECT * FROM cart WHERE name=:c'''
    sql2 = {"c": productname}
    c.execute(sql1, sql2)
    Productselect = c.fetchall() # our tuple [(Aspergus, 2.3)]
    print("Plus count uitgevoerd")
    if len(Productselect) == 0:
        Currentquantity = 1
    else:
        quantity = Productselect[0][2]
        Currentquantity = quantity + 1
    AddToCart(productname, Currentquantity)
    counterlist[1] = str(Currentquantity)
    return render_template("index.html", counters = counterlist)

@app.route('/minus2/')
def  Mincount():
    productname="Apples"
    sql1 = '''SELECT * FROM cart WHERE name=:c'''
    sql2 = {"c": productname}
    c.execute(sql1, sql2)
    Productselect = c.fetchall() 
    if len(Productselect) == 0:
        Currentquantity = 0
    else:
        quantity = Productselect[0][2]
        Currentquantity = quantity - 1
        RemoveFromCart(productname, Currentquantity)
    counterlist[1] = str(Currentquantity)
    return render_template("index.html", counters = counterlist)

if __name__ == '__main__':
    app.run(debug=True)
    app.config['SERVER_NAME'] = "127.0.0.1:5000"
















# ReadDatabase()
connection.commit()
connection.close()