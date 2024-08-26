a = [1,2]
b = [-2,-1]
c = [-1,2]
d = [0,2]

def four_sum_count(a, b, c, d):
    ans = 0
    m = {}
    for i in a:
        for j in b:
            k = str(i+j)
            if k in m:
                m[k] += 1
            else:
                m[k] = 1
    for i in c:
        for j in d:
            k = str((i+j)*-1)
            if k in m:
                ans += m[k]

    return ans

print(
    four_sum_count(a,b,c,d)
)