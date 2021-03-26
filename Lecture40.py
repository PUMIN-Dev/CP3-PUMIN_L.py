username = input("Username : ")
password = input("Password : ")
if username == "pumin" and password == "11" :
    print("--- Welcome To PUMIN SHOP ---")
    print("1.Banana Price 10(THB)")
    print("2.Orange Price 20(THB)")
    print("3.Mango  Price 30(THB)")
    print("Would you wont to order")
    a = input("Put Y if you want to order : ")
    if a == "Y" :
        b = input("Produc Code : ")
        c = int(input("Required Amount : "))
        if b == "1" :
            print("ToTal Price :",10*c,"(THB)")
        if b == "2" :
            print("Total Price :",20*c,"(THB)")
        if b == "3" :
            print("Total Price :",30*c,"(THB)")
        if b!= "1" and b!="2" and b!=3 :
            print("Don't have this Produc Code")
            print("Googbye")
    else  :
        print("Goodbye")



