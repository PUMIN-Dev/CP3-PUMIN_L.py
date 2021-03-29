menuList = []
priceList = []
def showList() :
    print("-----Hello-----")
    for i in range(len(menuList)) :
        print(i+1,".",menuList[i],":",priceList[i],"THB")
    print("Total Price:",sum(priceList))
while True :
    menu = input("Please Enter Menu : ")
    if (menu.lower() == "exit") :
        break
    price = input("Plase Enter Price : ")
    menuList.append(menu)
    priceList.append(int(price))
showList()




