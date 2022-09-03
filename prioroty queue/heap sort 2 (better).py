
def buildmaxheap(arr,n):
    a = (n-1) // 2
    while(a>-1):
        maxheapify(arr, n,a)
        a-=1

    # print("build max heap", arr)

def maxheapify(arr, n,i):
    l = (2 * i) + 1
    r = (2 * i) + 2

    while(l < n ):
        if ( arr[l] > arr[i]):
            mx = l
        else:
            mx = i
        if (r < n and arr[r] > arr[mx]):
            mx = r
        if i == mx:
            return arr
        else:
            arr[mx], arr[i] = arr[i], arr[mx]
            maxheapify(arr,n, mx)

    pass
def heapSort(arr):
    if len(arr) == 0 or len(arr) == 1:

        return
    n=len(arr)
    buildmaxheap(arr,n)

    for i in range(n-1, 0,-1):

        arr[i], arr[0] = arr[0], arr[i]
        maxheapify(arr, i,0)
        # print("after swapping the array is:",arr)









    ######################
    # PLEASE ADD CODE HERE#
    ######################








n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr[::-1]:
    print(ele, end=' ')