import sys
sys.stdin = open('2675.txt', 'r')

t = int(input())

for x in range(t):
    r, s = input().split()
    r = int(r)
    s = str(s)
    for y in range(len(s)):
        new = r*s[y]
        print(new, end='')
    print()
