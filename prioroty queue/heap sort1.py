
def buildmaxheap(arr):
    a = (len(arr)-1) // 2

    while(a>-1):
        maxheapify(arr, a)
        a-=1

    # print("build max heap", arr)
    return arr
def maxheapify(arr, i):
    l = (2 * i) + 1
    r = (2 * i) + 2
    s = len(arr)
    while(l < s ):
        if ( arr[l] > arr[i]):
            mx = l
        else:
            mx = i
        if (r < s and arr[r] > arr[mx]):
            mx = r
        if i == mx:
            return
        else:
            arr[mx], arr[i] = arr[i], arr[mx]
            maxheapify(arr, mx)
    pass
def heapSort(arr):
    if len(arr) == 0 or len(arr) == 1:

        return
    buildmaxheap(arr)

    for i in range(len(arr)-1, 0,-1):

        arr[i], arr[0] = arr[0], arr[i]
        # print("after swapping the array is:",arr)


        arr[0:i]= buildmaxheap(arr[0:i])
    #     print(arr)



    ######################
    # PLEASE ADD CODE HERE#
    ######################








n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr[::-1]:
    print(ele, end=' ')