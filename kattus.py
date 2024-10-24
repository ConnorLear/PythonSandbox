n = int(input())
h1 = n//3600
h2 = n-h1*3600
m1 = h2//60
m2 = h2-m1*60
s1 = m2
print(str(h1)+":"+str(m1)+":"+str(s1))