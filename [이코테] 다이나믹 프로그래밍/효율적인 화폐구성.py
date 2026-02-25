import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lst=[]
for _ in range(n):
    coin = int(input())
    lst.append(coin)

# dp 테이블은 1원을 만들기 위해 사용할 화폐 개수 
dp = [10001]*(m+1)

#0을 만들 수 잇는 건 0번 사용했을 때 
dp[0]=0
for i in lst:
    for j in range(i, m+1):
        if j-i == 0:
            dp[j]=1
        #그 전 단계 존재하면 
        if dp[j-i] != 10001:
            dp[j]=min(dp[j], dp[j-i]+1)

answer=dp[m]

if dp[m]==10001:
    answer=-1

print(answer)

