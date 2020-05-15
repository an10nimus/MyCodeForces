def solve(array):
    nums = [0]*8001
    counted = [False]*8001
    tmp = 0
    limit = 0
    length = len(array)
    for i in range(length):
        nums[array[i]] += 1
        if limit < array[i]:
            limit = array[i]
    for i in range(length-1):
        candidate = array[i] + array[i+1]
        j = i+1
        while (j < length) and (candidate <= limit):
            if not counted[candidate]:
                tmp += nums[candidate]
                counted[candidate] = True
            j += 1
            if j < length:
                candidate += array[j]
    return tmp

t = int(input())
for i in range(t):
    n = int(input())
    inp_str = input()
    arr = [int(j) for j in inp_str.split(' ')]
    ans = solve(arr)
    print(str(ans))
