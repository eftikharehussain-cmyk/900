for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_index_a = [(a[i], i) for i in range(n)]
    a_index_a.sort()
    b.sort()
    new_lst = n * [0]
    for j in range(n):
        value, index = a_index_a[j]
        new_lst[index] = b[j]
    print(*new_lst)