def p(GayMonkey):
    print(GayMonkey)

n = "\_______________________________________________/"
p("""
""")
p1 = n[1:]
p2 = int(len(p1))/2
for i in range(int(p2)+1):
    if i == 0:
        p(n[:-1]+"_/")
    else:
        p(" "*i+n[:1]+n[i*2:])
p("""
""")
