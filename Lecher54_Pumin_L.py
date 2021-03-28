def login():
    username = input("Username : ")
    password = input("Password : ")
    if username == "pumin" and password == "1pp" :
        return True
    else :
        return False
def showMenu():
    print("***** PUMIN SHOP *****")
    print("1.Vat Calculater")
    print("2.Price Calculater")
def menuSelect():
    menuSelect = int(input("Select Menu : "))
    return menuSelect
def vatCalcurate(price):
    return price + (price*0.07)
def priceCalculate():
    price1 = int(input("Frist Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalcurate(price1+price2)

while login() != True :
    print("Username or Password is False !")
showMenu()
x = menuSelect()
if x == 1 :
    price = int(input("Enter Price : "))
    print(vatCalcurate(price))
if x == 2 :
        print(priceCalculate())



