n = int(input())
s = input()
lst1 = []
if n % 2 != 0:
    for i in range(n):
        lst1.append(s[i]) if i % 2 == 0 else lst1.insert(0, s[i])
else:
    for i in range(n):
        lst1.append(s[i]) if i % 2 != 0 else lst1.insert(0, s[i])
print("".join(lst1))