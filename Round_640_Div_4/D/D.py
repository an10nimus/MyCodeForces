class answer:
    
    def __init__(self, a, b, moves):
        self.a = a
        self.b = b
        self.moves = moves
    
    def output(self):
        print(f'{self.moves} {self.a} {self.b}')

    def refresh(self):
        self.a = 0
        self.b = 0
        self.moves = 0


class candygame:
    
    def __init__(self, n, candy_list, answer_tmp = answer(0,0,0), left_last = 0, right_last = 0):
        self.n = n
        self.candy_list = candy_list
        self.answer_tmp = answer_tmp
        self.left_last = left_last
        self.right_last = right_last
    
    def eat_left(self):
        tmp = 0
        limit = self.right_last
        while (tmp <= limit) and (self.n > 0):
            tmp += self.candy_list.pop(0)
            self.n -= 1
        self.answer_tmp.moves += 1
        self.answer_tmp.a += tmp
        self.left_last = tmp
        #self.n = len(self.candy_list)
    
    def eat_right(self):
        tmp = 0
        limit = self.left_last
        while (tmp <= limit) and (self.n > 0):
            tmp += self.candy_list.pop()
            self.n -= 1
        self.answer_tmp.moves += 1
        self.answer_tmp.b += tmp
        self.right_last = tmp
        #self.n = len(self.candy_list)
    
    def solve(self):
        while self.n > 0:
            self.eat_left()
            if self.n > 0:
                self.eat_right()
        return self.answer_tmp

start_ans = answer(0, 0, 0)
t = int(input())
for i in range(t):
    n = int(input())
    inp_str = input()
    input_candies = [int(j) for j in inp_str.split(' ')]
    game = candygame(n, input_candies, start_ans)
    answer = game.solve()
    answer.output()
    start_ans = answer(0, 0, 0)
    #start_ans.refresh()
