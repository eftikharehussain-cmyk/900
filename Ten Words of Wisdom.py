for _ in range(int(input())):
    n = int(input())
    lst = []
    for _ in range(n):
        a, b = map(int,input().split())
        if a <= 10:
            lst.append(b)
        else:
            lst.append(0)
    _max = max(lst)
    cnt = 0
    for j in range(len(lst)):
        if lst[j] == _max:
            cnt = j+1
            break
    print(cnt)