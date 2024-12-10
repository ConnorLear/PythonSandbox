e = 1
n: int = input("  ")

for i in range(int(n)+1):
    m = str(f"2^{i}: {e}")
    print(m)
    e *= 2

print()

for j in range(int(n)):
    t1 = int(n)-int(j)
    t2 = int(j)*2
    if int(j+1) < int(n):
        print(f"{t1*" "}/{t2*" "}\ ")
    else: 
        print(f"{t1*" "}/{t2*"_"}\ ")