numbers = [2,1,3,1]

def check(numbers: list):
    m = {}
    for i in range(len(numbers)):
        if numbers[i] in m:
            return True
        m[numbers[i]] = True

    return False


print(
    check(numbers)
)