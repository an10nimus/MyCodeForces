def solve(th, tc, t):
    ans = 0
    if th == t:
        ans = 1
    elif 2*t <= th + tc:
        ans = 2
    else:
        halfsum = (th + tc)/2
        halfdelta = (th - tc)/2
        j = 1
        i = 2*j + 1
        current_t = halfsum + halfdelta/i
        prev_t = th
        while current_t > t:
            prev_t = current_t
            j += 1
            i = 2*j + 1
            current_t = halfsum + halfdelta/i
        if abs(current_t - t) > abs(prev_t - t):
            ans = i-2
        else:
            ans = i        
    return ans
 
# fin = open('input.txt', 'r')
# fout = open('output.txt', 'w')

AA = int(input())
# AA = 1
# AA = int(fin.readline())
for ___ in range(AA):
    # th, tc, t = (int(k) for k in fin.readline().split(' '))
    th, tc, t = (int(k) for k in input().split(' '))
    answer = solve(th, tc, t)
    # fout.write(str(answer) + '\n')
    print(answer)

# fin.close()
# fout.close()