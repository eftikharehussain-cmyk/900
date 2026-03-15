for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    cnt = cnt1 = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            cnt += 1
        else:
            cnt1 += 1
    if cnt == n or cnt1 == n:
        print("YES")
    else:
        print("NO")
