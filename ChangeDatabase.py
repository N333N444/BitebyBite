import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
counterlist = ["0", "0", "0", "0", "0", "0", "0", "0"]
mbcounterlist = ["1", "1", "1", "1", "1", "1", "1", "1"]
counterVal = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('templates/Product.html/')
def productpage():
    return render_template('templates/Product.html', counters=counterlist)


@app.route('/cart/')
def cart():
    totalprice = CalcFinalPrice()
    productlist = ReadCartInfo()
    return render_template('Shoppingcart.html', productlist=productlist, total=totalprice)


@app.route('/About_us.html/')
def About():
    return render_template('About_us.html')


@app.route('/Dishes.html/')
def Dishes():
    return render_template('Dishes.html')


@app.route('/VeganKap.html/')
def vegankapdish():
    return render_template('VeganKap.html', mbcounter=mbcounterlist)


@app.route('/omvk/', methods=['POST'])
def omvk():
    quantity = request.form.get('Val')
    print("deze:", quantity)
    AddToCart("MealboxVeganKap", quantity)
    return render_template("Shoppingcart.html")


print("**************")
connection = sqlite3.connect('BitebyBite.db', check_same_thread=False)
c = connection.cursor()


def ReadCartInfo():
    table = "cart"
    sql = '''SELECT * FROM '''
    c.execute(sql+table)
    selectedtable = c.fetchall()
    for i in range(0, len(selectedtable)):
        x = list(selectedtable[i])  # make (asp, 1.0,0) a list
        z = str(x[0])  # make asp a sting
        y = z.replace("_", " ")
        print(y)  # replace string
        x[0] = y  # replace asp with correct word in list
        print(x)
        selectedtable[i] = tuple(x)
    productlist = selectedtable
    return productlist


def ReadDatabase():
    c.execute('''SELECT name FROM sqlite_schema''')
    listoftables = c.fetchall()
    print("Tables:")
    for i in listoftables:
        print(i[0])
    # print("Tables:\ningredients\nuser_status\nuser_password\ncart\n\n")
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
    # Search for your chosen product
    sql1 = '''SELECT * FROM ingredients WHERE name=:c'''
    sql2 = {"c": productname}
    c.execute(sql1, sql2)
    Productsearch = c.fetchall()
    productname = str(Productsearch[0][0])

    productprice = Currentquantity * float(Productsearch[0][1])
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
        sql4 = '''UPDATE cart SET price = '''
        c.execute(sql4 + str(productprice) + sql2 + productname + sql3)


def RemoveFromCart(productname, Currentquantity):
    # Search for your chosen product
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
    # These are our products:
    c.execute('''SELECT * FROM ingredients''')
    results = c.fetchall()
    print(results)

    # Search for your chosen product
    productselect = input("Select a product: ")
    sql1 = '''SELECT * FROM ingredients WHERE name=:c'''
    sql2 = {"c": productselect}
    c.execute(sql1, sql2)
    Productsearch = c.fetchall()  # our tuple [(Aspergus, 2.3)]

    # show current price
    currentprice = Productsearch[0][1]
    print(f"The current price of this product is: {currentprice}")

    # replace price
    chosenprice = input("Choose a new price: ")

    # UPDATE the table "ingredients"
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
        totalprice = float(totalprice + i[1])
    totalprice = "%.2f" % totalprice
    return totalprice


def pluscount(productname, i):
    sql1 = '''SELECT * FROM cart WHERE name=:c'''
    sql2 = {"c": productname}
    c.execute(sql1, sql2)
    Productselect = c.fetchall()  # our tuple [(Aspergus, 2.3)]
    if len(Productselect) == 0:
        Currentquantity = 1
    else:
        quantity = Productselect[0][2]
        Currentquantity = quantity + 1
    AddToCart(productname, Currentquantity)
    counterlist[i] = str(Currentquantity)


def mincount(productname, i):
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


