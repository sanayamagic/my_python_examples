from termcolor import colored
import sys
argument=sys.argv
print(argument) 
table=argument[1]
na=table
naa=int(na)
for count in range(1,11):
    communication=f" {count}x{naa}={count*naa}"
    number=count
    n2=naa
    answer=count*naa
    #print(communication)
    message=f"{colored(number,color="cyan")}x{colored(n2,color="light_blue")}={colored(answer,color="magenta")}"
    print(message)