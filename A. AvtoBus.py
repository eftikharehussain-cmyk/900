for _ in range(int(input())):
    n = int(input())
    if n % 2 != 0 or n < 4:
        print(-1)
    else:
        print((n+5)//6, n//4)