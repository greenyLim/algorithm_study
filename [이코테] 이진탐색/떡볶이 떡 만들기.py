import sys
input=sys.stdin.readline

n ,m = map(int,input().split())

lst = list(map(int,input().split()))
lst.sort()
start = 0
end = max(lst)

def cut(i,j):
    answer=i-j
    if answer<0:
        answer=0
    return answer

answer=0
while start < end:
    print("start:",start,"end:",end,answer)
    mid=(start+end)//2

    res = list(map(lambda x:cut(x,mid),lst))
    res_next = list(map(lambda x:cut(x,mid+1),lst))
    print(res)
    
    if sum(res)==m:
        answer=mid
        break

    elif sum(res) < m:
        end = mid-1
        continue

    else:
        if sum(res_next) < m:
            answer=mid
            break
        start = mid + 1
        continue
       

print(answer)

