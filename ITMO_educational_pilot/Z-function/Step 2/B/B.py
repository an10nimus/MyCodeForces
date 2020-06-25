def solve(k, j):
    some_number = 2**(k-1)
    if j == some_number:    # then it's a separating element
        return some_number-1
    else:
        k -= 1
        if j > some_number:
            j -= some_number
        return solve(k, j)

t = int(input())
for ___ in range(t):
    inp = input()
    k, j = (int(ss) for ss in inp.split(' '))
    if (j*(j%2 - 1)) == 0:
        ans = 0
    else:
        ans = solve(k, j)
    print(ans)