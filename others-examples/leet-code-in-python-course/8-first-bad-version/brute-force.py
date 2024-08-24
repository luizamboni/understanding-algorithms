def isWrongVersion(n):
    return n >= 3


versions = [1,2,3,4,5,6,7,8,9,10]

def findTheFirstWrongVersion():
    for n in versions:
        if isWrongVersion(n):
            return n

print(findTheFirstWrongVersion())