import sys
argument=sys.argv
print(argument)
number=argument[1]
na=int(number)
for count in range(1,11):
    message=f"{na}x{count}={count*na}"
    print(message)

number2=argument[2]
nb=int(number2)
for count in range(1,11):
    message=f"{nb}x{count}={count*nb}"
    print(message)
    
number3=argument[3]
nc=int(number3)
for count in range(1,11):
    message=f"{nc}x{count}={count*nc}"
    print(message)
    