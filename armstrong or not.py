num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
term = num
while term > 0:
   digit = term % 10
   sum += digit ** 3
   term//= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
