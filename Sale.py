n, m = map(int, input().split())
lst = [x for x in map(int, input().split())]
lst1 = []
for i in lst:
    if i < 0:
        lst1.append(abs(i))
lst1.sort(reverse=True)
cnt = 0
if len(lst1) > m:
    for j in range(m):
        t = lst1[j]
        cnt += t
else:
    cnt = sum(lst1)
print(cnt)