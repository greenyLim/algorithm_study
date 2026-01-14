def solution (num, k):
    max_num=max(num)
    result=[0]*(max_num+1)
    count=[0]*(max_num+1)

    for i, n in enumerate(num):
        count[n]+=1

    while sum(result)<k:
        