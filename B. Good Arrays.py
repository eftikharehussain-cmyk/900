for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    _sum = sum(a)
    cnt = _sum
    ok = True
    if len(a) == 1:
        print("NO")
    else:
        for i in range(len(a)):
            if cnt < 0:
                break
            else:
                if a[i] == 1:
                    cnt -= 2
                elif a[i] == 2:
                    cnt -= 1
                else:
                    cnt -= 1
        if cnt >= 0:
            print("YES")
        else:
            print("NO")