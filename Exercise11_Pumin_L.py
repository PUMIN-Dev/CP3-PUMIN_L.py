amount = int(input("Enter Amount : "))
for a in range(amount) :
    print(" "*((amount-1)-a)+"*"*(((a*1)+1)+a))