for _ in range(int(input())):
    s= input()
    lst = list(s)
    n = len(lst)
    x = s.count("ab")
    y = s.count("ba")
    if x > y:
        if lst[0] == "a":
            lst[0] = lst[n-1]
        else:
            lst[n-1] = lst[0]
    elif x < y:
        if lst[0] == "b":
            lst[0] = lst[n-1]
        else:
            lst[n-1] = lst[0]
    else:
        lst = lst

    print("".join(lst))