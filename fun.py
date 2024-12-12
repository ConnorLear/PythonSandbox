e = 1

import random

n: int = random.randint(1, 75)

for i in range(int(n)+1):
    m = str(f"2^{i}: {e}")
    print(m)
    e *= 2

print("""

""")

for j in range(int(n)):
    t1 = int(n)-int(j)
    t2 = int(j)*2
    if int(j+1) < int(n):
        print(f"{t1*" "}/{t2*" "}\ ")
    else: 
        print(f"{t1*" "}/{t2*"_"}\ ")

print("""

""")

for j in range(int(n)):
    t1 = int(n)-int(j)
    t2 = int(j)*2
    print(f"{t1*" "}/{t2*" "}\ ")

for j in range(int(n)):
    t1 = (int(n)-int(j)-1)*2
    t2 = int(j)
    print(f" {t2*" "}\{t1*" "}/")

print(n)
