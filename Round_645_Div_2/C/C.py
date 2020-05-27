def solve(inp_arr):
    ans = 0
    m = inp_arr[2] - inp_arr[0]
    n = inp_arr[3] - inp_arr[1]
    if m < n:
        m, n = n, m
    if n == 0:
        ans = 1
    else:
        ans = fact_calc(m,n)
    return ans

def fact_calc(a, b): # we assume a > b
    ans = 1
    # (M+N * ... * M+1)/(N*(N-1)*...*1)
    for i in range(b)[::-1]:
        ans *= (a+i+1)/(i+1)
    return round(ans)

# fin = open('input.txt', 'r')
# fout = open('output.txt', 'w')

t = int(input())
# t = int(fin.readline())
for ___ in range(t):
    # inp_arr = [int(k) for k in fin.readline().split(' ')]
    inp_arr = [int(k) for k in input().split(' ')]
    answer = solve(inp_arr)
    # fout.write(str(answer) + '\n')
    print(answer)

# fin.close()
# fout.close()