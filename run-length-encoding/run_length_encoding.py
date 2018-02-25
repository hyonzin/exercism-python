def decode(string):
    result = ''
    count = 0
    for ch in string:
        if '0' <= ch <= '9':
            count = (10*count) + (ord(ch)-ord('0'))
        else:
            if count is 0:
                result += ch
            else:
                result += ch * count
            count = 0
    return result


def encode(string):
    result = ''
    cur_ch = ''
    count = 1
    for ch in string:
        if cur_ch is '':
            cur_ch = ch
        elif ch is cur_ch:
            count += 1
        else:
            if count is not 1:
                result += str(count)
            result += cur_ch
            cur_ch = ch
            count = 1
    if count is not 1:
        result += str(count)
    result += cur_ch
    return result
