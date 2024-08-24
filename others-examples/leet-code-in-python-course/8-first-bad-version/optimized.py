def isWrongVersion(n):
    return n >= 7

versions = [1,2,3,4,5,6,7,8,9,10]

def findTheFirstWrongVersion():
    L = 0
    R = len(versions) - 1
    while (L < R):

        mid =  L + (R - L)// 2

        if isWrongVersion(versions[mid]):
            if mid-1 > 0 and not isWrongVersion(versions[mid-1]):
                return versions[mid]
            else:
                R = mid
        else:
            L = mid + 1
    
print(findTheFirstWrongVersion())


# [1,2,3,4,5,6,7,8,9,10]
#  L       ^          R

# [1,2,3,4,5,6,7,8,9,10]
#  L   ^   R      
