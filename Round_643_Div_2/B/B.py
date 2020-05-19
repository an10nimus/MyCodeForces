def solve(n, arr):
    
    while (big_num.k < k_n) and (big_num.min > 0):
        big_num.next_num()
    ans = big_num.output()
    return ans

def prepare_data(n, inp_str):
    tmp_str = inp_str.split(' ')
    tmp = [0]*(n+1)
    for jj in range(n):
        tmp[int(tmp_str[jj])] += 1
    return tmp

fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())
for ___ in range(t):
    n = int(fin.readline())
    inp_str = fin.readline()
    array = prepare_data(n, inp_str)
    
fin.close()
fout.close()