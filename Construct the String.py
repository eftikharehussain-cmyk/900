for _ in range(int(input())):
    t = 'abcdefghijklmnopqrstuvwxyz'
    n, a, b = map(int, input().split())
    _str = ""
    result = t[:b]
    while len(_str) < n:
        _str += result
    print(_str[:n])