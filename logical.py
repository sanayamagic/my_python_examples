"""
and logical operator
or logical operator
not logical operator
and
true and true evaluate to true
true and false evaluate to false
false and false evaluate to false
false and true evaluate to false
or
true or true evaluate to true
true or false evaluate to true
false or false evaluate to false
false or true evaluate to true
not
not true evaluates to false
not false evaluates to true
"""                         
print("and operator")
print(True and True)
print(True and False)
print(False and False)
print(False and True)
print("or operator")
print(True or True)
print(True or False)
print( not True or False or False or False or not False)
print(False or True)
print("not operator")
print(not True)
print(not False)
print("combining logical operators")
print(10>9 and 9==9)
print(10>9 or 9==9)
print(10>9 and 9!=9)
print((10>9 and 9==9) and (9>6 and 5==5))
if(10>9):
    print("greater") 
else:
    print("smaller")   