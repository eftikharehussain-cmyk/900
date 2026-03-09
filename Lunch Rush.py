n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
for i in range(len(lst)):
    if lst[i][1] > k:
        lst[i][0] = lst[i][0] - (lst[i][1] - k)
lst1 = []
for j in range(len(lst)):
    lst1.append(lst[j][0])
print(max(lst1))