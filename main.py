e = 1
n: int = input()

for i in range(int(n)+1):
    m = str(f"2^{i}: {e}")
    print(m)
    e *= 2