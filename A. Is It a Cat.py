for _ in range(int(input())):
    n = int(input())
    s = input().upper()
    target = "MEOW"
    _chr = s[0]
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            _chr += s[i+1]
    if _chr == target:
        print("YES")
    else:
        print("NO")