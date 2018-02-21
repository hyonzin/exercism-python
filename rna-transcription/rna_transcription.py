def to_rna(dna_strand):
    res = ""
    for ch in dna_strand:
        if ch is 'G':
            res += 'C'
        elif ch is 'C':
            res += 'G'
        elif ch is 'T':
            res += 'A'
        elif ch is 'A':
            res += 'U'
        else:
            raise ValueError("Invalid Value:", ch)
    return res
