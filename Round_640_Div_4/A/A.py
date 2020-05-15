def solve(n):
    ans = []
    while n > 0:
        n_str = str(n)
        new_num = int(n_str[0])*10**(len(n_str)-1)
        ans.append(str(new_num))
        n = n - new_num
    return ans
 
t = int(input())
for i in range(t):
    answer = solve(int(input()))
    print(len(answer))
    print(' '.join(answer)) 
