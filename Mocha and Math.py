for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    tot = a[0]
    for i in a[1:]:
        tot &= i
    print(tot)