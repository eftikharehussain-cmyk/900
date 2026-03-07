for _ in range(int(input())):
    n = int(input())
    lst = [int(x) for x in input().split()]
    _set = set(lst)
    print(len(_set))