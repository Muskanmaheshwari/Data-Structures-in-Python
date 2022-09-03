def rec(n):
    if n//10==0:
        return n
    return n%10+rec(n//10)
def hi(n):
    if n//10==0:
        return n
    return rec(n)
n = int(input())
print(hi(n))