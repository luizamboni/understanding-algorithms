numbers = [3,0,1]

def find_missing_number(numbers):
    n = len(numbers)
    expectedSum = n*(n+1)/2 # gauss sum of all numbers in a sequence
    actualSum = sum(numbers)
    return int(expectedSum - actualSum)
    


print(
    find_missing_number(numbers)
)