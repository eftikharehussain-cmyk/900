for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    _dict = {}
    for i in range(n):
        if a[i] not in _dict:
            _dict[a[i]] = 1
        else:
            _dict[a[i]] += 1
    cnt = 0
    for key in _dict:
        t = k - key
        if t in _dict and t == key:
            cnt += (_dict[key]) // 2
            _dict[key] = 0
        elif t in _dict and t != key:
            cnt += min(_dict[key], _dict[t])
            _dict[key] = 0
            _dict[t] = 0
    print(cnt)