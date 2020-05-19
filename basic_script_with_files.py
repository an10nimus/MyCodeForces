def solve(n):
    ans = []
    return ans
 
fin = open('input.txt', 'r')
fout = open('input.txt', 'w')

#t = int(input())
t = int(fin.readline())
for i in range(t):
    answer = solve(int(fin.readline()))
    print(fout.write(str(ans)))

fin.close()
fout.close()