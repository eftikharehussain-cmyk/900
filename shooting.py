n = int(input())
lst = list(map(int, input().split()))
lst1 = lst[:]
lst.sort(reverse=True)
cnt = 0
i = 0
while i < n:
    cnt += (lst[i] * i) + 1
    i += 1
lst2 =[]
for i in range(n):
    lst2.append([lst1[i], i + 1])
for i in range(n):
    for j in range(i+1,n):
        if lst2[i][0] < lst2[j][0]:
            lst2[i],lst2[j] = lst2[j],lst2[i]
lst3 = []
for k in range(n):
    lst3.append(lst2[k][1])
print(cnt)
print(*lst3)