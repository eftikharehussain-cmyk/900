for _ in range(int(input())):
    n, m = map(int,input().split())
    _str = input()
    lst = list(_str)
    _dict = {}
    for i in range(len(lst)):
        if lst[i] not in _dict:
            _dict[lst[i]] = 1
        else:
            _dict[lst[i]] += 1
    cnt = 0
    for key in _dict:
        if _dict[key] > m:
            cnt += m
        else:
            cnt += _dict[key]
    print((m * 7) - cnt)
