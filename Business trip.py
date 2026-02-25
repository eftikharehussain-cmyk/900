n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
if sum(lst) < n:
    print(-1)
else:
    if n == 0:
        print(0)
    elif lst[0] >= n:
        print(1)
    else:
        cnt = cnt1 = 0
        for i in range(len(lst)):
            if cnt < n:
                cnt += lst[i]
                cnt1 += 1
        print(cnt1)