for _ in range(int(input())):
    s = input()
    c = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] == c and (i+1) % 2 != 0:
            cnt += 1

    if cnt > 0:
        print("YES")
    else:
        print("NO")