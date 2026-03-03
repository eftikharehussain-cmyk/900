for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    a.sort()
    lst = list(set(a))
    cnt = k
    if k >= max(lst):
        print(k + len(lst))
    elif k < min(lst) and len(lst) == 1:
        print(k)
    elif k+1 < min(lst):
        print(k)
    elif k == 0:
        if lst[0] == 1:
            for j in range(1,len(lst)):
                tot = lst[j] - lst[j-1]
                if tot > 1:
                    print(lst[j-1])
                    break
            else:
                print(lst[-1])
        else:
            print(0)
    else:
        j = 1
        i = 0
        while cnt > 0:
            if i == 0 and lst[i] > 1:
                t = lst[i] - 1
                cnt -= t
                if cnt == 0:
                    for h in range(len(lst)-1):
                        tt = lst[h+1] - lst[h]
                        if tt > 1:
                            print(lst[h])
                    else:
                        print(lst[-1])
                        break
            elif lst[0] == 1:
                tot = (lst[j] - lst[i])-1
                cnt -= tot
                i += 1
                j += 1
        if cnt == 0:
            for k in range(i, len(lst)-1):
                ct = lst[k+1] - lst[k]
                if ct > 1:
                    print(lst[k])
                    break
            else:
                print(lst[-1])