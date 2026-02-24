t = int(input())
for _ in range(t):
    x, n, m = map(int, input().split())
    tot = x
    i = 0
    while i < n:
        tot //= 2
        tot += 10
        i += 1
        if tot > x:
            break
        else:
            x = tot
    if (m * 10) >= x:
        print("YES")
    else:
        print("NO")