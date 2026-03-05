import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    ok = True
    
    for i in range(n-2, -1, -1):
        if a[i] < a[i+1]:
            continue
        if a[i+1] == 0:
            ok = False
            break

        k = 0
        val = a[i]
        while val >= a[i+1]:
            val //= 2
            k += 1

        ans += k
        a[i] = val
        if a[i] >= a[i+1]:
            ok = False
            break

    print(ans if ok else -1)


    #for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    lst = []
    cnt = 0
    for i in range(len(a)-1,-1,-1):
        lst.append(a[i])

    i = 0
    j = 1
    cnt = 0
    ok = True
    while j < len(lst):
        while lst[i] <= lst[j]:
            if lst[i] == 0 and lst[j] >= 0:
                ok = False
                break
            if lst[i] <= lst[j]:
                lst[j]//= 2
                cnt += 1

        i+=1
        j+=1
    print(cnt if ok else -1)
    print(lst)