def price_easy(ss, x):
    ans = 0
    for ch in ss:
        if ch == '.':
            ans += x
    return ans

def price_full(ss, x, y):
    ans = 0
    flag = False
    # length = len(ss)-1
    length = len(ss)
    i = 0
    while i < length:
        ch = ss[i]
        if ch == '.' and flag:
            ans += y
            flag = False
        elif ch == '.' and i == length - 1:
            ans += x
            flag = False
        elif ch == '.':
            flag = True
        elif ch == '*' and flag:
            ans += x
            flag = False
        i += 1
    return ans
 
# fin = open('input.txt', 'r')
# fout = open('output.txt', 'w')

t = int(input())
# t = int(fin.readline())
for ___ in range(t):
    # (n, m, x, y) = (int(k) for k in fin.readline().split(' '))
    (n, m, x, y) = (int(k) for k in input().split(' '))
    price = 0
    if y >= 2*x: #too expensive 1x2
        for  j in range(n):
            # inp_str = fin.readline()
            inp_str = input()
            price += price_easy(inp_str, x)
    else: #use 1x2 as much as possible
        for  j in range(n):
            # inp_str = fin.readline()
            inp_str = input()
            price += price_full(inp_str, x, y)
    # answer = solve(int(fin.readline()))
    # fout.write(str(price) + '\n')
    print(price)

# fin.close()
# fout.close()