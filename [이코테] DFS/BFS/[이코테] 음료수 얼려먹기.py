import sys
input=sys.stdin.readline

n,m = map(int,input().split())
graph=[]
visited=[[False]*m for _ in range(n)]
print(visited)

for _ in range(n):
    lst= list(map(int,input().strip()))
    graph.append(lst)

print(graph)

stack=[]
cnt=0
def dfs(v):
    i = v[0]
    j = v[1]
    if i>=n or i<0 or j>=m or j<0:
        return False
    else:
        if graph[i][j]==1:
            return True
    
    graph[i][j]=1

    dfs((i+1, j))
    dfs((i-1, j))
    dfs((i, j+1))
    dfs((i, j-1))
    return True

answer=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            dfs((i,j))
            if dfs((i,j))==True:
                answer+=1

print(answer)