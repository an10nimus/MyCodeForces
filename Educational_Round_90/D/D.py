t = int(input())
for ___ in range(t):
    length = int(input())
    a = [int(k) for k in input().split(' ')]
    max_boost = 0
    summm = 0
    for k in range(length):
        if k%2 == 0:
            summm += a[k]
    for l in range(length-1):
        if l%2 == 0:
            vygoda = 0
            sum_nech, sum_ch = 0, 0+a[l]
            for r in range(l+1, length):
                if r%2 == 1:
                    sum_nech += a[r]
                    vygoda = sum_nech - sum_ch
                    if vygoda > max_boost:
                        max_boost = vygoda
                else:
                    sum_ch += a[r]
        else:
            vygoda = 0
            sum_nech, sum_ch = 0+a[l], 0
            for r in range(l+1, length):
                if r%2 == 0:
                    sum_ch += a[r]
                    vygoda = sum_nech - sum_ch
                    if vygoda > max_boost:
                        max_boost = vygoda
                else:
                    sum_nech += a[r]
    print(summm + max_boost)