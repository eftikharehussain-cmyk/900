for _ in range(int(input())):
    n = int(input())
    s = input()
    lst = list(s)
    target = "aeiou"
    target1 = list(target)
    cnt = 0
    cnt1 = 0
    for i in range(len(lst)):
        if lst[i] not in target1:
            cnt += 1
            if cnt >= 4:
                cnt1 += 1
        else:
            cnt = 0
    if cnt1 >= 1:
        print("NO")
    else:
        print("YES")