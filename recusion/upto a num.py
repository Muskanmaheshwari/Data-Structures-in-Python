def num(x,a):
    if a<len(str(x)):
        return
    print(x)
    return num(x+1,a)


a = int(input("Enter a number "))
num(0,a)