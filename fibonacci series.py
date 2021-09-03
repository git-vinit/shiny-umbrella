i= int(input("How many terms? "))

# first two terms
n1=0
n2=1
count = 0

# check if the number of terms is valid
if (i <= 0):
   print("Please enter a positive integer")
elif (i == 1):
   print("Fibonacci sequence upto",i)
   print(n1)
else:
   print("Fibonacci sequence:")
   while (count < i):
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
