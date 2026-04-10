for _ in range(int(input())):
    n = int(input())
    _mat = []
    for _ in range(n):
        _mat.append(list(map(int, input().split())))
    _dict = {}
    for i in range(n):
        for j in range(n):
            d = i - j
            if d not in _dict:
                _dict[d] = []
            _dict[d].append(_mat[i][j])
    lst = []
    cnt = 0
    for key in _dict:
        lst.append(_dict[key])
    for j in lst:
        _min = min(j)
        if _min < 0:
            cnt += abs(_min)
    print(cnt)