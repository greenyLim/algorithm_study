import sys
input=sys.stdin.readline

n = int(input())
cnt = 0

coin = [500,100,50,10]

for c in coin:
    cnt +=  n//c
    n = n%c

print(cnt)