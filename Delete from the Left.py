t = input().strip()
s = input().strip()
total = len(t)+len(s)
_min = min(len(t),len(s))
i = j = -1
count = 0
while _min > 0:
    if t[i] == s[j]:
        i -= 1
        j -= 1
        count += 2
        _min -= 1
    else:
        break
print(total-count)
