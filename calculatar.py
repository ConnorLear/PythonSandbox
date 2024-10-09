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
""")

"""
person = p
math = m
# = problem number
n = problem letter
d = decimal
"""

pm = input().lower()

p("")

if pm == "a":
    n1 = (input("How many numbers are their to add and is there a decimal: "))
    x1, y1 = n1.split()
    p(x1)
    p(y1)


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
else:
    p("""That's not an option.
Try again""")
