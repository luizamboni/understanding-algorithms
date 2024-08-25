
values = [2,11,7,15]

def find_two_sum(target: int):
    desireds = {}
    for i in range(len(values)):
        
        desired_value = target - values[i]
        if values[i] in desireds:
            return i, desireds[values[i]]
        
        desireds[desired_value] = i
        print(desireds)

print(
    find_two_sum(26)
)