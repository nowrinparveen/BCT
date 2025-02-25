def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y
def div(x,y):
    return (x/y)
def pow(x,y):
    return x**y





print("please select the operation you want to perform\n"\
      "1.add\n"\
        "2.subtract\n"\
            "3.multiply\n"\
                "4.divide\n"\
                    "5.power\n")
select= int (input("select operations from 1,2,3,4,5:"))
x=int(input("enter the first number"))
y=int(input("enter the second number"))
if select==1:
    ans=add(x,y)
elif select==2:
    ans=sub(x,y)
elif select==3:
    ans=mul(x,y)
elif select==4:
    ans=div(x,y)
elif select==5:
    ans=pow(x,y)
else :print("invalid input")

print(ans)
