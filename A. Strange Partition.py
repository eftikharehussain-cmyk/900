for _ in range(int(input())):
    n, x = map(int, input().split())
    a = [int(x) for x in input().split()]
    cnt = 0
    _sum = (sum(a)+(x-1)) // x
    for i in range(len(a)):
        cnt += (a[i]+(x-1)) // x
    print(_sum, cnt)
