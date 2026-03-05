for _ in range(int(input())):
    n = int(input())
    s = input()
    i = 0
    cnt = 0
    while i < n:
        if i+4 < n and s[i:i+5] == "mapie":
            cnt += 1
            i += 5
        elif i+2 < n and s[i:i+3]  == "map" or s[i:i+3] == "pie":
            cnt += 1
            i += 3
        else:
            i+=1
    print(cnt)