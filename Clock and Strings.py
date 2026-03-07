for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    if a == 12 and b == 1 or b == 12 and a == 1:
        print("NO")
    elif (a-1) == b or (b-1) == a:
        print("NO")
    else:
        _min = min(a,b)
        _max = max(a,b)
        lst = []
        for i in range(_min+1,_max):
            lst.append(i)
        cnt = 0
        if c in lst:cnt += 1
        if d in lst:cnt += 1
        if cnt == 2 or cnt == 0:
            print("NO")
        else:
            print("YES")
