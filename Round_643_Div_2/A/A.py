LEN_ARR = 20

class longnum():
    
    def __init__(self, k, l, arr):
        self.k = k
        self.l = l
        self.arr = arr
        self.min = min(self.arr[0:self.l])
        self.max = max(self.arr[0:self.l])
    
    def make_correct(self):
        if self.arr[0] > 9:
            self.arr[1] += 1
            self.arr[0] -= 10
        flag = self.arr[1]>9
        ii = 0
        while flag:
            ii += 1
            self.arr[ii+1] += 1
            self.arr[ii] -= 10
            flag = self.arr[ii+1] > 9
        if (self.arr[ii+1] > 0) and (self.l < ii+2):
            self.l = ii+2
    
    def next_num(self):
        if self.min > 0:
            add = self.min*self.max
            (self.arr[0], self.arr[1]) = (self.arr[0] + (add % 10), self.arr[1] + (add // 10))
            if (self.l == 1) and self.arr[1] > 0:
                self.l = 2
            self.make_correct()
            self.min = min(self.arr[0:self.l])
            self.max = max(self.arr[0:self.l])
        self.k += 1

    def output(self):
        tmp = ''
        lngth = self.l
        for symb in self.arr[0:lngth][::-1]:
            tmp += str(symb)
        return tmp

def solve(k_n, big_num):
    while (big_num.k < k_n) and (big_num.min > 0):
        big_num.next_num()
    ans = big_num.output()
    return ans

t = int(input())
for ___ in range(t):
    arr_start = LEN_ARR*[0]
    inp_str_split = input().split(' ')
    k_num = int(inp_str_split[1])
    inp_str_num = inp_str_split[0][::-1]
    len_start = len(inp_str_num)
    for j in range(len_start):
        arr_start[j] = int(inp_str_num[j])
    new_big_num = longnum(1, len_start, arr_start)
    answer = solve(k_num, new_big_num)
    print(answer)