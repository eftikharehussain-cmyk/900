for _ in range(int(input())):
    n = int(input())
    s = input()
    lst1 = list(s)
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    for h in lst:
        if h > 1:
            j = 0
            k = h - 1
            while j <= k:
                lst1[j], lst1[k] = lst1[k], lst1[j]
                j += 1
                k -= 1
    print("".join(lst1))