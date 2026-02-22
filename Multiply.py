for _ in range(int(input())):
    n = int(input())
    cnt = 0
    if n == 1:
        cnt = 0
    else:
        tot = n * 2
        if tot % 6 != 0:
            cnt = -1
        else:
            while n > 1:
                if n % 6 == 0:
                    n //= 6
                    cnt += 1
                else:
                    n *= 2
                    cnt += 1
    print(cnt)

#Problem:	1374B - Multiply by 2, divide by 6
for _ in range(int(input())):
    n = int(input())
    cnt = cnt1 = 0
    while n % 2 == 0:
        n //= 2
        cnt += 1
    while n % 3 == 0:
        n //= 3
        cnt1 += 1
    if n != 1 or cnt > cnt1:
        print(-1)
    else:
        print((cnt1 * 2) - cnt)