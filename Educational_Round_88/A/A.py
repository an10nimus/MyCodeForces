def solve(n, m, k):
    ans = 0
    cards_pp = round(n/k)
    if m == n:
        ans = 0
    else:
        if m <= cards_pp:
            ans = m
        else:
            if k>2:
                if (m-cards_pp)%(k-1) == 0:
                    ans = cards_pp - (m-cards_pp)//(k-1)
                else:
                    ans = cards_pp - (m-cards_pp)//(k-1) - 1
            else:
                ans = cards_pp - (m-cards_pp)
    return ans
 
# fin = open('input.txt', 'r')
# fout = open('output.txt', 'w')

t = int(input())
# t = int(fin.readline())
for ___ in range(t):
    # (n, m, k) = (int(l) for l in fin.readline().split(' '))
    (n, m, k) = (int(l) for l in input().split(' '))
    answer = solve(n, m, k)
    # fout.write(str(answer) + '\n')
    print(answer)

# fin.close()
# fout.close()