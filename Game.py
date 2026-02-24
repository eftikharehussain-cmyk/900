for _ in range(int(input())):
    s = input()
    t = s.count("0")
    y = s.count("1")
    _min = min(t, y)
    if _min % 2 == 0:
        print("NET")
    else:
        print("DA")