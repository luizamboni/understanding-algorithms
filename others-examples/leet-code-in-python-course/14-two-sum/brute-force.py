
values = [2,11,7,15]

def find_two_sum(target: int):
    for i in range(len(values)):
        desired = target - values[i] 
        for j in range(i +1, len(values)):
            if desired == values[j]:
                return i, j
            

print(
    find_two_sum(26)
)