numbers = [2,1,3,1]

def check(numbers: list):

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # print(i, j)
            if numbers[i] == numbers[j]:
                return True

    return False


print(
    check(numbers)
)