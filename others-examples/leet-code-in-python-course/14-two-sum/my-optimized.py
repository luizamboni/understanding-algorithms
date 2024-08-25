
values = [2,11,7,15]

def find_two_sum(target: int):
    desireds = {}
    for i in range(len(values)):
        desireds[target - values[i]] = i
    
    for i in range(len(values)):
        if desireds.get(values[i]):
            return i, desireds.get(values[i])
            

print(
    find_two_sum(26)
)