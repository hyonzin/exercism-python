def rotate(text, key):
    result = ''
    for ch in text:
        if ch.isalpha():
            z = 'z' if ch.islower() else 'Z'
            ch = chr(ord(ch)+key if ord(ch)+key <= ord(z) else ord(ch)+key-26)
        result += ch
    return result
