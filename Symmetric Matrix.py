for _ in range(int(input())):
    n, m = map(int,input().split())
    cnt = 0
    for _ in range(n):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        if b == c:
            cnt += 1
    if m % 2 != 0:
        print("NO")
    elif m % 2 == 0 and cnt > 0:
        print("YES")
    else:
        print("NO")