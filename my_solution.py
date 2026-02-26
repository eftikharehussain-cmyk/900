for _ in range(int(input())):
    n = int(input())
    s = input()
    _str = ""
    if len(s) % 2 != 0:
        i = j = len(s) // 2
    else:
        i = (len(s) // 2)-1
        j = len(s) // 2
    while  j < len(s):
        if i == j:
            _str += s[j]
            j+=1
            i-=1
        else:
            _str += s[i]
            _str += s[j]
            i -= 1
            j += 1
    print(_str)
