for _ in range(int(input())):
    a = [int(x) for x in input().split()]
    _max = max(a)
    tot = a + a
    lst = []
    while len(lst) < len(a):
        i = 0
        j = 1
        while i < len(tot):
            if tot[j] > tot[i]:
                lst.append(tot[j])
                i += 1
                j = i+1
            else:
                j += 1
    print(lst)