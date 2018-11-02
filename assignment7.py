no=int(input("enter any number"))
print("the given num is:",no)
rev=0
while no!=0:
    r=no%10
    no=no//10
    rev=(rev*10)+r
print("reverse is:",rev)
