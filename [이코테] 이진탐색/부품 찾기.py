import sys
input= sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

def search(target, start, end):
    if start > end :
        return "no"
    mid = (start+end)//2
    if target == array[mid]:
        return "yes"
    
    elif target > array[mid] :
        return search(target, mid+1, end)
    else:
        return search(target,start,mid-1)

for r in request:
    answer = search(r,0,n-1)
    print(answer, end=' ')

