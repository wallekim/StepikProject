
def polin(s):
    s = list(s)
    i = 0
    while i != (len(s) + 1) // 2:
        j = len(s)-i-1
        if s[i] == s[j] != '?':
            pass
        elif s[i] == '?' and s[j] != '?':
            s[i] = s[j]
        elif s[j] == '?' and s[i] != '?':
            s[j] = s[i]
        elif s[i] == s[j] == '?':
            s[i], s[j] = 'a', 'a'
        else:
            return 'NO'
        i += 1
    return ''.join(s)


print(polin(str(input())))