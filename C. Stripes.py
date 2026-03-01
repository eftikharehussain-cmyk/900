t = int(input())

for _ in range(t):
    input()

    _mat = []
    for _ in range(8):
        _mat.append(input())

    t = False
    for row in _mat:
        if row == 'RRRRRRRR':
            t = True
            break
    if t:
        print('R')
    else:
        print('B')