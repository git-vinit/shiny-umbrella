
your_ans=""
number_of_try=0
number_of_max_try=8
max_try="not reached"

while your_ans!=our_password and max_try!="Reached":
    if number_of_try<number_of_max_try:
        your_ans= input("what is the password")
        number_of_try=number_of_try+1
    else:
        max_try ="Reached"
        
if max_try=="Reached":
    print("account blocked")
else:
    print("access granted")

























