def distance(strand_a, strand_b):
    if len(strand_a) is not len(strand_b):
        raise ValueError('please let two strands be same length')
    res = 0
    for i in range(len(strand_a)):
        if strand_a[i] is not strand_b[i]:
            res += 1
    return res
