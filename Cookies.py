n = int(input())
lst = list(map(int, input().split()))
_sum = sum(lst)
cnt = cnt1 = 0
for i in lst:
    if i % 2 == 0:
        cnt += 1
    else:
        cnt1 += 1
if _sum % 2 == 0:
    print(cnt)
else:
    print(cnt1)