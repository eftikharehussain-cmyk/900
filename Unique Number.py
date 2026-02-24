for _ in range(int(input())):
    n = int(input())
    if 1 <= n <= 9:
        print(n)
    elif n > 45:
        print(-1)
    else:
        i = 9
        _chr = ""
        while i >= 1:
            if n > i:
                _chr += str(i)
                n-=i

            elif n == i:
                _chr +=  str(i)
                break

            i -= 1
        lst = list(_chr)
        lst1 = []
        for x in lst:
            lst1.append(int(x))
        lst1.sort()
        lst2 = []
        for k in lst1:
            lst2.append(str(k))
        print("".join(lst2))