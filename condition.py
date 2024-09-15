import sys

location="Bababadalgharaghtakamminarronnkonnbronntonnerronntu"
#location="Floccinaucinihilipilification"
#location="queen"
#location="Lorem ipsum, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
result=10
if(result>=90):
    print("WB") 
elif (result<90 and result>=50 ):
    print("WA")  
else:
    print("WT")

#print(len(location))     
length=len(location)  
print(length)
if(length==1):
    print("single")
elif (length>1 and length<=10):
    print("short")
elif (length>10 and length<=30):
    print("long")
else:
    print("extremely long")
check=86485485784758734567
store=check%2
print(check%2) 
if (store==0):
    print("even")
elif (store==1):
    print("odd")
else:
    print("incorrect input")
print(sys.maxsize)   
    
    
    
    
