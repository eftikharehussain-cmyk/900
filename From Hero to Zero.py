for _ in range(int(input())):
    n, m = map(int, input().split())
    cnt = 0
    while n > 0:
        if n % m == 0:
            n //= m
            cnt += 1
        elif n % m != 0:
            tot = n % m
            n -= tot
            cnt += tot
            n //= m
            cnt += 1

    print(cnt -1)