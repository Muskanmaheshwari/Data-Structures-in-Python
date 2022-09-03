def pattern(a,n,flag):
    print(a,end=' ')
    if a == n and flag==False:
        return
    if flag:
        if a-5>0:
            return pattern(a-5,n,True)
        else:
            return pattern(a-5,n,False)
    else:
        pattern(a+5,n,False)



a = int(input("Enter a no"))
pattern(a,a, True)