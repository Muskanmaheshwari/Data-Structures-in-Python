## Read input as specified in the question.
## Print output as specified in the question.
def check(string, start, end):
    if (len(string) == 1 or len(string) == 0):
        return 1
    if (string[start] == string[end]):
        return check(string, (start + 1), (end - 1))
    else:
        return 0


def palindromecheck(string):
    if len(string)==0 or len(string)==1:
        return 1
    x = check(string, 0, len(string) - 1)
    return x
# def rec(a,si,ei):
#     if si==ei or si>ei:
#         return True
#     if a[si] == a[ei]:
#         return rec(a,si+1,ei-1)
#     else:
#         return False
#
#     pass
# a = input()
# print(rec(a,0, len(a)-1))



a = input()
if palindromecheck(a):
    print("true")
else:
    print("false")