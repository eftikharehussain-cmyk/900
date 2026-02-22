for _ in range(int(input())):
    lst = []
    for i in range(int(input())):
        t = list(map(int, input().split()))
        lst.append(t)
    _max = 0
    for j in lst:
        if sum(j) > _max:
            _max = sum(j)
    print(_max)
