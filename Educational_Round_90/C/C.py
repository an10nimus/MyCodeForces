t = int(input())
for ___ in range(t):
    s = input()
    a, length = [], len(s)
    current_sum, current_max = 0, 0
    for i in range(length):
        ch = s[i]
        if ch == '-':
            current_sum -= 1
        else:
            current_sum += 1
        if -current_sum > current_max:
            current_max = -current_sum
        a.append(current_max)
    if current_max == 0:
        print(length)
    else:
        moves = current_max + 1
        cur = 0
        summ = 0
        for i in range(length):
            if a[i] <= cur:
                summ += moves
            else:
                cur += 1
                summ += moves
                moves -= 1
        print(summ)