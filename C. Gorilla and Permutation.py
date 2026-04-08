for _ in range(int(input())):
    n, m, k = map(int, input().split())
    lst = []
    for i in range(n, m, -1):
        lst.append(i)
    for j in range(1, m):
        lst.append(j)
    _sum = sum(lst)
    tot = n * (n + 1) // 2
    lst.append(tot - _sum)
    print(*lst)