for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    lst = []
    cnt = 0
    for i in range(1, n-1):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            lst.append(i)
            lst.append(i+1)
            lst.append(i+2)
            cnt += 1
            break
    if cnt == 0:
        print("NO")
    else:
        print("YES")
        print(*lst)