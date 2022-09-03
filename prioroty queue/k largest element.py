import heapq
def kLargest(lst, k):
    # print(lst)
    priorityqueue = lst[:k]
    # print(priorityqueue)
    for i in  range(k, len(lst)):
        heapq.heapify(priorityqueue)
        if priorityqueue[0]< lst[i]:
            priorityqueue[0],lst[i]=lst[i], priorityqueue[0]
        else:
            continue
    return priorityqueue

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')
