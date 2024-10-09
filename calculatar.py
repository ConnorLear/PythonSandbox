def p(ape):
    print(ape)

#What math is wanting to be done
p("""What math is wanted to be done!:
  
A. Adding
B. Subtracting
C. Multiplication
D. Divition
E. Geometry
F. Algebra
G. Variable
""")

"""
person = p
math = m
# = problem number
n = problem letter
d = decimal
"""

#Persons answer
pm = input().lower()
p("")

#Addition
if pm == "a":
    lista =[]
    n1 = (input("How many numbers are their to add and is there a decimal(y/n): "))
    x1, y1 = n1.split()
    p("")
    p("What numbers:")
    if y1 == "y":
        
        for i in range(x1):
            y2 = float(input())
            
    else:
        print("")        


elif pm == "b":
    p("")
elif pm == "c":
    p("")
elif pm == "d":
    p("")
elif pm == "e":
    p("")
elif pm == "f":
    p("")
elif pm == "g":
    p("")
else:
    p("""That's not an option.
Try again""")
