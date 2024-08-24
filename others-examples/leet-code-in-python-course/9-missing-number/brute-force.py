numbers = [3,0,1]

def find_missing_number(numbers):
    numbers = sorted(numbers)
    for i in range(0,len(numbers) + 1):
        if i != numbers[i]:
            return i

print(
    find_missing_number(numbers)
)