class answer:

    def __init__(self, flag, arr = []):
        self.flag = flag
        self.arr = arr


def solve(n, k):
    if (k % 2 == 0) and (n % 2 == 0):
        if n >= k:
            ans = answer(True, [1] * (k-1) + [n - k+1])
        else:
            ans = answer(False,[])
    elif (k % 2 == 1) and (n % 2 == 0):
        if n >= 2 * k:
            ans = answer(True, [2] * (k-1) + [n - 2*(k-1)])
        else:
            ans = answer(False,[])
    elif (k % 2 == 1) and (n % 2 == 1):
        if n >= k:
            ans = answer(True, [1] * (k-1) + [n - k+1])
        else:
            ans = answer(False,[])
    else:
        ans = answer(False,[])
    return ans

t = int(input())
for i in range(t):
    input_nums = input().split(' ')
    obj = solve(int(input_nums[0]), int(input_nums[1]))
    if obj.flag == True:
        print('YES')
        print(' '.join(str(j) for j in obj.arr))
    else:
        print('NO')
 
