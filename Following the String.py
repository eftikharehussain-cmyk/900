for _ in range(int(input())):
    n = int(input())
    s = 'abcdefghijklmnopqrstuvwxyz'
    a = [int(x) for x in input().split()]
    _dict = {}
    cnt = 0
    lst = []
    for i in range(len(a)):
        if a[i] == 0 and a[i] not in _dict:
            lst.append(s[cnt])
            _dict[s[cnt]] = 1
            cnt += 1
        else:
            for k in _dict:
                if _dict[k] == a[i]:
                    lst.append(k)
                    _dict[k] += 1
                    break
    print("".join(lst))
