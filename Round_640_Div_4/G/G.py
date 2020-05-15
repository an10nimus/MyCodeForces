PATTERN = {
    0: [1, 4, 2, 5, 3],
    1: [1, 4, 2, 6, 3, 5],
    2: [1, 4, 2, 6, 3, 7, 5],
    3: [1, 5, 2, 6, 3, 7, 4, 8],
    4: [1, 4, 2, 5, 3, 7, 9, 6, 8]
    }
 
def solve(n):
    if n < 4:
        ans = -1
    elif n == 4:
        ans = [2, 4, 1, 3]
    else:
        ans = []
        common = (n // 5) - 1
        mod = n%5
        for jj in range(common):
            ans += [jj*5 + k for k in PATTERN[0]]
        ans += [(common)*5 + k for k in PATTERN[mod]]
    return ans
 
def output(arr):
    if isinstance(arr, list):
        print(' '.join(str(k) for k in arr))
    else:
        print(arr)
 
t = int(input())
for ___ in range(t):
    n = int(input())
    ans = solve(n)
    output(ans) 