def mbmincount(productname, i):
    sql1 = '''SELECT * FROM mbcounter WHERE name=:c'''
    sql2 = {"c": productname}
    c.execute(sql1, sql2)
    Mbselect = c.fetchall()
    if Mbselect[0][1] > 1:
        Currentquantity = Mbselect[0][1] - 1
        mbcounterlist[i] = Currentquantity
        sql1 = '''UPDATE mbcounter SET amount  = '''
        sql2 = ''' WHERE name="'''
        sql3 = '''"'''
        c.execute(sql1 + str(Currentquantity) + sql2 + productname + sql3)


def mbpluscount(productname, i):
    sql1 = '''SELECT * FROM mbcounter WHERE name=:c'''
    sql2 = {"c": productname}
    c.execute(sql1, sql2)
    Mbselect = c.fetchall()
    Currentquantity = Mbselect[0][1] + 1
    mbcounterlist[i] = Currentquantity
    sql1 = '''UPDATE mbcounter SET amount  = '''
    sql2 = ''' WHERE name="'''
    sql3 = '''"'''
    c.execute(sql1 + str(Currentquantity) + sql2 + productname + sql3)
    print(mbcounterlist[i])


@app.route('/pmb/')
def pmb():
    productname = "MealboxVeganKap"
    mbpluscount(productname, 0)
    return render_template("VeganKap.html", mbcounter=mbcounterlist)


@app.route('/mmb/')
def mmb():
    productname = "MealboxVeganKap"
    mbmincount(productname, 0)
    return render_template("VeganKap.html", mbcounter=mbcounterlist)


@app.route('/pwa/')
def pwa():
    pluscount('White_Asparagus', 0)
    return render_template("Product.html", counters=counterlist)


@app.route('/mwa/')
def mwa():
    mincount('White_Asparagus', 0)
    return render_template("Product.html", counters=counterlist)


@app.route('/pga/')
def pga():
    pluscount('Green_Asparagus', 1)
    return render_template("Product.html", counters=counterlist)


@app.route('/mga/')
def mga():
    mincount('Green_Asparagus', 1)
    return render_template("Product.html", counters=counterlist)


@app.route('/pol/')
def pol():
    pluscount('Chinese_Cabbage', 2)
    return render_template("Product.html", counters=counterlist)


@app.route('/mol/')
def mol():
    mincount('Chinese_Cabbage', 2)
    return render_template("Product.html", counters=counterlist)


@app.route('/poc/')
def poc():
    pluscount('Pak_Soi', 3)
    return render_template("Product.html", counters=counterlist)


@ app.route('/moc/')
def moc():
    mincount('Pak_Soi', 3)
    return render_template("Product.html", counters=counterlist)


@ app.route('/por/')
def por():
    pluscount('Organic_Radish', 4)
    return render_template("Product.html", counters=counterlist)


@ app.route('/mor/')
def mor():
    mincount('Organic_Radish', 4)
    return render_template("Product.html", counters=counterlist)


@ app.route('/pps/')
def pps():
    pluscount('Organic_Carrots', 5)
    return render_template("Product.html", counters=counterlist)


@ app.route('/mps/')
def mps():
    mincount('Organic_Carrots', 5)
    return render_template("Product.html", counters=counterlist)


@ app.route('/pro/')
def pro():
    pluscount('Bananas', 6)
    return render_template("Product.html", counters=counterlist)


@ app.route('/mro/')
def mro():
    mincount('Bananas', 6)
    return render_template("Product.html", counters=counterlist)


@ app.route('/pcc/')
def pcc():
    pluscount('Walnuts', 7)
    return render_template("Product.html", counters=counterlist)


@ app.route('/mcc/')
def mcc():
    mincount('Walnuts', 7)
    return render_template("Product.html", counters=counterlist)


if __name__ == '__main__':
    app.run(debug=True)
    app.config['SERVER_NAME'] = "127.0.0.1:5000"


connection.commit()
connection.close()
