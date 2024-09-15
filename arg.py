import sys
argument=sys.argv
print(argument)
#print(argument[4])
#print(argument[3])
print(argument[2])
print(argument[1])
#print(argument[0])
print("length of arguments")
print(len(argument))
#print(argument[21])
na=argument[1]
nb=argument[2]
nc=argument[3]
sum=na+nb
print(sum)
print(type(na))
naa=int(na)
print(type(naa))
print(naa)
nbb=int(nb)
#print(naa+nbb)
ncc=int(nc)
print(naa+nbb+ncc)
storage=naa+nbb+ncc
store=storage%2
print(storage%2) 
if (store==0):
    print("even")
elif (store==1):
    print("odd")
else:
    print("incorrect input")

