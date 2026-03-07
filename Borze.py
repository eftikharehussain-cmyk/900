s = input()
lst = []
i = 0
while i < len(s):
    if s[i] == ".":
        lst.append('0')
        i += 1
    elif s[i] == "-":
        if s[i+1] == ".":
            lst.append('1')
            i += 2
        elif s[i+1] == "-":
            lst.append('2')
            i += 2
print("".join(lst))