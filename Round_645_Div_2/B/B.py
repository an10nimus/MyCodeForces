# class grannies:

#     def __init__(self, arr, mmin, mmax):
#         self.ind = arr
#         self.min = mmin
#         self.max = mmax

# def solve2(some_gr):
#     ans = 0
#     cum_sum = 0 # nothing for the initial granny
#     candidate_ans = 0
#     for counter in range(some_gr.min, some_gr.max + 1): #count cumulative sum
#         new = some_gr.ind[counter]
#         if new > 0:  
#             cum_sum += new
#             if counter <= cum_sum:
#                 candidate_ans = cum_sum
#     candidate_ans += 1
#     return candidate_ans       

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
    if n == 1:
        if nonzero_indices[0] == 1:
            candidate_ans = 1
        else:
            candidate_ans = 0
    else:
        if highest <= sum_available:
            candidate_ans = sum_available
        else:
            nonzero_set = sorted(set(nonzero_indices))[::-1]
            i = 0
            cum_sum = sum_available
            while i < len(nonzero_set):
                counter = nonzero_set[i]
                if counter <= cum_sum:
                    candidate_ans = cum_sum
                    i = len(nonzero_set)
                else:
                    new = index[counter]
                    cum_sum -= new
                    i += 1
            # for counter in nonzero_set: #count cumulative sum       
    candidate_ans += 1
    return candidate_ans


t = int(input())
for ___ in range(t):
    n = int(input())
    if n == 1:
        if int(input()) == 1:
            answer = 2
        else:
            answer = 1
    else:
        indices = [0]*(2*10**5 + 5)
        lowest = 10**6
        highest = 0
        inp_str = input()
        answer = solve(n, inp_str)
    print(answer)