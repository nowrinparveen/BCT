t= lambda n:n+t(n-1)
a=int(input("enter the number="))
print("sum is=:",t(a))
