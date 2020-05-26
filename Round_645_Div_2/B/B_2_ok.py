def solve(n, ss):
    inp_arr_unsorted = [int(k) for k in ss.split(' ')]
    inp_arr = sorted(inp_arr_unsorted)[::-1]
    flag = False
    counter = 0
    n_fix = n
    candidate_ans = 0
    while not flag:
        if inp_arr[counter] <= n:
            flag = True
            candidate_ans = n
        else:
            counter += 1
            n -= 1
            flag = (counter == n_fix)
    candidate_ans += 1
    return candidate_ans

t = int(input())
for ___ in range(t):
    n = int(input())
    if n == 1:
        if int(input()) == 1:
            answer = 2
        else:
            answer = 1
    else:
        inp_str = input()   
        answer = solve(n, inp_str)
    print(answer)