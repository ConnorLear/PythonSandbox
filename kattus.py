n = "\___________________/"
print("""
|      
|      
|      
|      
|""")
p1 = n[1:]
p2 = int(len(p1))/2
for i in range(int(p2)+1):
    if i == 0:
        print(n[:-1]+"_/")
    else:
        print(" "*i+n[:1]+n[i*2:])
print()