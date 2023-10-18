#CALCULATOR
val1 = int(input("Enter First No."))
val2 = int(input("Enter Second No."))   
operator = input (' enter op')
if operator in [ '+' ]:
    add=val1+val2 
    print ("ADD = ",add)   
elif operator in [ '*' ]:
    multi=val1*val2 
    print ("Multiply = ",multi)    
elif operator in [ '/' ]:
    div=val1/val2 
    print ("Divide = ",div)  
elif operator in [ '-' ]:
    subt=val1-val2 
    print ("Subtract = ",subt) 
else:
    print("Fuck U")