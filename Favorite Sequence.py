for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    lst1 = []
    i = 0
    j = len(a)-1
    if n % 2 == 0:
        while i < j:
            lst1.append(a[i])
            lst1.append(a[j])
            i += 1
            j -= 1
    else:
        while i <= j:
            lst1.append(a[i])
            lst1.append(a[j])
            i += 1
            j -= 1
        if len(lst1) > len(a):
            lst1.pop(-1)

    print(*lst1)