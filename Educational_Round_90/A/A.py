t = int(input())
# t = int(fin.readline())
for ___ in range(t):
    a, b, c = (int(k) for k in input().split(' '))
    if a >= c:
        ans1 = -1
    else:
        ans1 = 1
    if a*b <= c:
        ans2 = -1
    else:
        ans2 = b
    print(f'{ans1} {ans2}')