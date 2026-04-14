for _ in range(int(input())):
    n, k = map(int, input().split())
    a = input()
    cnt0 = a.count('0')
    cnt1 = a.count('1')
    if min(cnt0, cnt1) >= ((n//2)-k) and (cnt0 - ((n//2)-k)) % 2 == 0:
        print('Yes')
    else:
        print('No')

