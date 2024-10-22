list = []
n = int(input())
for i in range(n):
    list1 = input()
    p1 = list1[0:1].upper()
    p2 = list1[1:].lower()
    l1 = (p1+p2)
    list.append(l1)
    if i == n-1:
        for j in range(len(list)):
            print(list[j])
