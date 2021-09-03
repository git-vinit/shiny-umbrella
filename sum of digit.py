n=int(input("enter any number"))
i=0
while(n>0):
    digit=n%10
    i=i+digit
    n=n//10
print("the sum of digit ",i)
