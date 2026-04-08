for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    _set = set(lst)
    cnt = 0
    for i in range(k):
        if i in _set:
            cnt += 1
    cnt1 = k - cnt
    x = lst.count(k)
    print(max(cnt1, x))

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    
    freq = [0] * (n + 1)
    
    for x in lst:
        freq[x] += 1
    
    missing = 0
    for i in range(k):
        if freq[i] == 0:
            missing += 1
    
    print(max(missing, freq[k]))