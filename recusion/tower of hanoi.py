def tower_hanoi(n,source,aux,des):
    if n == 1:
        print("Move disk from",source,"to",des)
        return
    if n == 0:
        return
    tower_hanoi(n-1,source,des,aux)
    print("Move disk from",source,"to",des)
    tower_hanoi(n-1,aux,source,des)
tower_hanoi(3,"s","h","d")