import sys
argument=sys.argv
print(argument) 
table=argument[1]
n1=argument[2]
n2=argument[3]
na=table
n11=int(n1)
n22=int(n2)
naa=int(na)
for count in range(n11,n22+1):
    communication=f" {naa}x{count}={count*naa}"
    print(communication)