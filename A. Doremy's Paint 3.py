for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    tot = set(a)
    if len(tot) == 1:
        print("YES")
    elif len(tot) > 2:
        print("NO")
    else:
        _max = max(a)
        _min = min(a)
        b = a.count(_max)
        c = a.count(_min)
        if b == c:
            print("YES")
        elif b > c:
            if b == c+1:
                print("YES")
            else:
                print("NO")
        elif b < c:
            if b+1 == c:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")