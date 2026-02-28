n = int(input())
_str = str(n)
i = 0
ok = True
while i < len(_str):
    if _str[i:i+3] == '144':
        i+=3
    elif _str[i:i+2] == '14':
        i+=2
    elif _str[i] == '1':
        i+=1
    else:
        ok = False
        break
print('YES' if ok else 'NO')
