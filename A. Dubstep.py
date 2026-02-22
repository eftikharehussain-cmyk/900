for _ in range(int(input())):
    s = input()
    _str = s.split("WUB")
    lst1 = []
    for i in _str:
        if i != "":
            lst1.append(i)
    print(*lst1)