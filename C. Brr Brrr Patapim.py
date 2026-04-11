for _ in range(int(input())):
    n = int(input())
    _mat = []
    for _ in range(n):
        _mat.append(list(map(int, input().split())))
    lst = (n * 2) * [0]
    for i in range(1, n+1):
        for j in range(1, n+1):
            d = i + j
            if lst[d-1] == 0:
                lst[d-1] = _mat[i-1][j-1]
    _sum = sum(lst)
    t = len(lst)
    tot = (t * (t + 1)) // 2
    total = tot - _sum
    lst[0] = total
    print(*lst)