# n = input()
# def sum(a):
#     if len(a) <= 1:
#         return True
#         print ("True")
#     elif n[0]==n[-1]:
#         return True
#         print("True")
#     else:
#         return False
#         print ("FAlse")
#     n.replace([0],"")
#     n.replace ([-1], "")

n = input()
def sum(a):
    if len(a) <= 1:
        return True
    else:
        return a[0] == a[-1] and sum(a[1:-1])