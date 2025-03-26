import sys
x =int(sys.stdin.readline())
dp=[0]*1000001

for i in range(x+1):
    if i == 0 or i == 1:
        dp[i]=0
    else:
        dp[i]=dp[i-1]+1
    if i%5==0:
       if dp[i]>dp[i//5]+1:
            dp[i]=dp[i//5]+1

    if i%3==0:
        if dp[i]>dp[i//3]+1:
            dp[i]=dp[i//3]+1

    if i%2==0:
        if dp[i]>dp[i//2]+1:
            dp[i]=dp[i//2]+1
            

print(dp[x])