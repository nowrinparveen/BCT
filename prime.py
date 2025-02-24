a=int(input("enter the number"))
fact=0
if a>1:
    for i in range (1,a+1):
        if a%i==0:
            fact=fact+1
            if fact>2:
                print("this is a not prime")

    if fact==2:
        print("this is a prime number")

else:
    print("this is not a prime number")
                



