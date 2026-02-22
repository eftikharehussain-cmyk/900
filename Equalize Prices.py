for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst1 = []
    lst2 = []
    for i in lst:
        lst1.append(i - k)
    for i in lst:
        lst2.append(i + k)
    if max(lst1) > min(lst2):
        print(-1)
    else:
        print(min(lst2))