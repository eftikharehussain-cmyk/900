for _ in range(int(input())):
    n, x = map(int, input().split())
    a = [int(x) for x in input().split()]
    a1 = list(set(a))
    cnt = x
    for i in range(1, max(a)):
        if i not in a:
            a1.append(i)
            cnt -=1
            if cnt == 0:
                break
    a1.sort()
    for j in range(1, 200):
        if j not in a1:
            print((j-1) + cnt)
            break