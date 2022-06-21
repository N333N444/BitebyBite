import sqlite3
from flask import Flask, render_template
app = Flask(__name__)
counterlist = ["0","0","0","0","0","0","0","0"]


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/Product.html/')
def productpage():
    return render_template('Product.html', counters = counterlist)

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
    print(productname)
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

def pluscount(productname,i):
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
    counterlist[i] = str(Currentquantity)
    

def  mincount(productname, i):
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
    counterlist[i] = str(Currentquantity)
    



@app.route('/pwa/')
def pwa():
    pluscount('WhiteAsparagus', 0)
    return render_template("Product.html", counters = counterlist)
@app.route('/mwa/')
def mwa():
    mincount('WhiteAsparagus', 0)
    return render_template("Product.html", counters = counterlist)

@app.route('/pga/')
def pga():
    pluscount('GreenAsparagus', 1)
    return render_template("Product.html", counters = counterlist)
@app.route('/mga/')
def mga():
    mincount('GreenAsparagus', 1)
    return render_template("Product.html", counters = counterlist)

@app.route('/pol/')
def pol():
    pluscount('OrganicLeek', 2)
    return render_template("Product.html", counters = counterlist)
@app.route('/mol/')
def mol():
    mincount('OrganicLeek', 2)
    return render_template("Product.html", counters = counterlist)

@app.route('/poc/')
def poc():
    pluscount('OrganicCarrots', 3)
    return render_template("Product.html", counters = counterlist)
@app.route('/moc/')
def moc():
    mincount('OrganicCarrots', 3)
    return render_template("Product.html", counters = counterlist)

@app.route('/por/')
def por():
    pluscount('OrganicRadish', 4)
    return render_template("Product.html", counters = counterlist)
@app.route('/mor/')
def mor():
    mincount('OrganicRadish', 4)
    return render_template("Product.html", counters = counterlist)

@app.route('/pps/')
def pps():
    pluscount('PakSoi', 5)
    return render_template("Product.html", counters = counterlist)
@app.route('/mps/')
def mps():
    mincount('PakSoi', 5)
    return render_template("Product.html", counters = counterlist)

@app.route('/pro/')
def pro():
    pluscount('RedOnions', 6)
    return render_template("Product.html", counters = counterlist)
@app.route('/mro/')
def mro():
    mincount('RedOnions', 6)
    return render_template("Product.html", counters = counterlist)

@app.route('/pcc/')
def pcc():
    pluscount('ChineseCabbage', 7)
    return render_template("Product.html", counters = counterlist)
@app.route('/mcc/')
def mcc():
    mincount('ChineseCabbage', 7)
    return render_template("Product.html", counters = counterlist)


if __name__ == '__main__':
    app.run(debug=True)
    app.config['SERVER_NAME'] = "127.0.0.1:5000"
















# ReadDatabase()
connection.commit()
connection.close()