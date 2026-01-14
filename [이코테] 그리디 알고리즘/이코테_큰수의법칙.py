import sys
input=sys.stdin.readline

n,m,k= map(int, input().split())
lst= list(map(int, input().split()))

lst.sort()
cnt = 0
answer = 0

for _ in range(m):
    if cnt == k:
        answer += lst[-2]
        cnt = 0
    elif cnt < k:
        answer += lst[-1]
        cnt += 1

print(answer)