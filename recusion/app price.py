def maximumProfit(arr, n):
    # Implement Your Function here

    arr = sorted(arr)
    max = 0
    i=0
    while(i<n):
        count=0
        while((arr[i]==arr[i+1])and i<n-1):
            count+=1
            i+=1

        ans=((n+1-i)*arr[i]+((count)*arr[i]))
        print(ans,i)
        i=i+1
        if max < ans:
            max = ans

    return max


n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr, len(arr)-1)
print(ans)