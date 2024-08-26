a = [1,2]
b = [-2,-1]
c = [-1,2]
d = [0,2]

def four_sum_count(a, b, c, d):
    ans = 0
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    if i + j + k + l == 0:
                        ans += 1

    return ans

print(
    four_sum_count(a,b,c,d)
)