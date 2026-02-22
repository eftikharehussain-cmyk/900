s = input()
lst = list(s)
lst1 = []
i = len(lst)
while i > 0:
    lst1.append(lst[i-1])
    i -= 1
if lst1 == lst:
    if len(set(lst)) == 1:
        print(0)
    else:
        print(len(lst)-1)
else:
    print(len(lst))