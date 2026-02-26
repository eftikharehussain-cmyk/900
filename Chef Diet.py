for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [x for x in map(int, input().split())]
    for i in range(len(a)-1):
        if a[i] > k:
            tot = a[i] - k
            a[i] = k
            a[i+1] += tot
    cnt = 0
    for j in range(len(a)):
        if a[j] < k:
            cnt = j+1
            break
    if cnt > 0:
        print("NO", cnt)
    else:
        print("YES")