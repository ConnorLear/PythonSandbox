def p(ape):
    print(ape)

#What math is wanting to be done
p("""What math is wanted to be done!:
  
A. Adding
B. Subtracting
C. Multiplication
D. Divition
E. Variable
D. Exponent 
F. Multiple Problems
""")

"""
person = p
math = m
# = problem number
n = problem letter
d = decimal
"""


import math

#Persons answer
pm = input().lower()
p("")

#Addition
if pm == "a":
    lista =[]
    x1 = int(input("How many numbers are their to Add: "))
    y1 = str(input("Is one of your numbers a decimal(y/n): "))
    p("")
    p("What numbers:")
    if y1 == "y":
        for i in range(x1):
            y2 = float(input(">"))
            lista.append(y2)
        print("Answer: ",sum(lista))
    else:
        for i in range(x1):
            y2 = int(input(">"))
            lista.append(y2)
        print("Answer: ",sum(lista))

#Subtraction
elif pm == "b":
    lista =[]
    x1 = int(input("How many numbers are their to Subtract: "))
    y1 = str(input("Is one of your numbers a decimal(y/n):" ))
    p("")
    p("What numbers:")
    if y1 == "y":
        for i in range(x1):
            y2 = float(input(">"))
            lista.append(y2)
        print("Answer: ",zip(lista))
    else:
        for i in range(x1):
            y2 = int(input(">"))
            lista.append(y2)
        print("Answer: ",zip(lista))

#Multpication 
elif pm == "c":
    lista =[]
    x1 = int(input("How many numbers are their to Multiply: "))
    y1 = str(input("Is one of your numbers a decimal(y/n):" ))
    p("")
    p("What numbers:")
    if y1 == "y":
        for i in range(x1):
            y2 = float(input(">"))
            lista.append(y2)
        print("Answer: ",math.prod(lista))
    else:
        for i in range(x1):
            y2 = int(input(">"))
            lista.append(y2)
        print("Answer: ",math.prod(lista))

#Divition
elif pm == "d":
    lista =[]
    x1 = int(input("How many numbers are their to Divide: "))
    p("")
    p("What numbers:")
    for i in range(x1):
        y2 = float(input(">"))
            lista.append(y2)
        print("Answer: ",divmod(lista))
    else:
        for i in range(x1):
            y2 = int(input(">"))
            lista.append(y2)
        print("Answer: ",divmod(lista))

#Variables    
elif pm == "e":
    p("")
elif pm == "f":
    p("")
elif pm == "g":
    p("")
else:
    p("""That's not an option.
Try again""")


p("")