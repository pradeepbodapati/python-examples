no=int(input("eneter the num:"))
sum=0
while no!=0:
    r=no%10
    no=no//10
    sum+=r
print("the sum is",sum)