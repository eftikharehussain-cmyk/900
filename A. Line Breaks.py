for _ in range(int(input())):
    n, m = map(int, input().split())
    lst = []
    l = 0
    cnt = 0
    for _ in range(n):
        s_i = input()
        l1 = len(s_i)
        if l1 + l <= m:
            l += l1
            cnt += 1
        else:
            l += l1


    print(cnt)