for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    cnt = cnt1 = 0
    for i in range(len(lst)-1):
        tot = abs(lst[i]-lst[i+1])
        if tot <= k:
            cnt+=1
            if cnt > cnt1:
                cnt1 = cnt
        else:
            cnt=0
    print(n - (cnt1+1))