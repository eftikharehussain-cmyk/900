for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    _dict = {}
    alice = (n + 1) // 2
    bob = n // 2
    for i in range(len(lst)):
        if lst[i] not in _dict:
            _dict[lst[i]] = 1
        else:
            _dict[lst[i]] += 1
    count = 0
    count1 = 0
    for color, cnt in _dict.items():
        if cnt == 1:
            count += 1
        else:
            count1 += 1
    if count > 1:
        count = (count + 1) // 2
    elif count == 1:
        count = 1
    print(count1 + (count*2))