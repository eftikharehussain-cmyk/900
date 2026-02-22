n, d = map(int, input().split())
a = [x for x in map(int, input().split())]
total = 10 * (n - 1)
_sum = sum(a)
if total + _sum > d:
    print(-1)
else:
    tot = _sum + total
    cnt = total // 5
    cnt += (d - tot) // 5
    print(cnt)