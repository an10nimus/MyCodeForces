t = int(input())
for ___ in range(t):
    s, count_0, count_1= input(), 0, 0
    length = len(s)
    for i in range(length):
        if s[i] == '0':
            count_0 += 1
        else:
            count_1 += 1
    moves = min(count_0, count_1)
    if moves%2 == 1:
        print('DA')
    else:
        print('NET')