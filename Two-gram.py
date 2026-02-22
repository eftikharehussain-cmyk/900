n = int(input())
_str = input()
_lst = list(_str)
_dict = {}
for i in range(len(_lst)-1):
    tot = _lst[i] + _lst[i+1]
    if tot not in _dict:
        _dict[tot] = 1
    else:
        _dict[tot] += 1
_lst1 = []
for key, value in _dict.items():
    _lst1.append([key, value])
_lst2 = []
for j in range(len(_lst1)):
    _lst2.append(_lst1[j][1])
_max = max(_lst2)
tot = ""
for k in range(len(_lst1)):
    if _lst1[k][1] == _max:
        tot = _lst1[k][0]
        break
print(tot)
