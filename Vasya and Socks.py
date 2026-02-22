n, m = map(int, input().split())
cnt = 0
cnt1 = 0
while n > 0:
    n -= m
    cnt += m
    cnt1 += 1
    if n >= 0:
        n += 1
print(cnt + n)