import sys
argument=sys.argv
print(argument)
print(len(argument))
if (len(argument)<5):
    message=f"minimum 4 numbers required. but you have supplied {len(argument)-1} numbers. we need to initialize remaining numbers with 0"
    print(message)
    if (len(argument)<2):
        argument=["arg3.py",0,0,0,0]
    if (len(argument)<3):
        argument=["arg3.py",argument[1],0,0,0]
    if (len(argument)<4):
        argument=["arg3.py",argument[1],argument[2],0,0]
    if (len(argument)<5):
        argument=["arg3.py",argument[1],argument[2],argument[3],0]
  #  sys.exit()
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
