# from typing import List


def solve(n: int, arr, mmax: int) -> int:
    ans = 0
    res = 0
    i = 1
    while i <= mmax:
        if res == 0:
            ans += arr[i] // i
            res = arr[i] % i
        else:
            if res + arr[i] < i:
                res += arr[i]
            else:
                delta = arr[i] + res - i
                ans += (1 + (delta) // i)
                res = delta % i
        i += 1
    return ans

def prepare_data(n, inp_str):
    tmp_str = inp_str.split(' ')
    tmp = [0]*(n+1)
    mmax = 1
    for jj in range(n):
        k = int(tmp_str[jj])
        tmp[k] += 1
        if k > mmax:
            mmax = k
    return tmp, mmax

# fin = open('input.txt', 'r')
# fout = open('output.txt', 'w')

# t = int(fin.readline())
t = int(input())
for ___ in range(t):
    # n = int(fin.readline())
    # inp_str = fin.readline()
    n = int(input())
    inp_str = input()
    if n == 1:
        print(1)
    else:
        array, mmax = prepare_data(n, inp_str)
        # array = [0, 199912, 15, 5, 8, 13, 7, 13, 10, 7, 10]
        # mmax = 10
        groups = solve(n, array, mmax)
        print(groups)

#     fout.write(str(groups) + '\n')
# fin.close()
# fout.close()
# 0, 199912, 15, 5, 8, 13, 7, 13, 10, 7, 10, 0