class grannies:

    def __init__(self, arr, mmin, mmax):
        self.ind = arr
        self.min = mmin
        self.max = mmax

def solve(some_gr):
    ans = 0
    cum_sum = 0 # nothing for the initial granny
    candidate_ans = 0
    for counter in range(some_gr.min, some_gr.max + 1): #count cumulative sum
        new = some_gr.ind[counter]
        if new > 0:  
            cum_sum += new
            if counter <= cum_sum:
                candidate_ans = cum_sum
    candidate_ans += 1
    return candidate_ans       
 
# fin = open('input.txt', 'r')
# fout = open('output.txt', 'w')

t = int(input())
# t = int(fin.readline())
for ___ in range(t):
    indices = [0]*(2*10**5 + 5)
    lowest = 10**6
    highest = 0
    # n = int(fin.readline())
    n = int(input())
    # inp_arr = fin.readline().split(' ')
    inp_arr = input().split(' ')
    for gr in inp_arr:
        new = int(gr)
        if new < n:
            indices[new] += 1
            if new > highest:
                highest = new
            if new < lowest:
                lowest = new
        else:
            n -= 1
    grannies_setup = grannies(indices, lowest, highest)
    answer = solve(grannies_setup)
    # fout.write(str(answer) + '\n')
    print(answer)

# fin.close()
# fout.close()