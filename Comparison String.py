for _ in range(int(input())):
    n = int(input())
    _str = input()
    lst = list(_str)
    _max = 0
    cnt = 1
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            cnt += 1
            if cnt > _max:
                _max = cnt
        else:
            cnt = 1
    if cnt > _max:
        _max = cnt
    print(_max+1)