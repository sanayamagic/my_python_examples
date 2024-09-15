import sys
argument=sys.argv
print(argument)
print(len(argument))
if (len(argument)<5):
    print("minimum 4 numbers required")
    sys.exit()
print(argument[0])
print(argument[1])
print(argument[2])
print(argument[3])
#print(argument[4])
#print(argument[5])
#print(argument[6])
ma=argument[1]
mb=argument[2]
mc=argument[3]
md=argument[4]
maa=int(ma)
mbb=int(mb)
mcc=int(mc)
mdd=int(md)
storage=maa+mbb+mcc+mdd
store=storage%2
print(storage%2)
if (store==0):
   print("even")
elif (store==1):   
    print("odd") 
else:
    print("wrong input") 
print(sys.maxsize)
