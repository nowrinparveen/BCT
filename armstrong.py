a=int(input("enter the number"))
temp=a
sum=0
while a>0:
    r=a%10
    sum=sum+r*r*r
    a=int(a/10)
if temp==sum:
    print("its a armstrong number")
else:
        print("its not a armstrong number")







