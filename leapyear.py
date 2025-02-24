a=int(input("enter the year"))

if a%4==0 and (a%400==0 or a%100!=0):
    print("this is a leap year")
else: print("this is not a leap year")