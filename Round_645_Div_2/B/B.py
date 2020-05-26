class grannies:

    def __init__(self, arr, mmin, mmax):
        self.ind = arr
        self.min = mmin
        self.max = mmax

def solve2(some_gr):
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

def solve(n, ss):
    cum_sum = 0 # nothing for the initial granny
    candidate_ans = 0
    index = indices = [0]*(2*10**5 + 5)
    lowest = 10**6
    highest = 0
    inp_arr = ss.split(' ')
    nonzero_indices= []
    sum_available = 0
    for under_s in  inp_arr:
        a = int(under_s)
        if a <= n+1:
            sum_available += 1
            index[a] += 1
            if lowest > a:
                lowest = a
            if highest < a:
                highest = a
            nonzero_indices.append(a)
        else:
            n -= 1
    if highest <= sum_available:
        candidate_ans = sum_available
    else:
        nonzero_set = sorted(set(nonzero_indices))[::-1]
        i = 0
        while i < len(nonzero_set):
            counter = nonzero_set[i]
            if 
        # for counter in nonzero_set: #count cumulative sum

        
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
    inp_str = input()
    answer = solve(n, inp_str)
    # inp_arr = fin.readline().split(' ')
    # inp_arr = input().split(' ')
    # solve(n, inp_str)
    # for gr in inp_arr:
    #     new = int(gr)
    #     indices[new] += 1
    #     if new > highest:
    #         highest = new
    #     if new < lowest:
    #         lowest = new
    # grannies_setup = grannies(indices, lowest, highest)
    # answer = solve(grannies_setup)
    # fout.write(str(answer) + '\n')
    print(answer)

# fin.close()
# fout.close()