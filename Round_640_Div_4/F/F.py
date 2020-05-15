def ans_v2(n_0, n_1, n_2):
    ans_left = ''
    ans_center = ''
    ans_right = ''
    if n_1 == 0:
        if n_0 > 0:
            ans_left = '0'*(n_0 + 1)
        else:
            ans_right = '1'*(n_2 + 1)
    else:
        if n_0 == 0:
            if (n_1 % 2 == 0):
                ans_left = '10'*(n_1 // 2)
            else:
                ans_left = '0' + '10'*((n_1 - 1) // 2)
            ans_center = '1'*(n_2 + 1)
        elif n_2 == 0:
            if (n_1 % 2 == 0):
                ans_left = '01'*(n_1 // 2)
            else:
                ans_left = '1' + '01'*((n_1 - 1) // 2)
            ans_right = '0'*(n_0 + 1)
        else: # все ненулевые
            ans_right = '0'*(n_0 + 1)
            ans_center = '1'*(n_2 + 1)
            if (n_1 % 2 == 0): # чётное n_1
                ans_left = '0' + '10'*((n_1 - 2) // 2)
            else: # нечётное n_1
                ans_left = '10'*((n_1 - 1) // 2)

    return ans_left + ans_center + ans_right

t = int(input())
for i in range(t):
    input_nums = input().split(' ')
    answer = ans_v2(int(input_nums[0]), int(input_nums[1]), int(input_nums[2]))
    print(answer) 
