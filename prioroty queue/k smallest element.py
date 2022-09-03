import heapq


def kSmallest(lst, k):
    # print(lst)
    priorityqueue = lst[:k]
    # print(priorityqueue)
    for i in  range(k, len(lst)):
        heapq._heapify_max(priorityqueue)
        if priorityqueue[0]> lst[i]:
            priorityqueue[0],lst[i]=lst[i], priorityqueue[0]
        else:
            continue
    return priorityqueue

    ######################
    # PLEASE ADD CODE HERE#
    ######################


# Main
n = int(input())
lst = list(int(i) for i in input().strip().split(' '))
k = int(input())
ans = kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')