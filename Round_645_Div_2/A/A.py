def solve(m, n):
    ans = 0
    if (m%2 == 1) and (n%2 == 1):
        ans = n*(m//2) + (n//2) + 1
    elif m%2 == 1:
        ans = (n//2)*m
    else:
        ans = (m//2)*n
    return ans

# fin = open('input.txt', 'r')
# fout = open('output.txt', 'w')

t = int(input())
# t = int(fin.readline())
for ___ in range(t):
    # inp_arr = fin.readline().split(' ')
    inp_arr = input().split(' ')
    (m, n) = [int(k) for k in inp_arr]
    if m%2 == 1:
        m, n = n, m
    answer = solve(m, n)
    # fout.write(str(answer) + '\n')
    print(answer)

# fin.close()
# fout.close()