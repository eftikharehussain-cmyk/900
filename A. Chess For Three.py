for _ in range(int(input())):
    a, b, c = map(int, input().split())
    tot = a + b + c
    if tot % 2 != 0:
        print(-1)
    else:
        tot = tot // 2
        print(min(tot, a + b))