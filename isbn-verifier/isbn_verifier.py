def verify(isbn):
    x = []
    for ch in isbn:
        if ch is '-':
            pass
        elif ch.isdigit():
            x.append(ord(ch)-48)
        elif ch is 'X' and len(x) is 9:
            x.append(10)
        else:
            return False

    if len(x) is not 10:
        return False

    res = (x[0] * 10 + x[1] * 9 + x[2] * 8 + x[3] * 7 + x[4] * 6 + x[5] * 5 + \
        x[6] * 4 + x[7] * 3 + x[8] * 2 + x[9] * 1) % 11 == 0
    return res
