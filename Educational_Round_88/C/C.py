def solve(th, tc, t):
    ans = 0
    if th == t:
        ans = 1
    elif 2*t <= th + tc:
        ans = 2
    else:
        k = (th - tc)/(2*t - th - tc)
        if (th - tc)%(2*t - th - tc) == 0:
            if k%2 == 0:
                ans = int(k)+1
            else:#k%2 == 1
                ans = int(k)
        else:
            k_int = int(k)
            if k_int%2 == 1:
                i_candidate = k_int
            else:
                i_candidate = k_int - 1
            if (1/k - 1/(i_candidate + 2) + 0.000000000000001) > (1/i_candidate - 1/k):
                ans = i_candidate
            else:
                ans = i_candidate + 2   
    return ans

AA = int(input())
for ___ in range(AA):
    th, tc, t = (int(k) for k in input().split(' '))
    answer = solve(th, tc, t)
    print(answer)
