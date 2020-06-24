def check_prefix(str, prefix):
    is_similar = True
    prefix_len = len(prefix)
    i = 0
    while (is_similar) and (i <= prefix_len - 1):
        is_similar = str[i] == prefix[i]
        if is_similar:
            i += 1
    return i

def z_function(s):
    l = len(s)
    ans = [0]*l
    for j in range(1,l):
        ans[j] = check_prefix(s, s[j:l])
    return ans
    

ss = input()
ans = z_function(ss)
print(' '.join(str(k) for k in ans))