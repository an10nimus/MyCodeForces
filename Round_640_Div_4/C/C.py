def solve(n, k):
    if k % (n-1) == 0:
        ans = n * (k // (n - 1)) - 1
    else:
        ans = (k // (n-1)) * n + k % (n-1)
    return ans

t = int(input())
for i in range(t):
    input_nums = input().split(' ')
    answer = solve(int(input_nums[0]), int(input_nums[1]))
    print(answer)
    
 
